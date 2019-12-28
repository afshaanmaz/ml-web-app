from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict')
def predict():
    return render_template('result.html')


if __name__ =='__main__':
    app.run(debug=True)