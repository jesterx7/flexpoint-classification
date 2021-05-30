# spot check for ES1
from numpy import mean
from numpy import std
from pandas import read_csv
from matplotlib import pyplot
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import joblib
# load dataset
dataset = read_csv('es1.csv', header=None)
# split into inputs and outputs
values = dataset.values
X, y = values[:, :-1], values[:, -1]
# create a list of models to evaluate
models, names = list(), list()
# logistic
models.append(LogisticRegression())
names.append('LR')
# knn
models.append(KNeighborsClassifier())
names.append('KNN')
# cart
models.append(DecisionTreeClassifier())
names.append('CART')
# svm
models.append(SVC())
names.append('SVM')
# random forest
models.append(RandomForestClassifier())
names.append('RF')
# gbm
models.append(GradientBoostingClassifier())
names.append('GBM')
# evaluate models
all_scores = list()

for i in range(len(models)):
	# create a pipeline for the model
	s = StandardScaler()
	p = Pipeline(steps=[('s',s), ('m',models[i])])
	p.fit(X, y)
	s.fit(X)
	joblib.dump(p, 'model_' + names[i] + '.pkl')
	joblib.dump(s, 'scaler_' + names[i] + '.pkl')
	scores = cross_val_score(p, X, y, scoring='accuracy', cv=2, n_jobs=-1)
	all_scores.append(scores)
	# summarize
	m, s = mean(scores)*100, std(scores)*100
	print('%s %.3f%% +/-%.3f' % (names[i], m, s))
# plot
pyplot.boxplot(all_scores, labels=names)
pyplot.show()