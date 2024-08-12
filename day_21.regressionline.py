# y = 2x + 3 그래프 그리기
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.linear_model import LinearRegression
#x값의 범위 설정
x = np.linspace(0, 100, 400)

#y값 계산
y = 2*x + 3

#np.random.seed(20240805)
obs_x = np.random.choice(np.arange(100), 100)
epsilon_i = norm.rvs(loc=0,scale=100,size = 100)
obs_y = 2 * obs_x + 3 + epsilon_i

#그래프 그리기
plt.plot(x, y, label = 'y = 2x + 3',color = 'black')
plt.scatter(obs_x, obs_y, color = 'blue', s=3)
#plt.show()
#plt.clf()
#df = pd.DataFrame({"x": obs_x,
#                    "y": obs_y})
#                    
#df

#선형회귀 모델 생성
model = LinearRegression()

#모델 학습
obs_x = obs_x.reshape(-1, 1)
model.fit(obs_x, obs_y)

#회귀 직선의 기울기와 절편
model.coef_[0]
model.intercept_

#회귀 직선 그리기
x = np.linspace(0, 100, 400)
y = model.coef_[0] * x + model.intercept_
plt.xlim([0, 100])
plt.ylim([0, 300])
plt.plot(x, y, color = "red") #회귀직선
plt.show()
plt.clf()


#model
#summary(model)

import statsmodels.api as sm
#!pip install statsmodels
obs_x = sm.add_constant(obs_x)
model = sm.OLS(obs_y, obs_x).fit()
print(model.summary())

