from scipy.stats import bernoulli
#!pip install scipy
#확률질량함수(pmf)
#확률변수가 갖는 값에 해당하는 확률을 저장하고 있는 함수
#bernoulli.pmf(k,p)
#P(X=1)
bernoulli.pmf(1, 0.3)
#P(X=0)
bernoulli.pmf(0, 0.3)


#P(X=k | n, p)
#n: 베르누이 확률변수 더한 갯수
#p : 1이 나올 확률
#binom.pmf(k, n ,p)
from scipy.stats import binom
binom.pmf(0, n =2, p=0.3)
binom.pmf(1, n =2, p=0.3)
binom.pmf(2, n =2, p=0.3)

#x1에서 부터 x30까지 확률이 0.3인 경우의 확률변수를 list로 나타내기
#베르누이 확률변수를 30개 구한 경우
result = [binom.pmf(x, n =30, p=0.3) for x in range(31)]
result

#numpy로 나타내기
import numpy as np
binom.pmf(np.arange(31), n = 30, p = 0.3)

#조합
import math
math.factorial(54) / math.factorial(26) * math.factorial(28)
math.comb(54,26)
#fact_54 = np.cumprod(np.arange(1, 55))[-1]로 시도하려 했으나 음수떠서 실패
#ln
log(a*b) = log(a) + log(b)
log(1 * 2 * 3 * 4) = log(1) + log(2) + log(3) + log(4)

np.log(24)
sum(np.log(np.arange(1, 5)))

math.log(math.factorial(54))
logf_54 = sum(np.log(np.arange(1, 55)))
logf_26 = sum(np.log(np.arange(1, 27)))
logf_28 = sum(np.log(np.arange(1, 29)))

np.exp(logf_54 - (logf_26 + logf_28))


math.comb(2, 0)*0.3**0*(1-0.3)**2
math.comb(2, 1)*0.3**1*(1-0.3)**1
math.comb(2, 2)*0.3**2*(1-0.3)**0

#probability mass function(확률질량함수)
binom.pmf(0, 2, 0.3)
binom.pmf(1, 2, 0.3)
binom.pmf(2, 2, 0.3)

#X~B(n=10, p = 0.36)일때 P(x=4)는?
binom.pmf(4, 10, 0.36)

#X~B(n=10, p = 0.36)일때 P(x<=4)는?
sum(binom.pmf([0, 1, 2, 3, 4], 10, 0.36))
#또는
binom.pmf(np.arange(5), 10, 0.36).sum()

#P(2<X<=8)일때 값?
binom.pmf(np.arange(9), 10, 0.36).sum()-binom.pmf(np.arange(2), 10, 0.36).sum()
#아니면
binom.pmf()

#X~B(30,0.2) 확률변수 X가 4보다 작고 25보다 크거나 같은 확률을 구하시오?
1- sum(binom.pmf(np.arange(4, 26), 30, 0.2))
#아니면
a = sum(binom.pmf(np.arange(4), 30, 0.2))
b = sum(binom.pmf(np.arange(25,31),30, 0.2))
a+b


#rvs함수(random variable sample)
# 표본추출함수
#X1~Bernoulli(p = 0.3)
bernoulli.rvs(p = 0.3)
#X2~Bernoulli(p = 0.3)
bernoulli.rvs(p = 0.3)
#X~B(n=2, p=0.3)
bernoulli.rvs(0.3) + bernoulli.rvs(0.3)
#를 한줄로 표시하면
binom.rvs(n = 2, p = 0.3, size = 1)

binom.pmf(0, n=2, p=0.3)
binom.pmf(1, n=2, p=0.3)
binom.pmf(2, n=2, p=0.3)

#X~B(30,0.26)
#표본 30개를 뽑아보세요!
binom.rvs(n=30, p=0.26, size=30)

#X~B(30,0.26)에서 E[X]?
#베르누이 확률변수의 기대값은 P다.0.26
#이항분포확률의 기대값은 np다. 30*0.26

#X~B(30,0.26)를 시각화하기
import matplotlib.pyplot as plt
import seaborn as sns
prob_x = binom.pmf(np.arange(31),n = 30, p = 0.26)
sns.barplot(prob_x)
plt.show()
plt.clf()

#교재 p.207
import pandas as pd
x = np.arange(31)
prob_x = binom.pmf(x, n=30, p=0.26)

df = pd.DataFrame({"x":x, "prob": prob_x})
df

sns.barplot(data = df, x = "x", y = "prob")
plt.show()

#cdf : cumulative dist. function
#(누적확률분포 함수)(왼쪽에서 오른쪽까지가 범위)
F(X=x) = P(X <= x)
# P(4<X<=18)를 cdf로 구하기
binom.cdf(18, n=30, p=0.26) - binom.cdf(3, n=30, p=0.26)
# P(13<X<20)를 cdf로 구하기
binom.cdf(19, n=30, p=0.26) - binom.cdf(13, n=30, p=0.26)


#x_1위치에 따라 포인트가 달라지는 그래프
import numpy as np
import seaborn as sns
x_1 = binom.rvs(n=30, p=0.26, size=10)
x_1
x = np.arange(31)
prob_x = binom.pmf(x, n=30, p=0.26)
sns.barplot(prob_x, color = 'blue')

#add a point at (2, 0)
plt.scatter(x_1, np.repeat(0.002,10), color = 'red', zorder =100, s =5)
#기대값 표현
plt.axvline(x=7.8, color = "green", linestyle="--", linewidth=2)

plt.show()
plt.clf()


binom.ppf(0.5, n = 30, p = 0.26)
binom.cdf(8, n=30, p=0.26)

binom.ppf(0.7, n = 30, p =0.26) #np.float64(9.0)
binom.cdf(9, n =30, p=0.26)











#정규분포
1/np.sqrt(2*math.pi) #랑 똑같이 작용하는 아래 공식
from scipy.stats import norm
norm.pdf(0, loc=0, scale=1)
norm.pdf(5, loc=3, scale=4)

#정규분포 pdf그리기
k = np.linspace(-5, 5, 100)
y = norm.pdf(k, loc=0, scale=1)

plt.plot(k,y, color = "black")
plt.show()
plt.clf()

#mu(loc): 분포의 중심을 결정하는 모수
k = np.linspace(-5, 5, 100)
y = norm.pdf(k, loc=0, scale=1)

plt.plot(k,y, color = "black")
plt.show()
plt.clf()

#정규분포의 확률밀도함수
#sigma(scale): 분포의 커짐을 결정하는 모수(표준편차)
k = np.linspace(-5, 5, 100)
y = norm.pdf(k, loc=0, scale=1)
y2 = norm.pdf(k, loc=0, scale=2)
y3 = norm.pdf(k, loc=0, scale=0.5)
plt.plot(k,y, color = "pink")
plt.plot(k,y2, color = "black")
plt.plot(k,y3, color = "green")
plt.show()
plt.clf()

#확률밀도함수에서는 아래에 있는 면적의 넓이를 구해야 함
#그래서 cdf 함수를 사용! P(X <= K)
norm.cdf(0, loc = 0, scale = 1)
#끝에 무한대로 쭉 가다보면 1과 가깝게 성립함
norm.cdf(100, loc = 0, scale = 1)
#연습문제 풀어봄!
norm.cdf(0.54, loc = 0, scale = 1)-norm.cdf(-2, loc = 0, scale = 1)
1 - norm.cdf(3, loc = 0, scale = 1)+norm.cdf(1, loc = 0, scale = 1)
#X~N(3, 5^2)일때 P(3<X<5)= ?인가 인데 답은 15.54%
norm.cdf(5, loc = 3, scale = 5) - norm.cdf(3, loc = 3, scale = 5)
#위의 확률변수에서 표본 1000개 뽑아보자!
x = norm.rvs(loc = 3, scale = 5, size = 1000)
sum((x > 3) & (x < 5))/1000#하면 15퍼센트를 확인할 수 있음





#평균:0, 표준편차:1 , 표본 1000개 뽑아서 0보다 작은 비율 확인
y = norm.rvs(loc=0, scale = 1, size = 1000)
y = sum(y<0)/1000  #np.mean(y<0)도 가능!
y


x = norm.rvs(loc=3, scale=2, size =1000)
x
sns.histplot(x, stat = "density")

#plot the normal distribution PDF
xmin, xmax = (x.min(), x.max())
x_values = np.linspace(xmin, xmax, 100)
pdf_values = norm.pdf(x_values, loc =3, scale =2)
plt.plot(x_values, pdf_values, color = "red", linewidth = 2)

plt.show()
plt.clf()








