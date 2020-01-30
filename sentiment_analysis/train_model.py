"""

"""

from Sentiment_Analysis import *


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


def get_test_accuracy(test_dataset): # Can live in the main script as well
    pass


def main():

    # load data
    reviews_train, reviews_test = load_data()

    # preprocess data
    reviews_train_clean = [preprocess_reviews(line) for line in reviews_train]
    reviews_test_clean = [preprocess_reviews(line) for line in reviews_test]

    # create feature vectorizer
    # optional: set the params of vectorizer here
    vectorizer = create_feature_transform(params_dict=None, train=True, training_data=reviews_train_clean)


    # Save the vectorizer
    pickle.dump(vectorizer, open("./model/count_vectorizer_object.pkl", "wb"))



    pass


if __name__ == "___main__":
    main()
