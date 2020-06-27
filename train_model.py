# Checkpoint 1 - Training the model

# Importing Libraries
import pandas as pd
import numpy as np

def model_prediction(result):

	# Importing dataset
	dataset = pd.read_csv("heart_disease.csv")

	# Getting dummies for categorical variables
	dataset = pd.get_dummies(dataset, columns=['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])

	# Feature Scaling
	from sklearn.preprocessing import StandardScaler
	sc = StandardScaler()
	columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
	dataset[columns_to_scale] = sc.fit_transform(dataset[columns_to_scale])

	# Splitting the dataset into dependent variable vector and independent features
	X = dataset.drop('target', axis=1)
	y = dataset['target']

	# Splitting the dataset into training and test set
	from sklearn.model_selection import train_test_split, cross_val_score
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

	# Loading/Creating the model

	try:
		model = 'heart-disease-predictor-model.pkl'
		classifier = pickle.load(open(model, 'rb'))
	except:
		# Fitting Logistic Regression to the model
		from sklearn.linear_model import LogisticRegression

		# Creating a Logistic Regression model
		classifier = LogisticRegression(solver='lbfgs', multi_class='auto', max_iter = 7600)
		scores = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
		#print("Linear Regression Classifier Accuracy(C = 1) : {}%".format(round(scores.mean(), 4)*100))

		# Fitting it to the dataset
		classifier.fit(X_train, y_train)

		# Model Evaluation

		# Creating a confusion matrix for training set
		from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
		y_train_pred = classifier.predict(X_train)
		cm = confusion_matrix(y_train, y_train_pred)
		#print(cm)
		# Accuracy Score
		score = round(accuracy_score(y_train, y_train_pred),4)*100
		#print("Accuracy on trainning set: {}%".format(score))

		# Saving the model
		import pickle
		# Creating a pickle file for the classifier
		filename = 'heart-disease-predictor-model.pkl'
		pickle.dump(classifier, open(filename, 'wb'))
		#print("Model Saved Successfully")

	result[0][0:5] = sc.transform([result[0][0:5]])
	pred = classifier.predict(result)
	return pred


result = np.array([[57, 140, 240, 162, 1.6, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0]])
print(model_prediction(result))


