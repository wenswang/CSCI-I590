import numpy as np
import scipy as sp
import pandas as pd

df = pd.read_csv('winequality-white.csv', sep=';')
df.head()

y = df['quality'].values
x = df.drop('quality',1)
y = np.array([1 if i >=7 else 0 for i in y])
x = x.as_matrix()

#normalize metrics
colmean = x.mean(axis=0)
sd = x.std(axis=0)
xNorm = (x-colmean)/sd

#in case I don't have scikit-learn package on computer,run following on terminal
# pip install -U scikit-learn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score

scores = []
for num in range(1,50):
    clf = KNeighborsClassifier(n_neighbors=num)
    score_list = cross_val_score(clf,xNorm,y,cv=10)
    scores.append(score_list)

#calculate percentage of bad wine
blind_guess = float(sum(1-y))/len(y)

boxplot(scores)
plt.axhline(y=blind_guess,ls='--')
plt.xlabel('Number of neighbors')
plt.ylabel('Classification score')
plt.title('Classification score~number of neighbors')
plt.show()

scores2 = []
for num in range(1,50):
    clf = KNeighborsClassifier(n_neighbors=num)
    score_list = cross_val_score(clf,xNorm,y,cv=10,scoring='f1')
    scores2.append(score_list)

boxplot(scores2)
plt.axhline(y=blind_guess,ls='--')
plt.xlabel('Number of neighbors')
plt.ylabel('F1 score')
plt.title('Classification score~number of neighbors')
plt.show()

