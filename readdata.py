import numpy as np
import scipy as sp
import pandas as pd
import sklearn
from matplotlib import pyplot as plt
import sklearn.cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('/Users/wensiwang/Desktop/I590/HW/Project/Code/winequality-white.csv', sep=';')
df.head()
print df.head()