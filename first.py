import argparse

from google.cloud import language


def analyze_annot(annotations):
    totalscore = 0

    for index, sentence in enumerate(annotations.sentences):
        sentiment_tmp = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentiment_tmp))
        totalscore += sentiment_tmp

    print("total score is")
    print(totalscore)
    return 0


def analyze(wikipedia_news_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    language_client = language.Client()

    with open(wikipedia_news_filename, 'r') as news_file:
        document = language_client.document_from_text(news_file.read())

        annotations = document.annotate_text(include_sentiment=True,
                                             include_syntax=False,
                                             include_entities=False)

        # analyze the annotations and collect sentiments
        analyze_annot(annotations)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'wikipedia_news_filename',
        help='The file you\'d like to analyze.')
    args = parser.parse_args()

    analyze(args.wikipedia_news_filename)
