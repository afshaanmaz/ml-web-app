"""
TODO: 
- Add data to folder

"""

# Load data

def load_data():
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


    reviews_train_clean = [preprocess_reviews(line) for line in reviews_train]
    reviews_test_clean = [preprocess_reviews(line) for line in reviews_test]



    pass