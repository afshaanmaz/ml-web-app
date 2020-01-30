
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import re

class SentimentAnalysis():

    # should I make the string and the prediction init params ?
    def __init__(self):
        pass

    def remove_escapes(self, input_string):
        escapes = ''.join([chr(char) for char in range(1, 32)])
        # all escape sequences have an ANSI encoding value between 1 and 32

        translator = str.maketrans('', '', escapes)
        output_string = input_string.translate(translator)
        return output_string

    def preprocess_reviews(self, input_string):
        """ preproceses a single string
        """
        REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])|(\_)|(\d+)")
        REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
        NO_SPACE = ""
        SPACE = " "

        input_string = self.remove_escapes(input_string)
        input_string = REPLACE_NO_SPACE.sub(NO_SPACE, input_string.lower())
        input_string = REPLACE_WITH_SPACE.sub(SPACE, input_string)

        return input_string

    def create_feature_transform(self, params_dict=None, train=False, training_data=None):
        """

        """
        # TODO: Include params for CountVectorizer from values in params_dict

        vectorizer = CountVectorizer(binary=True, decode_error="replace", strip_accents='unicode',
                                     stop_words='english', min_df=0.005
                                     )

        if train is True and training_data is not None:
            vectorizer.fit(reviews_train_clean)

        return vectorizer





