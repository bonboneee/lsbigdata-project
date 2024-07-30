import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#y = 2x그래프 그리기
#점을 직선으로 이어서 표현
x = np.linspace(0, 8, 2)
y = 2*x
plt.scatter(x, y, s = 3)
plt.plot(x,y,color = "black")
plt.show()
plt.clf()


#y = x^2를 점 3개 사용해서 그리기
x = np.linspace(-8, 8, 100) #점을 많이 찍을 수록 완만해짐
y = x**2
plt.scatter(x, y, s = 3)
plt.plot(x,y,color = "black")

#x, y축 범위 설정
plt.xlim(-10, 10)
plt.ylim(0, 40)
plt.gca().set_aspect('equal', adjustable = 'box')

#x축과 y축의 비율 맞추기
#plt.axis('equal') 이건 xlim이랑 ylim이랑 같이 사용x

plt.show()
plt.clf()





#adp-statistics-book(p. 57) 문제 풀기N(3, 5^2)
#작년 남학생 3학년 전체 분포의 표준편차는 6kg 이었다고 합니다.
#이 정보를 이번 년도 남학생 분포의 표준편차로 대체하여 모평균에 대한 90% 신뢰구간을 구하세요.
from scipy.stats import norm
import numpy as np

#표본평균구하기
x = np.array([79.1, 68.8, 62.0, 74.4, 71.0, 60.6, 98.5, 86.4, 73.0, 40.8, 61.2, 68.7, 61.6, 67.7, 61.7, 66.8])
x.mean()

z_005 = norm.ppf(0.95, loc = 0, scale= 1)
z_005

#신뢰구간
x.mean() + z_005 *6 / np.sqrt(16)
x.mean() - z_005 *6 / np.sqrt(16)



#데이터로부터 E[X^2] 구하기
x = norm.rvs(loc = 3, scale = 5, size = 100000)
np.mean(x**2)
sum(x**2) / (len(x)-1)그러

#몬테카를로 적분: E[(x-x**2) / (2*x)] 구하기
x = norm.rvs(loc = 3, scale = 5, size = 100000)
np.mean(x**2)
np.mean((x-x**2) / (2*x))


#표본을 10만개 추출해서 S^2을 구해보세요.
np.random.seed(20240729)
x = norm.rvs(loc = 3, scale = 5, size = 100000)
x_bar = x.mean()
s_2 = sum((x - x_bar)**2) / (100000 - 1)
s_2

#매서드를 이용해서 쉽게 구하자!
np.var(x, ddof=1) #n-1로 나눈 값 (표본분산)
np.var(x, ddof=0) #n으로 나눈 값


#n-1 vs. n
x = norm.rvs(loc = 3, scale = 5, size = 20)
np.var(x) #n으로 나눈 값
np.var(x, ddof = 1) #n-1로 나눈 값




#Do it python 교재 8장 p.212
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

economics = pd.read_csv("./data/economics.csv")
economics.head()

economics.info()
sns.lineplot(data = economics, x = "date", y = "unemploy")
plt.show()
plt.clf()

#날짜 시간 타입 변수 만들기
economics["date2"] = pd.to_datetime(economics['date'])
economics.info()

economics[["date", "date2"]] #로 date와 date2는 다름을 확인할 수 있다.


#데이터 타입 
economics['date2'].dt

#어트리뷰트 사용으로 연 추출하기
economics['date2'].dt.year
#어트리뷰트 사용으로 월 추출하기
economics['date2'].dt.month
#어트리뷰트 사용으로 일 추출하기
economics['date2'].dt.day
#어트리뷰트 사용으로 분기 추출하기
economics['date2'].dt.quarter


economics["quarter"] = economics["date2"].dt.quarter
economics[["date2", "quarter"]]


#각 날짜는 무슨 요일인가?
economics["date2"].dt.day_name()


#매서드 사용으로 월 이름 추출하기
economics['date2'].dt.month_name()

#날짜데이터에 월, 일을 더해주기 
economics['date2'] + pd.DateOffset(days = 30)
economics['date2'] + pd.DateOffset(months = 1)

economics["date2"].dt.is_leap_year #윤년체크

#p.216 연도 변수 만들고 그래프 만들기 
economics['year'] = economics['date2'].dt.year
economics.head()

sns.lineplot(data = economics, x = 'year', y = 'unemploy', errorbar = None)
#errorbar를 해주면 신뢰구간(연한 파랑)이 제거된 상태로 나타남.
sns.scatterplot(data=economics, x = 'year', y = 'unemploy', s =  1)
#특정 연도의 1월부터 12월까지의 정보가 담겨있음
plt.show()
plt.clf()


#error bar를 설정하지 않고, 신뢰구간을 표시하지 않는 그래프를 그려보기 
#연도로 그룹화해주고 월별 평균과 실업자수 표준편차, 연도별 표기된 월 개수
my_df = economics.groupby('year', as_index = False) \
         .agg(
            mon_mean = ('unemploy', 'mean'),
            mon_std = ('unemploy', 'std'),
            mon_n = ("unemploy", "count")
        )
my_df
#mean + 1.96*std/sqrt(12)
my_df["left_ci"] = my_df["mon_mean"] - 1.96 * my_df["mon_std"] / np.sqrt(my_df["mon_n"])
my_df["right_ci"] = my_df["mon_mean"] + 1.96 * my_df["mon_std"] / np.sqrt(my_df["mon_n"])
my_df.head()

x = my_df["year"]
y = my_df["mon_mean"]
#plt.scatter(x, y, s = 3)
plt.plot(x,y,color = "black")
plt.scatter(x, my_df["left_ci"], color = "blue", s = 1) #점 찍힌 위치를 연결시키면 신뢰구간
plt.scatter(x, my_df["right_ci"], color = "blue", s= 1)
plt.show()
plt.clf()















