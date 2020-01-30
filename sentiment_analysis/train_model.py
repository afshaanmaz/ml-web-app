"""

"""

from Sentiment_Analysis import SentimentAnalysis


# Load data

def load_data(file_path=None):
    reviews_train = []
    for line in open('../data/movie_data/full_train.txt', 'r'):

        reviews_train.append(line.strip())


    reviews_test = []
    for line in open('../data/movie_data/full_test.txt', 'r'):

        reviews_test.append(line.strip())

    # TODO: Also return targets at this point

    return reviews_train, reviews_test


def main():

    reviews_train, reviews_test = load_data()

    ml_api = SentimentAnalysis()


    reviews_train_clean = [ml_api.preprocess_reviews(line) for line in reviews_train]
    reviews_test_clean = [ml_api.preprocess_reviews(line) for line in reviews_test]

    pass


if __name__ == "___main__":
    main()
