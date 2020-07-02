# Heart-Disease-Predictor
Treat Your Heart Right

For live demo visit - https://heart-disease-bitninjas.herokuapp.com/

Checkout video explanation at - https://www.youtube.com/watch?v=qn2hcp8E76c

A web application which uses Machine Learning models to predict the heart condition of a user by providing some inputs about the user's health like age, blood pressure, cholesterol level etc.

It is seen that most people above a certain age are diagnosed with heart disease. In order to keep track of your heart condition whether you are diagnosed with heart disease or not, we created this web app. It uses a regression model to analyze the parameters provided by the user such as age, blood pressure, cholesterol level, thalassemia condition, max heart rate etc and predicts whether the user is diagnosed with heart disease or not. The model is trained using a dataset provided by Kaggle. Our model upon training gives an accuracy of nearly 85% which we plan to improve further.

Developed by team BitNinjas 🦋
Contributors: Avirup Aditya, Rudrajit Choudhuri, Debargha Ghosh

## Dataset Link - https://www.kaggle.com/ronitf/heart-disease-uci?select=heart.csv

This dataset comprises of the below given attributes which will be used to predict a person's heart health and thereby heart disease using Machine Learning and Analytics techniques. After building a robust ML model we will build an user friendly web application for the non technical users to use without having to figure out the working of the algorithm. We mainly focus on creating a web application where number of such diseases(malaria, covid19, breast cancer, skin cancer, etc.) can be predicted all in one place in further versions of the project. Basic idea is to create a one shop stop for prediction of a wide range of diseases to maximum achievable accuracy and precision.

## Attributes
- age
- sex
- chest pain type (4 values)[typical angina(0)/atypical angina(1)/non-anginal pain(2)/asymptotic(3)]
- resting blood pressure
- serum cholestoral in mg/dl
- fasting blood sugar > 120 mg/dl(yes/no)
- resting electrocardiographic results (Normal(0),ST-Wave Abnormality(1),left ventricular hypertrophy(2))
- maximum heart rate achieved
- exercise induced angina
- oldpeak = ST depression induced by exercise relative to rest
- the slope of the peak exercise ST segment
- number of major vessels (0-3) colored by flourosopy
- thal: 0 = normal; 1 = fixed defect; 2 = reversable defect


## Goal
We intend to create an end to end deployable web application to help medical experts predict the heart health based on the above parameters.

### Checkpoint 1
To be able to build/apply a robust Machine Learning algorithm to ensure accurate results.

### Checkpoint 2
Many have predicted the disease before but we need a user friendly interface for non technical users to use the above without having to figure out the working of the model. This web interface can then be scaled to predict other diseases and acutally create an application to predict some of the major diseases under one umbrella.

### Checkpoint 3
After building the web application we need to deploy it on some server for people to access it easily. We would preferably use herokuapp for the same.


## Acknowledgements
### Creators:
- Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
- University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
- University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
- V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.
- Donor: David W. Aha (aha '@' ics.uci.edu) (714) 856-8779


## Inspiration
Experiments with the Cleveland database have concentrated on simply attempting to distinguish presence (values 1,2,3,4) from absence (value 0).

See if you can find any other trends in heart data to predict certain cardiovascular events or find any clear indications of heart health.
