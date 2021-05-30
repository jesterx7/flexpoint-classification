
# load user movement dataset into memory
from sklearn.preprocessing import StandardScaler
from pandas import read_csv
from os import listdir
from numpy import vstack
from numpy import array
from numpy import savetxt
from matplotlib import pyplot
import joblib

def csv_to_df(file):
	df = read_csv(file, header=None)
	values = df.values

	return values

def transform_data(sequences):
	# create the transformed dataset
	transformed = list()
	n_vars = 10
	n_steps = 100
	# process each trace in turn
	for i in range(len(sequences)):
		seq = sequences[i]
		vector = list()
		# last n observations
		for row in range(1, n_steps+1):
			for col in range(n_vars):
				vector.append(seq[-row, col])
		# store
		transformed.append(vector)
	# prepare array
	transformed = array(transformed)
	transformed = transformed.astype('float32')
	return transformed

pred_data = csv_to_df('Sign/dataset_number/7_5.csv')
pred_data = transform_data([pred_data])
model = joblib.load('model_RF.pkl')
prediction = model.predict(pred_data)

print(prediction)

