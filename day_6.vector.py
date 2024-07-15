import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = 2.0
a * b

a.shape
b.shape


# 2차원 배열 생성
matrix = np.array([[ 0.0, 0.0, 0.0],
 [10.0, 10.0, 10.0],
 [20.0, 20.0, 20.0],
 [30.0, 30.0, 30.0]])
matrix.shape
# 1차원 배열 생성
vector = np.array([1.0, 2.0, 3.0])
vector.shape
# 브로드캐스팅을 이용한 배열 덧셈
result = matrix + vector
print("브로드캐스팅 결과:\n", result) 

# 2차원 배열 생성 
matrix = np.array([[ 0.0, 0.0, 0.0],
 [10.0, 10.0, 10.0],
 [20.0, 20.0, 20.0],
 [30.0, 30.0, 30.0]])
# 벡터 생성
vector = np.array([1.0, 2.0, 3.0, 4.0]
# 브로드캐스팅을 이용한 배열 덧셈
result = matrix + vector
print("브로드캐스팅 결과:\n", result)

#vector 재정렬
vector = np.array([1.0, 2.0, 3.0, 4.0]).reshape(4,1) #행이 하나 열이 네개
vector
vector.shape
result = matrix + vector
print("브로드캐스팅 결과:\n", result)


#강의안 5. 백터와 친해지기
#넘파이 벡터 슬라이싱

import numpy as np
# 벡터 슬라이싱 예제, a를 랜덤하게 채움
np.random.seed(42) #seed를 사용하면 같은 값이 발생함.
a = np.random.randint(1, 21, 10) #1에서 20까지 10개의 정수 발생
print(a)
# 두 번째 값 추출
print(a[1])

#5.1.1 파이썬 인덱싱
a[::1]#마지막은 스텝
a[2:5]
a[-2]#맨끝에서 두번째
a[1:6:2] #1부터 5까지 2스텝으로

#1에서부터 1000사이의 3의 배수의 합은?
a = np.arange(3,1001,3)
sum(a)

#x= np.arange(1, 1001)
#sum(x[2:1000:3])

#x= np.arange(0, 1001)
#sum(x[::3])


#5.1.1a
print(a[[0, 2, 4]])

# 두 번째 값 제외하고 추출
print(np.delete(a, 1))
print(np.delete(a, [1, 3])) #리스트 사용해서 여러개 제외시킴


#5.1.2 논리 연산자
a = np.arange(1,10)
a>3
a[a>3]

np.random.seed(42) #seed를 사용하면 같은 값이 발생함.
a = np.random.randint(1, 10000,5)
a
(a>2000)&(a<5000)#a[조건을 만족하는 논리형 벡터]
a[(a>2000)&(a<5000)]




#!pip install pydataset
import pydataset

df = pydataset.data('mtcars')
df
np_df = np.array(df['mpg'])
np_df

model_names = np.array(df.index)

#15이상 25이하인 자동차모델은?
model_names[(np_df>=5) & (np_df<=25)]

#평균 mpg보다 낮은(미만) 자동차모델은?
model_names[np_df < np.mean(np_df)]


#15이상 25이하인 데이터 개수는?
sum((np_df>=5) & (np_df<=25))

#평균 mpg보다 높은(이상) 자동차 대수?
sum(np_df >= np.mean(np_df))

#15 작거나 22이상인 데이터 개수는?
sum((np_df < 15) | (np_df >= 22))

np.random.seed(2024)
a = np.random.randint(1, 10000, 5)
a
b = np.array(["A", "B", "C", "F", "W"])
b
#a[조건을 만족하는 논리형 벡터]
a[(a > 2000) & (a<5000)]
b[(a > 2000) & (a<5000)]


#필터링을 이용한 벡터 변경
a[a>3000] = 3000
a


#where함수
np.random.seed(2024)
a = np.random.randint(1, 100, 10)
a
a < 50
np.where(a < 50)

np.random.seed(2024)
a= np.random.randint(1, 26346, 1000)
a


#처음으로 5000보다 큰 숫자가 나왔을 때, 그 숫자 위치와 그 숫자는 무엇인가?
np.random.seed(2024)
a= np.random.randint(1, 26346, 1000)
a
#a[a > 5000][0]
#a[np.where(a > 5000)]

#처음으로 22000보다 큰 숫자가 나왔을때, 숫자 위치와 숫자는 무엇?
x = np.where(a > 22000)
type(x)
my_index = x[0][0]
a[my_index]


#처음으로 24000보다 큰 숫자가 나왔을때 위치?
np.where(a > 24000)
my_index = x[0][0]
a[my_index]


#처음으로 10000보다 큰 숫자들 중 50번째로 나오는 숫자 위치와 숫자 무엇?
x = np.where(a > 10000)
a[x[0][49]]

#500보다 작은 숫자들 중 가장 마지막으로 나오는 숫자 위치와 그 숫자는 무엇?
x = np.where(a<500)
a[x[0][-1]] #391번째 위치



#5.1.7
import numpy as np
a = np.array([20, np.nan, 13, 24, 309])
a +3
np.mean(a) #np.float64(nan)처럼 숫자가 안 나옴.
np.nan + 3 #nan
np.nanmean(a) #nan무시하고 평균냄.
np.nan_to_num(a, nan = 0) #nan값을 원하는 값으로 설정 가능

#5.1.7none
False
a = None #변수를 초기화
b = np.nan
b
a
b+1 #nan
a+1 #error

a = np.array([20, np.nan, 13, 24, 309])
np.isnan(a)
a_filtered = a[~np.isnan(a)]
a_filtered

#벡터 합치기
str_vec = np.array(["사과", "배", "수박", "참외"])
str_vec
str_vec[[0, 2]]

mix_vec = np.array(["사과", 12, "수박", "참외"], dtype=str)
#리스트는 숫자, 문자 섞여도 허용, 벡터는 한가지만 허용, 조정후 모두 문자형 
mix_vec

combined_vec = np.concatenate((str_vec, mix_vec))
#conceatenate는 튜플과 리스트 모두를 허용함.np.concatenate([str_vec, mix_vec])
combined_vec


col_stacked = np.column_stack((np.arange(1, 5), np.arange(12, 16)))
col_stacked

row_stacked = np.vstack((np.arange(1, 5), np.arange(12, 16)))
row_stacked #강의안에서는 row_stack()함수로 표기되어있음. 이제는 vstack쓰자.


#5.1.10.b 길이가 다른 벡터 합치기
uneven_stacked = np.column_stack((np.arange(1, 5), np.arange(12, 18)))
uneven_stacked #하면 에러뜸.

vec1 = np.arange(1, 5)
vec2 = np.arange(12, 18)
vec1 = np.resize(vec1, len(vec2))
vec1 #array([1, 2, 3, 4, 1, 2])

uneven_stacked = np.vstack((vec1, vec2))
uneven_stacked


#5.1.11.a 연습 문제 1
#주어진 벡터의 각 요소에 5를 더한 새로운 벡터를 생성하세요
a = np.array([1, 2, 3, 4, 5])
a +5 

#주어진 벡터의 홀수 번째 요소만 추출하여 새로운 벡터를 생성하세요.
a = np.array([12, 21, 35, 48, 5])
a[0::2]

#주어진 벡터에서 최대값을 찾으세요
a = np.array([1, 22, 93, 64, 54])
a.max()

#주어진 벡터에서 중복된 값을 제거한 새로운 벡터를 생성하세요.
a = np.array([1, 2, 3, 2, 4, 5, 4, 6])
np.unique(a)

#주어진 두 벡터의 요소를 번갈아 가면서 합쳐서 새로운 벡터를 생성하세요.
a = np.array([21, 31, 58])
b = np.array([24, 44, 67])
x = np.empty(6)
x

#짝수번째
x[1::2] = b #아니면 x[[1, 3, 5]]
x
#홀수번째
x[0::2] = a #아니면 x[[2, 4, 6]]
x


