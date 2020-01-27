"""
This script contains all the code needed to interface with a Flask App
Accepts user input, preprocesses it, converts to a feature 
"""
import re

#from sklearn.feature_extraction.text import CountVectorizer
# cv = CountVectorizer(binary=True)
# cv.fit(reviews_train_clean)
# X = cv.transform(reviews_train_clean)
# X_test = cv.transform(reviews_test_clean)



def remove_escapes(input_string):
    escapes = ''.join([chr(char) for char in range(1, 32)]) 
    # all escape sequences have an ANSI encoding value between 1 and 32
    
    translator = str.maketrans('', '', escapes) # Different syntax for py2/ py3 / py3.1 +
    output_string = input_string.translate(translator)
    return output_string


def preprocess_reviews(input_string):
    """
    """
    REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])|(\_)|(\d+)")
    REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
    NO_SPACE = ""
    SPACE = " "
    
    input_string = remove_escapes(input_string)
    input_string = REPLACE_NO_SPACE.sub(NO_SPACE, input_string.lower())
    input_string = REPLACE_WITH_SPACE.sub(SPACE, input_string)
    
    return input_string





def main():


    reviews_train_clean = [preprocess_reviews(line) for line in reviews_train]
    reviews_test_clean = [preprocess_reviews(line) for line in reviews_test]



    pass

if __name__=="___main__":
    main()
