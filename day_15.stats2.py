from scipy.stats import uniform
import matplotlib.pyplot as plt
from scipy.stats import uniform
import numpy as np

#<Uniform : 균일분포>
uniform.rvs(loc = 2, scale = 4, size=1) #uniform에서는 loc이 구간 시작점, scale이 구간 길이

x = np.linspace(0, 8, 100)
y = uniform.pdf(x, loc = 2, scale = 4)
plt.plot(x,y, color = "pink")
plt.show()
plt.clf()

#P(X<0.25)=?
uniform.cdf(3.25, loc = 2, scale = 4)

#P(5<X<8.39)=?
uniform.cdf(8.39, loc =2, scale = 4) - uniform.cdf(5, loc =2, scale = 4)

#상위 7% 값은?
uniform.ppf(0.93, loc = 2, scale = 4)

#표본 20개를 뽑아서 표본 평균을 계산해보시오.(random_state는 seed와 비슷한 역할)
x = uniform.rvs(loc = 2, scale = 4, size = 20, random_state = 42)
x.mean()




#표본 20개 뽑고 그래프 만들기
y = uniform.rvs(loc = 2, scale = 4, size = 20*1000, random_state = 42)
y = y.reshape(-1, 20)
y.shape
blue_y = y.mean(axis = 1)
blue_y

import seaborn as sns
sns.histplot(blue_y, stat = "density")
plt.show()

#X bar ~ N(mu, sigma^2/n)
#X bar ~ N(4, 1.333333/20)
from scipy.stats import norm

uniform.var(loc = 2, scale = 4)
uniform.expect(loc = 2, scale = 4)


#plot the normal distribution PDF
xmin, xmax = (blue_y.min(), blue_y.max())
x_values = np.linspace(xmin, xmax, 100)
pdf_values = norm.pdf(x_values, loc =4, scale = np.sqrt(1.333333/20))
plt.plot(x_values, pdf_values, color = "red", linewidth = 2)

plt.show()
plt.clf()







#신뢰구간
#X bar ~ N(mu, sigma^2/n)
#X bar ~ N(4, 1.333333/20)
from scipy.stats import norm

#plot the normal distribution PDF
x_values = np.linspace(3, 5, 100)
pdf_values = norm.pdf(x_values, loc =4, scale = np.sqrt(1.333333/20))
plt.plot(x_values, pdf_values, color = "red", linewidth = 2)


#파란벽돌 (파란벽돌) 점찍기
blue_x = uniform.rvs(loc = 2, scale = 4, size = 20).mean()
a = blue_x + 0.665 #99% 신뢰구간
b = blue_x - 0.665
#a = blue_x + 1.96 * np.sqrt(1.3333333/20) : 95% 신뢰구간
#b = blue_x - 1.96 * np.sqrt(1.3333333/20) : 95% 신뢰구간간
plt.scatter(blue_x, 0.002, color = 'blue', zorder =10, s =10)
plt.axvline(x=b, color = "blue", linestyle="--", linewidth=1)
plt.axvline(x=a, color = "blue", linestyle="--", linewidth=1)
#기대값 표현
plt.axvline(x=4, color = "green", linestyle="-", linewidth=2)
plt.show()
plt.clf()





norm.ppf(0.995, loc = 0,scale = 1)

#a에서 b까지 면적 계산했더니 95%다. a와 b를 구하시오.
a = norm.ppf(0.025, loc = 4, scale =  np.sqrt(1.333333/20))
a
b = norm.ppf(0.975, loc = 4, scale =  np.sqrt(1.333333/20))
b

#a에서 b까지 면적 계산했더니 97%다. a와 b를 구하시오.
a = norm.ppf(0.015, loc = 4, scale =  np.sqrt(1.333333/20))
a
b = norm.ppf(0.915, loc = 4, scale =  np.sqrt(1.333333/20))
b
#중심에서 부터 얼마나 떨어졌는가?
4 - a






