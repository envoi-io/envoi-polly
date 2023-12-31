# Envoi AWS Polly Utility

Prerequisites

- AWS CLI

    You will need to have the AWS CLI installed and configured with a profile configured to access the AWS account
    you want to use

```shell
usage: envoi_polly.py [-h] [--output-format {json,mp3,ogg_vorbis,pcm}] [--output-s3-bucket-name OUTPUT_S3_BUCKET_NAME] [--text TEXT]
                      [--voice-id {Aditi,Amy,Astrid,Bianca,Brian,Camila,Carla,Carmen,Celine,Chantal,Conchita,Cristiano,Dora,Emma,Enrique,Ewa,Filiz,Gabrielle,Geraint,Giorgio,Gwyneth,Hans,Ines,Ivy,Jacek,Jan,Joanna,Joey,Justin,Karl,Kendra,Kevin,Kimberly,Lea,Liv,Lotte,Lucia,Lupe,Mads,Maja,Marlene,Mathieu,Matthew,Maxim,Mia,Miguel,Mizuki,Naja,Nicole,Olivia,Penelope,Raveena,Ricardo,Ruben,Russell,Salli,Seoyeon,Takumi,Tatyana,Vicki,Vitoria,Zeina,Zhiyu}]
                      [--engine {standard,neural,long-form}] [--language-code LANGUAGE_CODE] [--lexicon-names LEXICON_NAMES] [--output-s3-key-prefix OUTPUT_S3_KEY_PREFIX] [--sample-rate SAMPLE_RATE] [--sns-topic-arn SNS_TOPIC_ARN] [--speech-mark-types SPEECH_MARK_TYPES] [--text-type {ssml,text}]

Envoi AWS Polly Utility

Executes an AWS Polly Start Speech Synthesis Task 

options:
  -h, --help            show this help message and exit
  --output-format {json,mp3,ogg_vorbis,pcm}
                        The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json. (default: None)
  --output-s3-bucket-name OUTPUT_S3_BUCKET_NAME
                        The name of the Amazon S3 bucket in which the output file will be stored. (default: None)
  --text TEXT           The input text to synthesize. (default: None)
  --voice-id {Aditi,Amy,Astrid,Bianca,Brian,Camila,Carla,Carmen,Celine,Chantal,Conchita,Cristiano,Dora,Emma,Enrique,Ewa,Filiz,Gabrielle,Geraint,Giorgio,Gwyneth,Hans,Ines,Ivy,Jacek,Jan,Joanna,Joey,Justin,Karl,Kendra,Kevin,Kimberly,Lea,Liv,Lotte,Lucia,Lupe,Mads,Maja,Marlene,Mathieu,Matthew,Maxim,Mia,Miguel,Mizuki,Naja,Nicole,Olivia,Penelope,Raveena,Ricardo,Ruben,Russell,Salli,Seoyeon,Takumi,Tatyana,Vicki,Vitoria,Zeina,Zhiyu}
                        The voice ID to use for synthesis. (default: None)
  --engine {standard,neural,long-form}
                        Specifies the engine (standard, neural or long-form) for Amazon Polly to use when processing input text for speech synthesis. (default: None)
  --language-code LANGUAGE_CODE
                        The language code for the input text. (default: None)
  --lexicon-names LEXICON_NAMES
                        List of one or more pronunciation lexicon names you want the service to apply during synthesis. (default: None)
  --output-s3-key-prefix OUTPUT_S3_KEY_PREFIX
                        The Amazon S3 key prefix for the output speech file. (default: None)
  --sample-rate SAMPLE_RATE
                        The audio frequency specified in Hz. (default: None)
  --sns-topic-arn SNS_TOPIC_ARN
                        The ARN of the Amazon SNS topic you want to publish feedback about your speech synthesis. (default: None)
  --speech-mark-types SPEECH_MARK_TYPES
                        The type of speech marks returned for the input text. (default: None)
  --text-type {ssml,text}
                        The type of input text. (default: None)
```