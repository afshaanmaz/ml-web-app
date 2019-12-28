from flask import Flask, render_template, url_for, request
#import keras

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


# request.args contains all the arguments passed by our form
    # comes built in with flask. It is a dictionary of the form
    # "form name (as set in template)" (key): "string in the    
    # textbox" (value)
    

@app.route('/predict')
def predict():

    print(request.args)
    #model = keras.load_model('abc.h5')

    # if request.args:
    #     comment = request.form['comment']
    # else: comment = ''
    
    if request.method == 'POST':
        comment = request.form['comment']
        
       
    return render_template('home.html', prediction="Hello")





if __name__ =='__main__':
    app.run(debug=True)

"""
TODO: 
- Return results on console



https://towardsdatascience.com/deploying-models-to-flask-fb62155ca2c4
https://www.youtube.com/watch?v=tFjeUtFay_Q&t=277s
"""
