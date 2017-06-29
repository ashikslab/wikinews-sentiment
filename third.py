import argparse

from google.cloud import language


def analyze_annot(annotations):
    totval = 0
    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        totval += sentence_sentiment

    if totval <-0.5: print("Not at all a good day")
    elif totval<0: print("Today looks like not a very good day")
    elif totval<0.2: print("Today is just a regular day. Not a lot of depressing news")
    elif totval<0.4: print("Looks like today is a good day")
    else: print("Today is a very good day, can't complain!")
    return 0

def analyze(wikipedia_news_filename):
    """call the cloud nlp API."""
    language_client = language.Client()

    with open(wikipedia_news_filename, 'r') as news_file:
        document = language_client.document_from_text(news_file.read())

        annotations = document.annotate_text(include_sentiment=True,
                                             include_syntax=False,
                                             include_entities=False)

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
