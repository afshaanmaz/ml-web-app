"""
Inference or accessing ML model

This script contains all the code needed to interface with a Flask App
Accepts user input, pre-processes it, converts to a feature
"""


## ** this is faulty - fix it
from train_model import preprocess_reviews, get_feature_vectors, get_model_prediction

def main(user_input):
    user_input_processed = preprocess_reviews(user_input)

    # Load saved model - vectorizer
    saved_vectorizer = pickle.load(open('./model/vectorizer.pkl', 'rb'))

    # Get feature vector
    user_data_vector = saved_vectorizer.transform([user_input_processed, ''])[:-1]
    #extra string cuz it expects more than one document to transform

    # load saved logreg model
    saved_model = pickle.load(open('./model/log_reg_model.pkl', 'rb'))


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

if __name__=='___main__':
    main()
