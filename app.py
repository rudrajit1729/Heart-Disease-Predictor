# Checkpoint 2 - Creating a web application

# Import Libraries
from flask import Flask, request, render_template
import numpy as np
import train_model as tm # Load Model created in Checkpoint 1

# Creating flask app 
app = Flask(__name__)
#temp
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        # TODO
        '''
            Take Input from the form and process data 
            to finally use model to predict results.
        '''
        
        #result = np.array([[57, 140, 240, 162, 1.6, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0]])
        print(result.dtype)

        pred = tm.model_prediction(result)
        return render_template('result.html', prediction = pred)

if __name__ == '__main__':
    app.run(debug = True)
