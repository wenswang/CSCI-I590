import numpy as np
import scipy as sp
import pandas as pd
import sklearn
from matplotlib import pyplot as plt
import sklearn.cross_validation
from sklearn.ensemble import RandomForestClassifier


dfw = pd.read_csv('/Users/wensiwang/Desktop/I590/HW/Project/winequality-white.csv', sep=';')

y = dfw['quality'].values
x = dfw.drop('quality',1)
y = np.array([1 if i >=7 else 0 for i in y])
x = x.as_matrix()

clf = RandomForestClassifier(n_estimators=60)
#clf = RandomForestClassifier(n_estimators=120)
clf.fit(x,y)
importance_list = clf.feature_importances_
name_list = dfw.columns
importance_list, name_list = zip(*sorted(zip(importance_list, name_list)))
plt.barh(range(len(name_list)),importance_list,align='center')
plt.yticks(range(len(name_list)),name_list)
plt.xlabel('Relative Importance')
plt.ylabel('Features')
plt.title('Relative importance of White Wine')
plt.show()