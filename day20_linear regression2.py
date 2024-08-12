# 변수 2개 사용하기 (숫자 변수만)
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

house_test = pd.read_csv('data/houseprice/test.csv')
house_train = pd.read_csv('data/houseprice/train.csv')
sub_df = pd.read_csv('data/houseprice/sample_submission.csv')

## 이상치 탐색
house_train=house_train.query("GrLivArea <= 4500")

## 회귀분석 적합(fit)하기
# house_train["GrLivArea"]   # 판다스 시리즈
# house_train[["GrLivArea"]] # 판다스 프레임
x = house_train[["GrLivArea", "GarageArea"]]
y = house_train["SalePrice"]



# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y)  # 자동으로 기울기, 절편 값을 구해줌

# 회귀 직선의 기울기와 절편

model.coef_      # 기울기 a
model.intercept_ # 절편 b

# def my_houseprice(x, y):
#     return model.coef_[0]*x + model.coef_[1]*y + model.intercept_
# 
# my_houseprice(300, 55)

my_houseprice(house_test["GrLivArea"], house_test["GarageArea"])

test_x = house_test[["GrLivArea", "GarageArea"]]
test_x

# 결측치 확인
test_x["GrLivArea"].isna().sum()
test_x["GarageArea"].isna().sum()
test_x=test_x.fillna(house_test["GarageArea"].mean())

pred_y=model.predict(test_x) # test 셋에 대한 집값
pred_y

# SalePrice 바꿔치기
sub_df["SalePrice"] = pred_y
sub_df

# csv 파일로 내보내기
sub_df.to_csv("./data/houseprice/sample_submission10.csv", index=False)
