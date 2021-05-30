
# load user movement dataset into memory
from pandas import read_csv
from os import listdir
import os
from numpy import vstack
from numpy import array
from numpy import savetxt
from matplotlib import pyplot

# return list of traces, and arrays for targets, groups and paths
def load_dataset(prefix=''):
	grps_dir, data_dir = prefix+'groups_number/', prefix+'dataset_number/'
	# load mapping files
	targets = read_csv(data_dir + 'targets.csv', header=0)
	groups = read_csv(grps_dir + 'groups.csv', header=0)
	# load traces
	sequences = list()
	target_mapping = None
	lstdir = listdir(data_dir)
	for name in sorted(lstdir):
		filename = data_dir + name
		if filename == 'target.csv':
			continue
		df = read_csv(filename, header=None)
		values = df.values
		sequences.append(values)
	return sequences, targets.values[:,1], groups.values[:,1]

def create_dataset(sequences, targets):
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
		# add output
		vector.append(targets[i])
		# store
		transformed.append(vector)
	# prepare array
	transformed = array(transformed)
	transformed = transformed.astype('float32')
	return transformed

# load dataset
sequences, targets, groups = load_dataset('Sign/')
# separate traces
seq1 = [sequences[i] for i in range(len(groups)) if groups[i]==1]
seq2 = [sequences[i] for i in range(len(groups)) if groups[i]==2]
# separate target
targets1 = [targets[i] for i in range(len(groups)) if groups[i]==1]
targets2 = [targets[i] for i in range(len(groups)) if groups[i]==2]
# create ES1 dataset
es1 = create_dataset(seq1, targets1)
print('ES1: %s' % str(es1.shape))
savetxt('es1.csv', es1, delimiter=',')
# create ES2 dataset
es2_train = create_dataset(seq1, targets1)
es2_test = create_dataset(seq2, targets2)
print('ES2 Train: %s' % str(es2_train.shape))
print('ES2 Test: %s' % str(es2_test.shape))
savetxt('es2_train.csv', es2_train, delimiter=',')
savetxt('es2_test.csv', es2_test, delimiter=',')