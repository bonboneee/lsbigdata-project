# 변수 2개 사용하기 (숫자 변수만)
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

house_test = pd.read_csv('data/houseprice/test.csv')
house_train = pd.read_csv('data/houseprice/train.csv')
sub_df = pd.read_csv('data/houseprice/sample_submission.csv')

## 이상치 탐색
# house_train=house_train.query("GrLivArea <= 4500")


## 회귀분석 적합(fit)하기
# house_train["GrLivArea"]   # 판다스 시리즈
# house_train[["GrLivArea"]] # 판다스 프레임
# 숫자형 변수만 선택하기
x = house_train.select_dtypes(include=[int, float])
# 필요없는 칼럼 제거하기
x = x.iloc[:,1:-1]
y = house_train["SalePrice"]


# 변수별로 결측값 채우기
fill_values = {
    'LotFrontage': x["LotFrontage"].mean(),
    'MasVnrArea': x["MasVnrArea"].mean(),
    'GarageYrBlt': x["GarageYrBlt"].mean()
}
x = x.fillna(value=fill_values)
x.isna().sum()
x.mean()

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y)  # 자동으로 기울기, 절편 값을 구해줌

# 회귀 직선의 기울기와 절편
model.coef_      # 기울기 a
model.intercept_ # 절편 b

# 테스트 데이터 예측
test_x = house_test.select_dtypes(include=[int, float])
test_x = test_x.iloc[:,1:] #id값만 제거 

# fill_values = {
#     'LotFrontage': test_x["LotFrontage"].mean(),
#     'MasVnrArea': test_x["MasVnrArea"].mode()[0],
#     'GarageYrBlt': test_x["GarageYrBlt"].mode()[0]
# }
# test_x = test_x.fillna(value=fill_values)
test_x=test_x.fillna(test_x.mean())


# 결측치 확인
test_x.isna().sum()
test_x.mean()
# 테스트 데이터 집값 예측
pred_y=model.predict(test_x) # test 셋에 대한 집값
pred_y

# SalePrice 바꿔치기
sub_df["SalePrice"] = pred_y
sub_df

# csv 파일로 내보내기
sub_df.to_csv("./data/houseprice/sample_submission11.csv", index=False)
#--------------------------------------dakyung
house_train = df.copy()
house_test = df_test.copy()
sub = sub_df.copy()

## 이상치 탐색


## 회귀분석 적합(fit)하기
x = house_train.select_dtypes(include = [int, float]) # 숫자형 변수만 선택
x = x.iloc[:, 1:-1] # 필요없는 열 제거(Id, SalePrice)
x.isna().sum()

x['LotFrontage'] = x['LotFrontage'].fillna(x['LotFrontage'].mean())
x['MasVnrArea'] = x['MasVnrArea'].fillna(x['MasVnrArea'].mean()) 
x['GarageYrBlt'] = x['GarageYrBlt'].fillna(x['GarageYrBlt'].mean())

y = house_train['SalePrice']

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y) # 자동으로 기울기, 절편 값을 구해줌

# 회귀 직선의 기울기와 절편
model.coef_ # 기울기(a)
model.intercept_ # 절편(b)

slope = model.coef_
intercept = model.intercept_
print(f"기울기 (slope: a): {slope}")
print(f"절편 (intercep: b): {intercept}")

test_x = house_test.select_dtypes(include = [int, float])
test_x = test_x.iloc[:, 1:]

# 결측치 확인
test_x.isna().sum()

# 결측치 채우기 노가다
# test_x['LotFrontage'] = test_x['LotFrontage'].fillna(test_x['LotFrontage'].mean())
# test_x['MasVnrArea'] = test_x['MasVnrArea'].fillna(test_x['MasVnrArea'].mean())
# test_x['GarageYrBlt'] = test_x['GarageYrBlt'].fillna(test_x['GarageYrBlt'].mean())
# test_x['BsmtFinSF1'] = test_x['BsmtFinSF1'].fillna(test_x['BsmtFinSF1'].mean())
# test_x['BsmtFinSF2'] = test_x['BsmtFinSF2'].fillna(test_x['BsmtFinSF2'].mean())
# test_x['BsmtUnfSF'] = test_x['BsmtUnfSF'].fillna(test_x['BsmtUnfSF'].mean())
# test_x['TotalBsmtSF'] = test_x['TotalBsmtSF'].fillna(test_x['TotalBsmtSF'].mean())
# test_x['BsmtFullBath'] = test_x['BsmtFullBath'].fillna(test_x['BsmtFullBath'].mean())
# test_x['BsmtHalfBath'] = test_x['BsmtHalfBath'].fillna(test_x['BsmtHalfBath'].mean())
# test_x['GarageCars'] = test_x['GarageCars'].fillna(test_x['GarageCars'].mean())
# test_x['GarageArea'] = test_x['GarageArea'].fillna(test_x['GarageArea'].mean())

# 결측치 채우기 반복문
## 결측치를 채워야 하는 컬럼 리스트
columns_to_fill = [
    'LotFrontage', 'MasVnrArea', 'GarageYrBlt', 
    'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 
    'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath', 
    'GarageCars', 'GarageArea']

## 각 컬럼의 결측치를 평균으로 채우기
for i in columns_to_fill:
    test_x[i] = test_x[i].fillna(test_x[i].mean())

# 걍 이렇게 하면 된대...
# test_x = test_x.fillna(test_x.mean())

# prediction
y_pred = model.predict(test_x)

# SalePrice 바꿔치기
sub["SalePrice"] = y_pred
sub

# csv 내보내기
sub.to_csv("data/kaggle/houseprice/sample_submission11.csv", index = False)


