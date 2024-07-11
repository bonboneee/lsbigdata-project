#교재 63페이지
#!pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt

var = ['a', 'a', 'b', 'c']
var

sns.countplot(x=var)
plt.show()
plt.clf()

df = sns.load_dataset("titanic")
sns.countplot(data = df, x = "sex", hue = "sex")
sns.countplot(data = df, x = "sex", hue = "sex", orient = "v") #hue는 항목별 색을 다르게 함
plt.show()

?sns.countplot #앞에 물음표 붙이면 설명 나옴옴
sns.countplot(data = df, x = "class")
sns.countplot(data = df, x = "class", hue = "alive")
sns.countplot(data = df,
              X = "survived",
              y = "pclass")
plt.show()



!pip install scikit-learn

import sklearn.metrics
#sklearn.metrics.accuracy_score()

from sklearn import metrics
#metrics.accuracy_score()

import sklearn.metrics as met
#met.accuracy_score()

