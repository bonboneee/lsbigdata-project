# X ~ N(3, 7^2)

from scipy.stats import norm
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x=norm.ppf(0.25, loc=3, scale=7)
z=norm.ppf(0.25, loc=0, scale=1)

x
3 + z * 7
#X~N(3, 7^2)
#5이하가 나올 확률?
norm.cdf(5, loc=3, scale=7)

norm.cdf(2/7, loc=0, scale=1)

norm.ppf(0.975, loc=0, scale=1)

#표준정규분포 표본 1000개를 뽑고 PDF와 겹쳐보기
z=norm.rvs(loc=0, scale=1, size=1000)
z

x=z*np.sqrt(2) + 3
sns.histplot(z, stat="density", color="grey")
sns.histplot(x, stat="density", color="green")

# Plot the normal distribution PDF
zmin, zmax = (z.min(), x.max())
z_values = np.linspace(zmin, zmax, 500)
pdf_values = norm.pdf(z_values, loc=0, scale=1)
pdf_values2 = norm.pdf(z_values, loc=3, scale=np.sqrt(2))
plt.plot(z_values, pdf_values, color='red', linewidth=2)
plt.plot(z_values, pdf_values2, color='blue', linewidth=2)

plt.show()
plt.clf()







#표준화 확인
x = norm.rvs(loc = 5, scale = 3, size =1000)
#표준화
z = (x - 5)/3
sns.histplot(z, stat = "density", color = "grey")

# Plot the normal distribution PDF
zmin, zmax = (z.min(), z.max())
z_values = np.linspace(zmin, zmax, 100)
pdf_values = norm.pdf(z_values, loc=0, scale=1)
plt.plot(z_values, pdf_values, color='red', linewidth=2)

plt.show()
plt.clf()




#예제1

#표준화 확인 #분산값 주어진 경우
x = norm.rvs(loc = 5, scale = 3, size =1000)
#표준화
z = (x - 5)/3
sns.histplot(z, stat = "density", color = "grey")

# Plot the normal distribution PDF
zmin, zmax = (z.min(), x.max())
z_values = np.linspace(zmin, zmax, 100)
pdf_values = norm.pdf(z_values, loc=0, scale=1)
plt.plot(z_values, pdf_values, color='red', linewidth=2)

plt.show()
plt.clf()
#결론:표준화를 통한 정규분포는 표본정규분포와 같다.





#예제2 #분산을 우리가 추정해야 함(how to?)
#표본표준편차로 나눠도 표준정규분포가 될까?
#1.X표본을 10개 뽑아서 표본 분산값 계산(표본편차를 구하려고)
x = norm.rvs(loc = 5, scale = 3, size =10)
s = np.std(x, ddof=1)
s

#2. X 표본 1000개 뽑음(본격적인 표준화 과정)
x = norm.rvs(loc = 5, scale = 3, size =1000)

#3. 1에서 계산한 S^2(표본 분산)으로 시그마제곱을 대체함(표준화 진행)
z = (x - 5)/s
sns.histplot(z, stat = "density", color = "grey")

#4. Z의 히스토그램 그리기 및 표준 정규분포 PDF 확인하기
zmin, zmax = (z.min(), z.max())
z_values = np.linspace(zmin, zmax, 100)
pdf_values = norm.pdf(z_values, loc=0, scale=1)
plt.plot(z_values, pdf_values, color='red', linewidth=2)

plt.show()
plt.clf()
#결론: Size가 작아서 표준정규분포를 못 따라감.





#t분포에 대해서 알아보자!
#X~ t(df)
#종모양, 대칭분포, 중심 0
#모수 df: 자유도라고 부름 - 퍼짐을 나타내는 모수
#df가 작으면 분산이 커짐.
from scipy.stats import t
#t.pdf
#t.ppf
#t.cdf
#t.rvs

#자유도가 4인 t분포의 pdf를 그려보세요.
t_values = np.linspace(-4, 4, 100)
pdf_values = t.pdf(t_values, df = 4)
plt.plot(t_values, pdf_values, color='red', linewidth=2)
#표준정규분포 겹치기
pdf_values = norm.pdf(t_values, loc = 0, scale = 1)
plt.plot(t_values, pdf_values, color='black', linewidth=2)

plt.show()
plt.clf()
#자유도4 그래프가 표준정규분포보다 극단값 많이 나옴을 알 수 있다.
#자유도가 커질 수록 표준정규분포랑 비슷해짐.(n이 무한대로 가면 표준정규분포가 된다)




#x ~ ?(mu, sigma^2)
#X bar ~ N(mu, sigma^2/n)
#X bar ~= t(x_bar, s^2/n) 자유도가 n-1인 t분포

x = norm.rvs(loc = 15, scale=3, size=16, random_state=42)
x
x_bar = x.mean()
n=len(x)
n
#모분산을 모를 때: 모평균에 대한 95% 신뢰구간을 구해보자!
x_bar + t.ppf(0.975, df=n-1) * np.std(x, ddof = 1) / np.sqrt(n)
x_bar - t.ppf(0.975, df=n-1) * np.std(x, ddof = 1) / np.sqrt(n)

#모분산을 알 때: 모평균에 대한 95% 신뢰구간을 구해보자!
x_bar + norm.ppf(0.975, loc=0, scale = 1) * 3/ np.sqrt(n)
x_bar - norm.ppf(0.975, loc=0, scale = 1) * 3/ np.sqrt(n)










