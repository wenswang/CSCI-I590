import numpy as np
import scipy as sp
import pandas as pd
import sklearn
from matplotlib import pyplot as plt
import sklearn.cross_validation
from sklearn.ensemble import RandomForestClassifier

dfr = pd.read_csv('/Users/wensiwang/Desktop/I590/HW/Project/winequality-red.csv', sep=';')

y = dfr['quality'].values
x = dfr.drop('quality',1)
y = np.array([1 if i >=7 else 0 for i in y])
x = x.as_matrix()

clf = RandomForestClassifier(n_estimators=60)
#clf = RandomForestClassifier(n_estimators=120)
clf.fit(x,y)
importance_list = clf.feature_importances_
name_list = dfr.columns
importance_list, name_list = zip(*sorted(zip(importance_list, name_list)))
plt.barh(range(len(name_list)),importance_list,align='center')
plt.yticks(range(len(name_list)),name_list)
plt.xlabel('Relative Importance')
plt.ylabel('Features')
plt.title('Relative importance of Red Wine')
plt.show()