import pandas as pd
import numpy as np

# 변수 1. ExterQual
# ExterQual: Evaluates the quality of the material on the exterior 
#       
#        Ex   Excellent
#        Gd   Good
#        TA   Average/Typical
#        Fa   Fair
#        Po   Poor

house_train = pd.read_csv("data/house price/train.csv")
house_train.info()
house_train = house_train[["Id", "ExterQual", "SalePrice"]]
house_train.info()

# ExterQual의 고윳값 확인
house_train["ExterQual"].value_counts()

# ExterQual 평균
E_house_mean = house_train.groupby("ExterQual", as_index=False)\
           .agg(mean_E = ("SalePrice", "mean"))
E_house_mean

# ExterQual 평균 시각화
import matplotlib.pyplot as plt
x = E_house_mean["ExterQual"]
y = E_house_mean['mean_E']
plt.plot(x, y)
plt.show()
plt.clf()

# ExterQual의 Ex, Gd, TA, Fa, Po를 값 변경 5, 4, 3, 2, 1
# 고윳값을 숫자로 변환할 매핑 딕셔너리 정의
quality_mapping = {
    'Ex': 5,
    'Gd': 4,
    'TA': 3,
    'Fa': 2
}

# ExterQual 열을 숫자로 변환
house_train["ExterQual"] = house_train["ExterQual"].replace(quality_mapping)

# ExterQual 평균 계산
E_house_mean = house_train.groupby("ExterQual", as_index=False)\
           .agg(mean_E = ("SalePrice", "mean"))

# ExterQual 평균 시각화
x = E_house_mean["ExterQual"]
y = E_house_mean['mean_E']

plt.plot(x, y, marker='o', linestyle='-')

plt.xlabel('ExterQual (Quality Rating)')
plt.ylabel('Mean SalePrice')
plt.title('Mean SalePrice by ExterQual')
plt.xticks(ticks=[2, 3, 4, 5]) # 정수만 표시되게 함
plt.show()
plt.clf()

# 상관계수 correlation을 구함
# correlation : np.float64(0.9819325684393003)
# 1 에 가까울 수록 상관관계가 높음
correlation = E_house_mean["ExterQual"].corr(E_house_mean["mean_E"])
correlation
# ---------------------------------------------------------------------


# 변수 2. Fireplaces: Number of fireplaces

house_train = pd.read_csv("data/house price/train.csv")
house_train.info()
house_train = house_train[["Id", "Fireplaces", "SalePrice"]]
house_train.info()

# Fireplaces의 고윳값 확인
house_train["Fireplaces"].value_counts()

# Fireplaces 평균
F_house_mean = house_train.groupby("Fireplaces", as_index=False)\
           .agg(mean_F = ("SalePrice", "mean"))
F_house_mean

# Fireplaces 평균 시각화
import matplotlib.pyplot as plt
x = F_house_mean["Fireplaces"]
y = F_house_mean['mean_F']
plt.plot(x,y)
plt.show()
plt.clf()

# 상관계수 correlation을 구함
# correlation : np.float64(0.937085010309497)
# 1 에 가까울 수록 상관관계가 높음
correlation = F_house_mean["Fireplaces"].corr(F_house_mean["mean_F"])
correlation
# ---------------------------------------------------------------------
# 변수 3. BsmtExposure
# BsmtExposure: Refers to walkout or garden level walls
#       
#       Gd	Good Exposure
#       Av	Average Exposure (split levels or foyers typically score average or above)	
#       Mn	Mimimum Exposure
#       No	No Exposure
#       NA	No Basementr

house_train = pd.read_csv("data/house price/train.csv")
house_train.info()
house_train = house_train[["Id", "BsmtExposure", "SalePrice"]]
house_train.info()

# BsmtExposure의 고윳값 확인
house_train["BsmtExposure"].value_counts()

# BsmtExposure 평균
B_house_mean = house_train.groupby("BsmtExposure", as_index=False)\
           .agg(mean_B = ("SalePrice", "mean"))
B_house_mean

# BsmtExposure 평균 시각화
import matplotlib.pyplot as plt
x = B_house_mean["BsmtExposure"]
y = B_house_mean['mean_B']
plt.plot(x, y)
plt.show()
plt.clf()

# BsmtExposure의 Ex, Gd, TA, Fa, Po를 값 변경 5, 4, 3, 2, 1
# 고윳값을 숫자로 변환할 매핑 딕셔너리 정의
quality_mapping = {
    'Gd': 5,
    'Av': 4,
    'Mn': 3,
    'No': 2,
    'Na': 1
}

# BsmtExposure 열을 숫자로 변환
house_train["BsmtExposure"] = house_train["BsmtExposure"].replace(quality_mapping)

# BsmtExposure 평균 계산
E_house_mean = house_train.groupby("BsmtExposure", as_index=False)\
           .agg(mean_B = ("SalePrice", "mean"))

# BsmtExposure 평균 시각화
x = B_house_mean["BsmtExposure"]
y = B_house_mean['mean_B']

plt.plot(x, y, marker='o', linestyle='-')

plt.xlabel('BsmtExposure (Quality Rating)')
plt.ylabel('Mean SalePrice')
plt.title('Mean SalePrice by BsmtExposure')
plt.xticks(ticks=[2, 3, 4, 5]) # 정수만 표시되게 함
plt.show()
plt.clf()

# 상관계수 correlation을 구함
# correlation : np.float64(0.9693234927093594)
# 1 에 가까울 수록 상관관계가 높음
correlation = E_house_mean["BsmtExposure"].corr(E_house_mean["mean_B"])
correlation
