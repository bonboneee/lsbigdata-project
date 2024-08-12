# 문제1. y = 2x +3의 그래프를 그려보세요.
import numpy as np
import matplotlib.pyplot as plt
a= 2
b = 3
x = np.linspace(-5, 5, 100)
y = a*x +b
plt.plot(x,y, color="blue")

#축설정
plt.axvline(0, color = "black")
plt.axhline(0, color = "black")

plt.show()
plt.clf()


#y = -2x 그래프
import numpy as np
import matplotlib.pyplot as plt
a= -2
b = 0
x = np.linspace(-5, 5, 100)
y = a*x +b
plt.plot(x,y, color="blue")

#축설정
plt.axvline(0, color = "black")
plt.axhline(0, color = "black")

plt.show()
plt.clf()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a= 80
b = 5
x = np.linspace(0, 5, 100)
y = a*x +b

house_train = pd.read_csv("data/house price/train.csv")
my_df = house_train[["BedroomAbvGr", "SalePrice"]].head(10)
my_df["SalePrice"] = my_df["SalePrice"] / 1000
plt.scatter(x = my_df["BedroomAbvGr"], y = my_df["SalePrice"])
plt.plot(x,y, color="black")
plt.show()
plt.clf()

# --------------------------------------------------
#회귀 팀플 시작!
import pandas as pd

a = 24
b = 109

x = np.linspace(0, 5, 100)
y = a * x + b 

house_train = pd.read_csv('./data/houseprice/train.csv')
house_train.info()
my_df = house_train[["BedroomAbvGr", "SalePrice"]].head(1000)
my_df["SalePrice"] = my_df["SalePrice"] / 1000
plt.scatter(x=my_df["BedroomAbvGr"], y=my_df["SalePrice"])

mean_bed_room = my_df.groupby("BedroomAbvGr",  as_index=False)\
                    .agg(mean_bedroom = ("SalePrice", "mean"))
mean_bed_room

my_df["BedroomAbvGr"].value_counts()

plt.plot(x, y, color = 'blue')
plt.xlim(0,6)
plt.show()
plt.clf()
# --------------------------------------------------

## test 데이터 불러오기
#house_test = pd.read_csv('./data/houseprice/test.csv')
#house_test = house_test[["Id", "BedroomAbvGr"]]
#house_test
#
#a = 36
#b = 68
#x = house_test["BedroomAbvGr"]
#y = a * x + b 
#
#house_test["SalePrice"] = y * 1000
#house_test
#
## sub 데이터 불러오기
#sub_df = pd.read_csv('./data/houseprice/sample_submission.csv')
#sub_df
#
## SalePrice 바꿔치기
#sub_df['SalePrice'] = house_test['SalePrice']
#sub_df
#
#sub_df.to_csv('./data/houseprice/sample_submission7.csv', index=False)
#
#
##--------------------------
#선생님 버전
#house_test=pd.read_csv("./data/houseprice/test.csv")
#a = 70; b=10
#(a * house_test["BedroomAbvGr"] + b) * 1000
#
##sub 데이터 불러오기
#sub_df = pd.read_csv("./data/houseprice/test.csv")
#sub_df
#
##SalePrice 바꿔치기
#sub_df["SalePrice"] = (a * house_test["BedroomAbvGr"] + b) *1000
#sub_df
#
#sub_df.to_csv('./data/houseprice/sample_submission7.csv', index=False)

#--------------------------------------------------------------
#직선 성능 평가
a = 36
b = 68

# y_hat 어떻게 구할까?
y_hat = (a * house_train["BedroomAbvGr"] + b) * 1000

#y는 어디있는가?
y = house_train["SalePrice"]

np.abs(y - y_hat)  # 절대거리
np.sum(np.abs(y - y_hat)) # 절대값 합
#np.sum((y - y_hat)**2) # 제곱합

#우리조 거리측정: 거리가 짧을 수록 직선의 성능이 좋다.
#np.int64(81472836)

#--------------------------------------------------------
#!pip install scikit-learn
#선형회귀 예시
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 예시 데이터 (x와 y 벡터)
x = np.array([1, 3, 2, 1, 5]).reshape(-1, 1)  # x 벡터 (특성 벡터는 2차원 배열이어야 합니다)
y = np.array([1, 2, 3, 4, 5])  # y 벡터 (레이블 벡터는 1차원 배열입니다)

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y) #fit함수가 자동으로 기울기, 절편 값을 구해줌.

# 회귀 직선의 기울기와 절편
model.coef_         #기울기 a
model.intercept_    #절편 b


slope = model.coef_[0]
intercept = model.intercept_
print(f"기울기 (slope): {slope}")
print(f"절편 (intercept): {intercept}")

# 예측값 계산, x는 방 개수
y_pred = model.predict(x)

# 데이터와 회귀 직선 시각화
plt.scatter(x, y, color='blue', label='data')
plt.plot(x, y_pred, color='red', label='regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.clf()


#-------------------------------------------------------
#train에 있는 x(방갯수)들고 와서 집값 예측해보기(성능1. 절대값 기준으로)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array(house_train["BedroomAbvGr"]).reshape(-1,1)
y = np.array(house_train["SalePrice"])

# house_train["BedroomAbvGr"].count()
# house_train["SalePrice"].count()

model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

# len(y_pred)

plt.scatter(x, y, color='blue', label='BedroomAbvGr')
plt.plot(x, y_pred, color='red', label='SalePrice')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.clf()
np.sum(np.abs(y - y_hat)) # 절대값 합 : np.int64(81472836)
#--------------------------------------------------------
#선생님 버전_ 회귀모델을 통한 집값 예측
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#필요한 데이터 불러오기
house_test = pd.read_csv('data/houseprice/test.csv')
house_train = pd.read_csv('data/houseprice/train.csv')
sub_df = pd.read_csv('data/houseprice/sample_submission.csv')

# 회귀분석 적합(FIT)하기 
x = np.array(house_train["BedroomAbvGr"]).reshape(-1, 1)
y = np.array(house_train["SalePrice"]) / 1000 

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y) #fit함수가 자동으로 기울기, 절편 값을 구해줌.

# 회귀 직선의 기울기와 절편
model.coef_         #기울기 a
model.intercept_    #절편 b


slope = model.coef_[0]
intercept = model.intercept_
print(f"기울기 (slope): {slope}")
print(f"절편 (intercept): {intercept}")

# 예측값 계산, x는 방 개수
y_pred = model.predict(x)

# 데이터와 회귀 직선 시각화
plt.scatter(x, y, color='blue', label='data')
plt.plot(x, y_pred, color='red', label='regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.clf()
np.sum((y - y_hat)**2)
#----------------------------------------------------------
# ====================
# =====   옵션   =====
# ====================

import numpy as np
from scipy.optimize import minimize

# 최소값을 찾을 다변수 함수 정의
def my_f(x):
    return (x[0] - 1) ** 2 + (x[1] - 2) ** 2

# 초기 추정값
initial_guess = [0, 0]

# 최소값 찾기
result = minimize(my_f, initial_guess)

# 결과 출력
print("최소값:", result.fun)
print("최소값을 갖는 x 값:", result.x)


# 회귀직선 구하기

import numpy as np
from scipy.optimize import minimize

def line_perform(par):
    y_hat=(par[0] * house_train["BedroomAbvGr"] + par[1]) * 1000
    y=house_train["SalePrice"]
    return np.sum(np.abs((y-y_hat)))

line_perform([36, 68])

# 초기 추정값
initial_guess = [0, 0]

# 최소값 찾기
result = minimize(line_perform, initial_guess)

# 결과 출력
print("최소값:", result.fun)
print("최소값을 갖는 x 값:", result.x)

#-----------------------------------minimize 설명
import numpy as np
from scipy.optimize import minimize

#y = x^2 + 3
#최소값: (0, 3)

def my_f(x):
    return x**2 + 3
my_f(3)    

# 초기 추정값
initial_guess = [0]

# 최소값 찾기
result = minimize(my_f, initial_guess)

# 결과 출력
print("최소값:", result.fun)
print("최소값을 갖는 x 값:", result.x)


#----------------------------z = x^2 +  y^2  +3 그래프
def my_f2(x):
    return x[0]**2 + x[1]**2 +3
my_f2([1, 3])

# 초기 추정값
initial_guess = [-10,3]

# 최소값 찾기
result = minimize(my_f2, initial_guess)

# 결과 출력
print("최소값:", result.fun)
print("최소값을 갖는 x 값:", result.x)

#---------------------------f(x, y, z) = (x-1)^2 + (y-2)^2 + (z-4)^2 +7
#최소값과 최솟값이 되는 자리

def my_f3(x):
    return (x[0]-1)**2 + (x[1]-2)**2 + (x[2]-4)**2 + 7
my_f3([1, 2, 3])

# 초기 추정값
initial_guess = [-10,3, 4]

# 최소값 찾기
result = minimize(my_f3, initial_guess)

# 결과 출력
print("최소값:", result.fun)
print("최소값을 갖는 x 값:", result.x)


#-------------------------


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#필요한 데이터 불러오기
house_test = pd.read_csv('data/houseprice/test.csv')
house_train = pd.read_csv('data/houseprice/train.csv')
sub_df = pd.read_csv('data/houseprice/sample_submission.csv')

# 회귀분석 적합(FIT)하기 
x = np.array(house_train["BedroomAbvGr"]).reshape(-1, 1)
y = np.array(house_train["SalePrice"]) / 1000 

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y) #fit함수가 자동으로 기울기, 절편 값을 구해줌.

# 회귀 직선의 기울기와 절편
model.coef_         #기울기 a
model.intercept_    #절편 b


slope = model.coef_[0]
intercept = model.intercept_
print(f"기울기 (slope): {slope}")
print(f"절편 (intercept): {intercept}")

# 예측값 계산, x는 방 개수
y_pred = model.predict(x)

# 데이터와 회귀 직선 시각화
plt.scatter(x, y, color='blue', label='data')
plt.plot(x, y_pred, color='red', label='regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.clf()

test_x = np.array(house_test["BedroomAbvGr"]).reshape(-1,1)
test_x


pred_y = model.predict(test_x) #test셋에 대한 집값
pred_y



#SalePrice 바꿔치기
sub_df["SalePrice"] = pred_y*1000
sub_df

#csv로 바꿔치기
sub_df.to_csv("data/houseprice/sample_submission4.csv", index = False)


#------------------------------


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#필요한 데이터 불러오기
house_test = pd.read_csv('data/houseprice/test.csv')
house_train = pd.read_csv('data/houseprice/train.csv')
sub_df = pd.read_csv('data/houseprice/sample_submission.csv')

# 회귀분석 적합(FIT)하기 
x = np.array(house_train["BedroomAbvGr"]).reshape(-1, 1)
y = np.array(house_train["SalePrice"]) / 1000 

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y) #fit함수가 자동으로 기울기, 절편 값을 구해줌.

# 회귀 직선의 기울기와 절편
model.coef_         #기울기 a
model.intercept_    #절편 b


slope = model.coef_[0]
intercept = model.intercept_
print(f"기울기 (slope): {slope}")
print(f"절편 (intercept): {intercept}")

# 예측값 계산, x는 방 개수
y_pred = model.predict(x)

# 데이터와 회귀 직선 시각화
plt.scatter(x, y, color='blue', label='data')
plt.plot(x, y_pred, color='red', label='regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.clf()

test_x = np.array(house_test["BedroomAbvGr"]).reshape(-1,1)
test_x


pred_y = model.predict(test_x) #test셋에 대한 집값
pred_y



#SalePrice 바꿔치기
sub_df["SalePrice"] = pred_y*1000
sub_df

#csv로 바꿔치기
sub_df.to_csv("data/houseprice/sample_submission4.csv", index = False)
#------------------------------------------
#FullBath를 이용해서 집값 예측하기: 0.34919 점
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#필요한 데이터 불러오기
house_test = pd.read_csv('data/houseprice/test.csv')
house_train = pd.read_csv('data/houseprice/train.csv')
sub_df = pd.read_csv('data/houseprice/sample_submission.csv')

# 회귀분석 적합(FIT)하기 
x = np.array(house_train["FullBath"]).reshape(-1, 1)
y = np.array(house_train["SalePrice"]) / 1000 

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y) #fit함수가 자동으로 기울기, 절편 값을 구해줌.

# 회귀 직선의 기울기와 절편
model.coef_         #기울기 a
model.intercept_    #절편 b


slope = model.coef_[0]
intercept = model.intercept_
print(f"기울기 (slope): {slope}")
print(f"절편 (intercept): {intercept}")

# 예측값 계산, x는 방 개수
y_pred = model.predict(x)

# 데이터와 회귀 직선 시각화
plt.scatter(x, y, color='blue', label='data')
plt.plot(x, y_pred, color='red', label='regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.clf()

test_x = np.array(house_test["FullBath"]).reshape(-1,1)
test_x


pred_y = model.predict(test_x) #test셋에 대한 집값
pred_y



#SalePrice 바꿔치기
sub_df["SalePrice"] = pred_y*1000
sub_df

#csv로 바꿔치기
sub_df.to_csv("data/houseprice/sample_submission5.csv", index = False)

#------------------------------------
#BedroomAbvGr를 이용해서 집값 예측하기: 0.41949 점
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#필요한 데이터 불러오기
house_test = pd.read_csv('data/houseprice/test.csv')
house_train = pd.read_csv('data/houseprice/train.csv')
sub_df = pd.read_csv('data/houseprice/sample_submission.csv')

# 회귀분석 적합(FIT)하기 
x = np.array(house_train["BedroomAbvGr"]).reshape(-1, 1)
y = np.array(house_train["SalePrice"]) / 1000 

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y) #fit함수가 자동으로 기울기, 절편 값을 구해줌.

# 회귀 직선의 기울기와 절편
model.coef_         #기울기 a
model.intercept_    #절편 b


slope = model.coef_[0]
intercept = model.intercept_
print(f"기울기 (slope): {slope}")
print(f"절편 (intercept): {intercept}")

# 예측값 계산, x는 방 개수
y_pred = model.predict(x)

# 데이터와 회귀 직선 시각화
plt.scatter(x, y, color='blue', label='data')
plt.plot(x, y_pred, color='red', label='regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.clf()

test_x = np.array(house_test["BedroomAbvGr"]).reshape(-1,1)
test_x


pred_y = model.predict(test_x) #test셋에 대한 집값
pred_y



#SalePrice 바꿔치기
sub_df["SalePrice"] = pred_y*1000
sub_df

#csv로 바꿔치기
sub_df.to_csv("data/houseprice/sample_submission6.csv", index = False)
#------------------------------------
#1stFlrSF를 이용해서 집값 예측하기: 0.33063 점
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#필요한 데이터 불러오기
house_test = pd.read_csv('data/houseprice/test.csv')
house_train = pd.read_csv('data/houseprice/train.csv')
sub_df = pd.read_csv('data/houseprice/sample_submission.csv')

# 회귀분석 적합(FIT)하기 
x = np.array(house_train["1stFlrSF"]).reshape(-1, 1)
y = np.array(house_train["SalePrice"]) / 1000 

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y) #fit함수가 자동으로 기울기, 절편 값을 구해줌.

# 회귀 직선의 기울기와 절편
model.coef_         #기울기 a
model.intercept_    #절편 b


slope = model.coef_[0]
intercept = model.intercept_
print(f"기울기 (slope): {slope}")
print(f"절편 (intercept): {intercept}")

# 예측값 계산, x는 방 개수
y_pred = model.predict(x)

# 데이터와 회귀 직선 시각화
plt.scatter(x, y, color='blue', label='data')
plt.plot(x, y_pred, color='red', label='regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.clf()

test_x = np.array(house_test["1stFlrSF"]).reshape(-1,1)
test_x


pred_y = model.predict(test_x) #test셋에 대한 집값
pred_y



#SalePrice 바꿔치기
sub_df["SalePrice"] = pred_y*1000
sub_df

#csv로 바꿔치기
sub_df.to_csv("data/houseprice/sample_submission7.csv", index = False)
#---------------------------------
#GrLivArea를 이용해서 집값 예측하기: 0.29117 점
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#필요한 데이터 불러오기
house_test = pd.read_csv('data/houseprice/test.csv')
house_train = pd.read_csv('data/houseprice/train.csv')
sub_df = pd.read_csv('data/houseprice/sample_submission.csv')

# 회귀분석 적합(FIT)하기 
x = np.array(house_train["GrLivArea"]).reshape(-1, 1)
y = np.array(house_train["SalePrice"]) / 1000 

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y) #fit함수가 자동으로 기울기, 절편 값을 구해줌.

# 회귀 직선의 기울기와 절편
model.coef_         #기울기 a
model.intercept_    #절편 b


slope = model.coef_[0]
intercept = model.intercept_
print(f"기울기 (slope): {slope}")
print(f"절편 (intercept): {intercept}")

# 예측값 계산, x는 방 개수
y_pred = model.predict(x)

# 데이터와 회귀 직선 시각화
plt.scatter(x, y, color='blue', label='data')
plt.plot(x, y_pred, color='red', label='regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.clf()


test_x = np.array(house_test["GrLivArea"]).reshape(-1,1)
test_x


pred_y = model.predict(test_x) #test셋에 대한 집값
pred_y



#SalePrice 바꿔치기
sub_df["SalePrice"] = pred_y*1000
sub_df

#csv로 바꿔치기
sub_df.to_csv("data/houseprice/sample_submission8.csv", index = False)
#------------------------------
#GrLivArea에서 이상치 제거하고 예측 회귀 돌려보기 

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#필요한 데이터 불러오기
house_test = pd.read_csv('data/houseprice/test.csv')
house_train = pd.read_csv('data/houseprice/train.csv')
sub_df = pd.read_csv('data/houseprice/sample_submission.csv')

#이상치 탐색 및 제거 
house_train.query("GrLivArea > 4500") #탐색
house_train = house_train.query("GrLivArea <= 4500") #4500보다 작거나 같은 것만 할당해줌


# 회귀분석 적합(FIT)하기 
x = np.array(house_train["GrLivArea"]).reshape(-1, 1)
y = np.array(house_train["SalePrice"])

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y) #fit함수가 자동으로 기울기, 절편 값을 구해줌.

# 회귀 직선의 기울기와 절편
model.coef_         #기울기 a
model.intercept_    #절편 b


slope = model.coef_[0]
intercept = model.intercept_
print(f"기울기 (slope): {slope}")
print(f"절편 (intercept): {intercept}")

# 예측값 계산, x는 방 개수
y_pred = model.predict(x)

# 데이터와 회귀 직선 시각화
plt.scatter(x, y, color='blue', label='data')
plt.plot(x, y_pred, color='red', label='regression')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([0, 5000])
plt.ylim([0, 900000])
plt.legend()
plt.show()
plt.clf()


test_x = np.array(house_test["GrLivArea"]).reshape(-1,1)
test_x


pred_y = model.predict(test_x) #test셋에 대한 집값
pred_y



#SalePrice 바꿔치기
sub_df["SalePrice"] = pred_y*1000
sub_df

#csv로 바꿔치기
sub_df.to_csv("data/houseprice/sample_submission9.csv", index = False)
#------------------------------
