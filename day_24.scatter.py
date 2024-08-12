
#p.128산점도
import plotly.express as px
#!pip install palmerpenguins
import pandas as pd
import numpy as np
from palmerpenguins import load_penguins
import seaborn as sns

penguins = load_penguins()
penguins.head()
penguins.columns


#fig = px.scatter(penguins, x = 'bill_length_mm', y = 'bill_depth_mm', color = "species", trendline = "ols")
fig = px.scatter(penguins, x = 'bill_length_mm', y = 'bill_depth_mm', color = "species")

fig.update_layout(
    title=dict(text="팔머펭귄 종별 부리 길이 vs. 깊이", font=dict(color="white", size=24)),
    paper_bgcolor="black",
    plot_bgcolor="black",
    font=dict(color="white"),
    xaxis=dict(
        title=dict(text="부리 길이 (mm)", font=dict(color="white", size=18)), 
        tickfont=dict(color="white", size=14),
        gridcolor='rgba(255, 255, 255, 0.2)'  # 그리드 색깔 조정
    ),
    yaxis=dict(
        title=dict(text="부리 깊이 (mm)", font=dict(color="white", size=18)), 
        tickfont=dict(color="white", size=14),
        gridcolor='rgba(255, 255, 255, 0.2)'  # 그리드 색깔 조정
    ),
    legend=dict(title=dict(text="펭귄종", font=dict(color="white", size=18)), font=dict(color="white"))
)

# 점 크기 및 투명도 설정
fig.update_traces(marker=dict(size=10, opacity = 0.7))

fig.show()


#=====================

#132 추세선 그리기
from sklearn.linear_model import LinearRegression
model = LinearRegression()
penguins = penguins.dropna()
x = penguins[["bill_length_mm"]]
y = penguins['bill_depth_mm']

model.fit(x,y)
linear_fit = model.predict(x)

#p.134
fig.add_trace(
    go.Scatter(
        mode = "lines",
        x = penguins['bill_length_mm'], y = linear_fit,
        name = "선형회귀직선",
        line = dict(dash="dot",color = "white")
    )
)
fig.show()


#====================================

# 범주형 변수로 회귀분석 진행하기
# 범주형 변수인 'species'를 더미 변수로 변환
penguins = penguins.dropna()
penguins_dummies = pd.get_dummies(penguins, 
                                  columns=['species'],
                                  drop_first=True)
#drop_first = True : "species_Chinstrap", "species_Gentoo"
#drop_first = False : "species_Adelie","species_Chinstrap", "species_Gentoo"

penguins_dummies.columns
penguins_dummies.iloc[:,-3:]
# x와 y 설정
x = penguins_dummies[["bill_length_mm", "species_Chinstrap", "species_Gentoo"]]
y = penguins_dummies["bill_depth_mm"]

# 모델 학습
model = LinearRegression()
model.fit(x, y)

model.coef_
model.intercept_

# y = 0.2 * bill_length -1.93 * species_Chinstrap -5.1 * species_Gentoo + 10.56
# penguins
# species    island  bill_length_mm  ...  body_mass_g     sex  year
# Adelie     Torgersen            39.5  ...       3800.0  female  2007
# Chinstrap  Torgersen            40.5  ...       3800.0  female  2007
# Gentoo     Torgersen            40.5  ...       3800.0  female  2007
# x1, x2, x3
# 39.5, 0, 0
# 40.5, 1, 0
# y = 0.2 * bill_length -1.93 * species_Chinstrap -5.1 * species_Gentoo + 10.56
#Adel y hat
#0.2*39.5 + (-1.93)*0 + (-5.1)*0 +10.56
#Chinstrap y hat
#0.2 * 40.5 -1.93 * True -5.1* False + 10.56


regline_y = model.predict(x)

sns.scatterplot(x = x['bill_length_mm'], y = y, hue = penguins['species'], palette = 'deep', legend = False)
sns.scatterplot(x = x['bill_length_mm'], y = model.predict(x), color = 'black')
plt.show()
plt.clf()



#=========================================
# 원하는 변수를 사용해서 회귀모델을 만들고, 제출할것!
# 원하는 변수 2개
# 회귀모델을 통한 집값 예측

# 필요한 패키지 불러오기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

## 필요한 데이터 불러오기
house_train=pd.read_csv("./data/houseprice/train.csv")
house_test=pd.read_csv("./data/houseprice/test.csv")
sub_df=pd.read_csv("./data/houseprice/sample_submission.csv")

## 이상치 탐색
house_train=house_train.query("GrLivArea <= 4500")

## 회귀분석 적합(fit)하기
# house_train["GrLivArea"]   # 판다스 시리즈
# house_train[["GrLivArea"]] # 판다스 프레임
house_train["Neighborhood"]
neighborhood_dummies = pd.get_dummies(
    house_train["Neighborhood"],
    drop_first=True
    )
# pd.concat([df_a, df_b], axis=1)
x= pd.concat([house_train[["GrLivArea", "GarageArea"]], 
             neighborhood_dummies], axis=1)
y = house_train["SalePrice"]

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y)  # 자동으로 기울기, 절편 값을 구해줌

# 회귀 직선의 기울기와 절편
model.coef_      # 기울기 a
model.intercept_ # 절편 b

neighborhood_dummies_test = pd.get_dummies(
    house_test["Neighborhood"],
    drop_first=True
    )
test_x = pd.concat([house_test[["GrLivArea", "GarageArea"]],
                    neighborhood_dummies_test], axis = 1)
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
sub_df.to_csv("./data/houseprice/sample_submission12.csv", index=False)
