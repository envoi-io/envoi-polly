#!/usr/bin/env python3
import argparse
import sys

try:
    # noinspection PyUnresolvedReferences
    import boto3
except ImportError:
    if __name__ == '__main__':
        print("Missing dependency boto3. Try running 'pip install boto3'")
        sys.exit(1)


class EnvoiArgumentParser(argparse.ArgumentParser):

    def to_dict(self):
        # noinspection PyProtectedMember
        return {a.dest: a.default for a in self._actions if isinstance(a, argparse._StoreAction)}


class EnvoiCommand:
    command_dest = "command"
    description = ""
    subcommands = {}

    def __init__(self, opts=None, auto_exec=True):
        self.opts = opts or {}
        if auto_exec:
            self.run()

    @classmethod
    def init_parser(cls, command_name=None, parent_parsers=None, subparsers=None,
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter):
        if subparsers is None:
            parser = EnvoiArgumentParser(description=cls.description, parents=parent_parsers or [],
                                         formatter_class=formatter_class)
        else:
            parser = subparsers.add_parser(command_name or cls.__name__.lower(), help=cls.description,
                                           parents=parent_parsers or [],
                                           formatter_class=formatter_class)
        parser.set_defaults(handler=cls)

        if cls.subcommands:
            cls.process_subcommands(parser=parser, parent_parsers=parent_parsers, subcommands=cls.subcommands)

        return parser

    @classmethod
    def process_subcommands(cls, parser, parent_parsers, subcommands, dest=None, add_subparser_args=None):
        subcommand_parsers = {}
        if add_subparser_args is None:
            add_subparser_args = {}
        if dest is not None:
            add_subparser_args['dest'] = dest
        subparsers = parser.add_subparsers(**add_subparser_args)

        for subcommand_name, subcommand_info in subcommands.items():
            if not isinstance(subcommand_info, dict):
                subcommand_info = {"handler": subcommand_info}
            subcommand_handler = subcommand_info.get("handler", None)
            if subcommand_handler is None:
                continue
            if isinstance(subcommand_handler, str):
                subcommand_handler = globals()[subcommand_handler]

            subcommand_parser = subcommand_handler.init_parser(command_name=subcommand_name,
                                                               parent_parsers=parent_parsers,
                                                               subparsers=subparsers)
            subcommand_parser.required = subcommand_info.get("required", True)
            subcommand_parsers[subcommand_name] = subcommand_parser

        return parser

    def run(self):
        pass


class EnvoiAwsPollyStartSpeechSynthesisTaskCommand(EnvoiCommand):
    description = "Envoi Polly Start Synthesis Task Utility"

    @classmethod
    def init_parser(cls, **kwargs):
        parser = super().init_parser(**kwargs)

        parser.add_argument("--output-format",
                            help="The format in which the returned output will be encoded. For audio stream, this will "
                            "be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.",
                            choices=["json", "mp3", "ogg_vorbis", "pcm"])
        parser.add_argument("--output-s3-bucket-name",
                            help="The name of the Amazon S3 bucket in which the output file will be stored.")
        parser.add_argument("--text",
                            help="The input text to synthesize.")
        # noinspection SpellCheckingInspection
        parser.add_argument("--voice-id",
                            help="The voice ID to use for synthesis.",
                            choices=["Aditi", "Amy", "Astrid",
                                     "Bianca", "Brian",
                                     "Camila", "Carla", "Carmen", "Celine", "Chantal", "Conchita", "Cristiano",
                                     "Dora",
                                     "Emma", "Enrique", "Ewa", "Filiz",
                                     "Gabrielle", "Geraint", "Giorgio", "Gwyneth",
                                     "Hans", "Ines", "Ivy",
                                     "Jacek", "Jan", "Joanna", "Joey", "Justin",
                                     "Karl", "Kendra", "Kevin", "Kimberly",
                                     "Lea", "Liv", "Lotte", "Lucia", "Lupe",
                                     "Mads", "Maja", "Marlene", "Mathieu", "Matthew", "Maxim", "Mia", "Miguel",
                                     "Mizuki",
                                     "Naja", "Nicole", "Olivia", "Penelope",
                                     "Raveena", "Ricardo", "Ruben", "Russell",
                                     "Salli", "Seoyeon", "Takumi",
                                     "Tatyana",
                                     "Vicki", "Vitoria",
                                     "Zeina", "Zhiyu"])

        # Optional Parameters
        parser.add_argument("--engine",
                            help="Specifies the engine (standard, neural or long-form) for Amazon Polly to use when "
                            "processing input text for speech synthesis.",
                            choices=["standard", "neural", "long-form"])
        parser.add_argument("--language-code",
                            help="The language code for the input text.")
        parser.add_argument("--lexicon-names",
                            help="List of one or more pronunciation lexicon names you want the service to apply during "
                            "synthesis.")
        parser.add_argument("--output-s3-key-prefix",
                            help="The Amazon S3 key prefix for the output speech file.")
        parser.add_argument("--sample-rate",
                            help="The audio frequency specified in Hz.")
        parser.add_argument("--sns-topic-arn",
                            help="The ARN of the Amazon SNS topic you want to publish feedback about your speech "
                            "synthesis.")
        parser.add_argument("--speech-mark-types",
                            help="The type of speech marks returned for the input text.")
        parser.add_argument("--text-type",
                            help="The type of input text.",
                            choices=["ssml", "text"])
        return parser

    def run(self, opts=None):
        if opts is None:
            opts = self.opts

        command_args = {
            "OutputFormat": getattr(opts, "output_format", None),
            "OutputS3BucketName": getattr(opts, "output_s3_bucket_name", None),
            "Text": getattr(opts, "text", None),
            "VoiceId": getattr(opts, "voice_id", None),
        }

        optional_args = {
            "engine": "Engine",
            "language-code": "LanguageCode",
            "lexicon-names": "LexiconNames",
            "output-s3-key-prefix": "OutputS3KeyPrefix",
            "sample-rate": "SampleRate",
            "sns-topic-arn": "SnsTopicArn",
            "speech-mark-types": "SpeechMarkTypes",
            "text-type": "TextType",
        }

        for opt_name, arg_name in optional_args.items():
            opt_value = getattr(opts, opt_name, None)
            if opt_value is not None:
                command_args[arg_name] = opt_value

        client = boto3.client('polly')
        response = client.start_speech_synthesis_task(**command_args)
        print(response['SynthesisTask'])
        return response


def main():
    parser = EnvoiAwsPollyStartSpeechSynthesisTaskCommand.init_parser()
    opts, unknown_args = parser.parse_known_args()
    EnvoiAwsPollyStartSpeechSynthesisTaskCommand(opts=opts)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

