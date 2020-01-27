from flask import Flask, render_template, url_for, request, flash, redirect
from forms import UserInputForm

from sentiment_analysis.preprocess_data import *

import secrets
key = secrets.token_hex(16)

app = Flask(__name__)

app.config["SECRET_KEY"] = key


@app.route('/')
def home():
    return render_template('basic_home.html', title='user supplied')


@app.route('/enter_data', methods=['GET', 'POST'])
def python_form():
    form = UserInputForm()

    if form.is_submitted():
        print("submitted")
        flash('Is this what you typed ? {}'.format(form.textdata.data), 'success' )
        return redirect(url_for('home'))
    else:
    # if form.validate_on_submit():
    #     flash('Is this what you typed ?{}'.format(form.textdata.data), 'success' )
    #     return redirect(url_for('home'))
        return render_template('display_data.html', form= form)


if __name__ =='__main__':
    app.run(debug=True)




"""

Forms need a lot of data validation 

pip install flask_wtf for forms:

two ways to integrate forms  - html vs flask-wtf

"""