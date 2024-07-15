a = 1, 2, 3 #a =1,2,3
a

a=1,2,3
a#로 하면 이 아이도 튜플로 나옴. 굳이 튜플로 안 써도 튜플의 성질을 가져서 산출


#soft copy, deep copy 개념
#soft copy 설명명
a = [1, 2, 3]
a

b=a
b

a[1]=4
a #[1, 4, 3]

b #[1, 4, 3]
id(a) #2328899394048
id(b) #2328899394048



#deep copy 설명
a = [1, 2, 3]
a

b=a[:] #아니면 b = a.copy()

a[1]=4
a #[1, 4, 3]
id(a) #2328899354368
b #[1, 2, 3]
id(b) #2328898233856




#강의안 3. 수학함수
#제곱근 반환
import math #math모듈은 자동다운되어있지만 사용할 때마다 매번 로드해줘야 실행됨.
x = 4
math.sqrt(x)

# 지수 계산
exp_val = math.exp(5)
print("e^5의 값은:", exp_val) 


# 로그 계산
log_val = math.log(10, 10)
print("10의 밑 10 로그 값은:", log_val)


#정규분포 확률밀도함수
import math

def my_normal_pdf(x, mu, sigma):
  part_1 = (sigma * math.sqrt(2*math.pi))**-1
  part_2 = math.exp((-(x-mu)**2)/(2*sigma**2))
  return part_1*part_2

my normal_pdf(3, 3, 1)


def normal_pdf(x, mu, sigma):
sqrt_two_pi = math.sqrt(2 * math.pi)
factor = 1 / (sigma * sqrt_two_pi)
return factor * math.exp(-0.5 * ((x - mu) / sigma) ** 2)


def my_function(x, y, z):
  return(x**2 + math.sqrt(y) + math.sin(z)* math.exp(x))

my_function(2, 9, math.pi/2)


def my_g(x):
  return math.cos(x) + math.sin(x) * math.exp(x)

my_g(math.pi)

import numpy as np

#Ctrl + shift+ c: 커맨드처리
#!pip install numpy
import pandas as pd
import numpy as np

# 벡터 생성하기 예제
a = np.array([1, 2, 3, 4, 5]) # 숫자형 벡터 생성
b = np.array(["apple", "banana", "orange"]) # 문자형 벡터 생성
c = np.array([True, False, True, True]) # 논리형 벡터 생성
print("Numeric Vector:", a)
print("String Vector:", b)
print("Boolean Vector:", c)

a #array([1, 2, 3, 4, 5])
type(a) #<class 'numpy.ndarray'>
a[3] #마찬가지로 인덱스 적용됨
a[2:]
a[1:4] #array([2, 3, 4])



b = np.empty(3)
b

b[0]=1
b[1]=4
b[2]=10
b #array([ 1.,  4., 10.])처럼 소수형태로 산출
b[2] #np.float64(10.0)

vec1 = np.array([1, 2, 3, 4, 5])
vec1
#처럼해도 되지만 수가 너무 많으면 힘들어서 생긴 함수
vec1 = np.arange(100)
vec1 #array([ 0,  1,  2,  3,  4,  5,  ... 99])처럼 마지막 수는 안 나옴!

vec1= np.arange(1,101,0.5) #0.5는 단위
vec1



linear_space1 = np.linspace(0, 1, 5)
print("0부터 1까지 5개 원소:", linear_space1)


linear_space2 = np.linspace(0, 1, 5, endpoint=False)
print("0부터 1까지 5개 원소, endpoint 제외:", linear_space2)

vec1 = np.arange(5)
np.repeat(vec1, 5)

#-100부터 0까지
vec2 = np.arange(0,-100, -1)
vec3 = -np.arange(0, 100)
vec2
vec3

#repeat vs. tile
vec1 = np.arange(5)
np.repeat(vec1, 3) #array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4])
np.tile(vec1, 3) #array([0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4])

vec1 + vec1 #같은 위치의 애들끼리 덧셈을 해줌 array([0, 2, 4, 6, 8])


max(vec1) #np.int64(4)
sum(vec1) #np.int64(10)

#35672 이하 홀수들의 합은?
vec4 = np.arange(1, 35673, 2)
vec4 #array([    1,     3,     5, ..., 35667, 35669, 35671])

sum(vec4) #np.int64(318122896)
#np.arange(1, 35673, 2).sum() 해도 실행됨.

len(vec4) #17836
vec4.shape #(17836,) 크기를 튜플로 반환함


# 2차원 배열
b = np.array([[1, 2, 3], [4, 5, 6]])
length = len(b) # 첫 번째 차원의 길이:2
shape = b.shape # 각 차원의 크기: (2, 3)
size = b.size # 전체 요소의 개수: 6


a = np.array([1, 2])
b = np.array([1, 2, 3, 4])
a + b #ValueError: operands could not be broadcast together with shapes (2,) (4,) 
#a와 b의 길이가 맞지 않아서 생긴 문제다.

np.tile(a, 2)+b #array([2, 4, 4, 6])
np.repeat(a,2)+b #array([2, 3, 5, 6])


b==3 #array([False, False,  True, False])


#35672보다 작은 수 중에서 7로 나눠서 나머지가 3인 숫자들의 개수는?
sum((np.arange(1, 356752)%7)==3) #np.int64(5096)

#10보다 작은 수 중에서 7로 나눠서 나머지가 3인 숫자들의 개수는?
sum((np.arange(1, 10)%7)==3) #np.int64(1)


