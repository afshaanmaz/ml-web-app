"""
display data on website.

Adapted from : https://www.youtube.com/watch?v=QnDWIZuWYW0
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/02-Templates

"""


from flask import Flask, render_template, url_for, request


app = Flask(__name__)


data_to_display = [
    {
        "name": "Jane Doe",
        "number": "123456"
    }, 
    {
        "name": "John Smith",
        "number": "789101"
    }
]

@app.route('/')
def home():
    return render_template('home.html', display=data_to_display)

"""
We have access to the variable called "display" in pur template, 
by passing it in as an argument in render_template
"""



if __name__ =='__main__':
    app.run(debug=True)

"""
TODO: 
- if else block 
- template inheritance



Child templates can override a block 
 - Bootstrap for simple+ responsive styling


- url_for links to the static folder in the app, also provide a filename='something.css'

that tells you how to style it

whats a container in html ?

static files like css and javascript need to live in the static folder for a flask app


https://towardsdatascience.com/deploying-models-to-flask-fb62155ca2c4
https://www.youtube.com/watch?v=tFjeUtFay_Q&t=277s
"""
