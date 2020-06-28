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
        age = int(request.form['age'])
        sex = str(request.form['sex'])
        cp = str(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = str(request.form['chol'])
        fbs = str(request.form['fbs'])
        restecg = str(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = str(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = str(request.form['slope'])
        ca = str(request.form['ca'])
        thal = str(request.form['thal']) 
        
        #new ones
        if(sex == '0'):
            sex_0 = 1
            sex_1 = 0
        else:
            sex_0 = 1
            sex_1 = 0

        
        cp_0 = 0
        cp_1 = 0
        cp_2 = 0
        cp_3 = 0
        if(cp == '0'):
            cp_0 = 1
        elif(cp == '1'):
            cp_1 = 1
        elif(cp == '2'):
            cp_2 = 1
        else:
            cp_3 = 1


        if(fbs == '0'):
            fbs_0 = 1
            fbs_1 = 0
        else:
            fbs_0 = 0
            fbs_1 = 1


        restecg_0 = 0
        restecg_1 = 0
        restecg_2 = 0
        if(restecg == '0'):
            restecg_0 = 1
        elif(restecg == '1'):
            restecg_1 = 1
        else:
            restecg_2 = 1

        if(exang == '0'):
            exang_0 = 1
            exang_1 = 0
        else:
            exang_0 = 0
            exang_1 = 1

        slope_0 = 0
        slope_1 = 0
        slope_2 = 0
        if(slope == '0'):
            slope_0 = 1
        elif(slope == '1'):
            slope_1 = 1
        else:
            slope_2 = 1

        ca_0 = 0
        ca_1 = 0
        ca_2 = 0
        ca_3 = 0
        ca_4 = 0
        if(ca == '0'):
            ca_0 = 1
        elif(ca == '1'):
            ca_1 = 1
        elif(ca == '2'):
            ca_2 = 1
        elif(ca == '3'):
            ca_3 = 1
        else:
            ca_4 = 1


        thal_0 = 0
        thal_1 = 0
        thal_2 = 0
        thal_3 = 0
        if(thal == '0'):
            thal_0 = 1
        elif(thal == '1'):
            thal_1 = 1
        elif(thal == '2'):
            thal_2 = 1
        else:
            thal_3 = 1  

        result = np.array([[int(age), int(trestbps), int(chol), int(thalach), float(oldpeak), int(sex_0), int(sex_1), int(cp_0), int(cp_1), int(cp_2), int(cp_3), int(fbs_0), int(fbs_1), int(restecg_0), int(restecg_1), int(restecg_2), int(exang_0), int(exang_1), int(slope_0), int(slope_1), int(slope_2), int(ca_0), int(ca_1), int(ca_2), int(ca_3), int(ca_4), int(thal_0), int(thal_1), int(thal_2), int(thal_3)]])
        #result = np.array([[57, 140, 240, 162, 1.6, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0]])
        print(result.dtype)

        pred = tm.model_prediction(result)
        return render_template('result.html', prediction = pred)

if __name__ == '__main__':
    app.run(debug = True)
