"""Basic app to demonstrate anatomy of flask"""

from flask import Flask, render_template, request
import sentiment_analysis.api_sentiment_analysis as senti_api
app = Flask(__name__)


@app.route('/predict')
def predict():
    """ Preprocess and pass the user input to the ML api. Display the prediction with a render template """

    # Step 3c-1:
    user_input = accept_user_input()
    print('User input = ', user_input)

    # Preprocess input - Remember to import the file from sentiment analysis
    preprocessed_data = senti_api.preprocess_reviews(user_input)

    # Step 3c-2
    # Send the preprocessed data to the ML model
    sentiment = test.inference(preprocessed_data)

    # Send the prediction to the web app
    return render_template('predict.html', predicted_out=sentiment)


def accept_user_input():
    """Accept user input with forms"""

    if request.args:
        user_input = request.args['user_review']
    else:
        user_input = ''

    return user_input


@app.route('/display_data')
def display_data():
    """Accept user input and display the user input using render template"""

    # Step 3b-2
    # Accept user input and print to html
    user_input = accept_user_input()
    print('User input = ', user_input)
    return render_template('display_data.html', user_input=user_input)


@app.route('/')
def hello_world():
    """Basic function for simply displaying a statement via Flask"""

    # Step 3a:
    # return 'Hello from Flask!'

    # Step 3b-1:
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
