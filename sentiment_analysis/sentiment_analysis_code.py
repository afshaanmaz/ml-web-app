"""

This script contains all the code needed to train a sentiment analysis model
and to interface with a Flask App
Accepts user input, pre-processes it, converts to a feature
Then it predicts whether the review was positive or negative using
Logistic Regression on the feature vector

"""

import re
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import os

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def load_data(file_path=None):
    reviews_train = []
    for line in open('./data/movie_data/full_train.txt', 'r'):

        reviews_train.append(line.strip())

    reviews_test = []
    for line in open('./data/movie_data/full_test.txt', 'r'):

        reviews_test.append(line.strip())

    # TODO: Also return targets at this point

    return reviews_train, reviews_test


def remove_escapes(input_string):
    escapes = ''.join([chr(char) for char in range(1, 32)])
    # all escape sequences have an ANSI encoding value between 1 and 32

    translator = str.maketrans('', '', escapes)
    output_string = input_string.translate(translator)
    return output_string


def preprocess_reviews(input_string):
    """ preproceses a single string
    """
    REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])|(\_)|(\d+)")
    REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
    NO_SPACE = ""
    SPACE = " "

    input_string = remove_escapes(input_string)
    input_string = REPLACE_NO_SPACE.sub(NO_SPACE, input_string.lower())
    input_string = REPLACE_WITH_SPACE.sub(SPACE, input_string)

    return input_string


def create_feature_transform(train=False, training_data=None):
    """
    training_data should be a list of preprocessed strings
    """
    vectorizer = CountVectorizer(binary=True, decode_error="replace", strip_accents='unicode',
                                 stop_words='english', min_df=0.001
                                 )
    # min_df: Remove proper nouns - any word occuring less than 0.01% of all words in the dataset

    if train is True and training_data is not None:
        vectorizer.fit(training_data)

    return vectorizer


def get_feature_vectors(input_string_list, vectorizer):
    """
    Takes in a list of strings
    """
    input_feature_vectors = vectorizer.transform(input_string_list)

    return input_feature_vectors


def cross_validate(X_features, target):
    X_train, X_val, y_train, y_val = train_test_split(
    X_features, target, train_size = 0.75)
    
    for c in [0.01, 0.05, 0.25, 0.5, 1]:
        lr = LogisticRegression(C=c)
        lr.fit(X_train, y_train)
        print("Accuracy for C=%s: %s"% (c, accuracy_score(y_val, lr.predict(X_val))))
    pass


# inference script - interfaces with the ML api
def get_model_prediction(user_input):
    user_input_processed = preprocess_reviews(user_input)

    # Load saved model - vectorizer
    script_path = os.path.dirname(os.path.abspath(__file__))
    saved_vectorizer = pickle.load(open(os.path.join
                                        (script_path, './model/vectorizer.pkl'), 'rb'))

    # Get feature vector
    user_data_vector = saved_vectorizer.transform([user_input_processed, ''])[:-1]
    # extra string cuz it expects more than one document to transform

    # load saved logreg model
    saved_model = pickle.load(open(os.path.join
                     (script_path, './model/log_reg_model.pkl'), 'rb'))

    # get prediction from saved model
    result = saved_model.predict(user_data_vector)[0]

    # It returns an integer, just being conservative here to deal with precision errors

    if result >= 0.5:
        return 'Positive'
    elif result < 0.5:
        return 'Negative'
    else:
        return 'Error'

    pass



def train_model():
    print('Loading data ...')
    # load data
    reviews_train, reviews_test = load_data()

    print(len(reviews_train))

    print('\nPreprocessing data ...')

    # preprocess data
    reviews_train_clean = [preprocess_reviews(line) for line in reviews_train]
    reviews_test_clean = [preprocess_reviews(line) for line in reviews_test]

    print(len(reviews_train_clean))

    print('\nCreating Feature Vectors ...')

    # create feature vectorizer
    # optional: set the params of vectorizer here
    vectorizer = create_feature_transform(train=True, training_data=reviews_train_clean)

    print(vectorizer)

    # Save the vectorizer
    pickle.dump(vectorizer, open("./model/vectorizer.pkl", "wb"))


    
    # Get Feature Vectors
    X_data = get_feature_vectors(reviews_train_clean, vectorizer)

    X_test = get_feature_vectors(reviews_test_clean, vectorizer)
    
    print(X_data.shape)
    
    # Load the target label for the training data
    # We're able to set the target like this because we know the reviews are ordered
    # as being positive for the first 12500 and negative for the next 12500 (for both train and test data)
    target = [1 if i < 12500 else 0 for i in range(25000)]

    print('\nCross Validation ...')

    # Cross Validate
    cross_validate(X_data, target)
    
    # At this point you can change the regularization term C based on results from cross validation
    print('\nFitting and saving the best model ...')
    
    final_model = LogisticRegression(C=0.05)
    final_model.fit(X_data, target)
    print("Final Accuracy on Test Set: %s"
           % accuracy_score(target, final_model.predict(X_test)))
    # Final Accuracy: ~0.87552
    
    # Save the final_model
    pickle.dump(final_model, open("./model/log_reg_model.pkl", "wb"))

    print('\nSaved Trained Logistic Regression model')

    pass

def test_inference():
    pos_str = 'This movie was excellent, so good, best thing ever'
    neg_str = 'The worst thing Ive ever seen terrible horrible bad'

    print('\n', get_model_prediction(pos_str), pos_str)
    print('\n', get_model_prediction(neg_str), neg_str)



if __name__ == '__main__':
    #train_model()
    test_inference()




