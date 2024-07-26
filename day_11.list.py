#list는 다른 데이터 타입을 허용함.
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "apple", 3.5, True]

# 빈 리스트 생성
empty_list1 = []
empty_list2 = list()

# 초기값을 가진 리스트 생성
numbers = [1, 2, 3, 4, 5]
range_list = list(range(5))

range_list[3] = "LS 빅데이터 스쿨"
range_list

#두번째 원소에 리스트 넣어보기
range_list[1] = ["1st", "2st", "3st"]
range_list

#"3st"만 가져오고 싶다면?
range_list[1][2]


# 리스트 내포(comprehension)
#1.대괄호로 쌓여져있다.
#2. 넣고 싶은 수식표현을 x를 사용해서 표현
#3. for .. in ..을 사용해서 원소정보 제공

list(range(10))#에서 각 요소에 제곱을 넣고 싶다면 아래와 같이 하기!
squares = [x**2 for x in range(10)]
squares

#3, 5, 2, 15를 세제곱한 리스트 만들기
my_squares = [x**3 for x in [3, 5, 2, 15]]
my_squares

#numpy array로 가능!
import numpy as np
my_squares = [x**3 for x in np.array([3, 5, 2, 15])]
my_squares #[np.int64(27), np.int64(125), np.int64(8), np.int64(3375)]


#pandas 시리즈와도 가능!
import pandas as pd
#!pip install pandas
exam = pd.read_csv("data/exam.csv")
my_squares = [x**3 for x in exam["math"]]
my_squares 


#리스트 합치기
3 + 2
"안녕"+"하세요"
"안녕"*3

# 리스트 연결
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2

(list1 * 3) + (list2 * 5)


# 리스트 각 원소별 반복
numbers = [5, 2, 3]
repeated_list = [x for x in numbers for _ in range(4)]
#repeated_list = [x for x in numbers for _ in [4, 2, 1, 3]]
#4, 2, 1, 3 숫자들만의 어떤 기능이 있기보단 개수만큼 원소가 반복됨.
repeated_list


#for 루프 문법
#for i in 범위:
#   작동방식
for x in [4, 1, 2, 3]:
        print(x)


for i in range(5):
    print(i**2)
    

#리스트를 하나 만들어서
#for 루프를 사용해서 2, 4, 6, 8, ..., 20의 수를
#채워넣어보세요!
#1
new = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in new:
    print(x*2)
#2
[i for i in range(2, 21, 2)]

#3
my_list = []
for i in range(1, 11):
    my_list.append(i*2)
my_list



#cf. 인덱스로 수정하기
my_list = [0] * 10
for i in range(10)
    my_list[i] = 2 * (i + 1)
my_list



#quiz. my_list2를 my_list에 인덱스 공유로 복사시키기.
my_list2 = [2, 4, 6, 80, 10, 12, 24, 35, 23, 20]
my_list = [0] * 10

for i in range(10):
    my_list[i] = my_list2[i]

#quiz. my_list2의 홀수번째 위치에 있는 숫자들만 my_list에 가져오기
my_list2 = [2, 4, 6, 80, 10, 12, 24, 35, 23, 20]
for i in range(5):
    my_list[i] = my_list[2 *i]
    


#for문을 리스트 컴프리헨션으로 바꾸는 방법
#바깥은 무조건 대괄호로 묶어줌: 리스트 반환을 위함
#for 루프의 :는 생략한다.
#실행부분을 먼저 써준다.
#결과값을 발생하는 표현만 남겨두기기
[i*2 for i in range(1, 11)]
[x for x in numbers]

for i in [0, 1]:
    for j in [4, 5, 6]:
         print(i,j)


for i in [0, 1]:
    for j in [4, 5, 6]:
         print(i)


numbers = [5, 2, 3]
for i in numbers:
    for j in range(4):
        print(i, j)

numbers = [5, 2, 3]
for i in numbers:
    for j in range(4):
        print(i)
#리스트 컴프리헨션 변환
[i for i in numbers for j in range(4)]
        

my_list = list(range(1, 11))
my_list



# _의 의미
# 앞에 나온 값을 가리킴
5 + 4
_ + 6 #_는 9를 의미
del _ # _의 기존값을 삭제시켜줘야 다음 번 _를 사용할 때 지장없음

# 값 생략, 자리 차리(placeholder)
a, _, b = (1, 2, 4)
a; b
_
# _ = None
#del _



#7.0.1.d.d 원소 체크
fruits = ["apple", "banana", "cherry"]
"banana" in fruits #True

[x == "banana" for x in fruits]
#를 리스트 컴프리헨션으로 전환
my_list=[]
for x in fruits:
    my_list.append(x == "banana")
my_list


#바나나의 위치를 뱉어내게 하려면?
fruits = ["apple","apple", "banana", "cherry"]
import numpy as np
fruits = np.array(fruits)
int(np.where(fruits == "banana")[0][0])



#list method: reverse : 원소를 거꾸로
fruits = ["apple","apple", "banana", "cherry"]
fruits.reverse()
fruits

#list method: append: 맨끝에 원소 추가
fruits.append("pineapple")
fruits

#list method: insert: 특정 위치에 원소 삽입
fruits.insert(2, "test")
fruits

#list method: pop: 원소 제거
fruits.remove("test")
fruits


import numpy as np
# 넘파이 배열 생성
fruits = np.array(["apple", "banana", "cherry", "apple", "pineapple"])

# 제거할 항목 리스트
items_to_remove = np.array(["banana", "apple"])

# 마스크 (논리형 벡터) 생성
mask = ~np.isin(fruits, items_to_remove)
#mask = ~np.isin(fruits, ["banana", "apple"])
mask #array([False, False,  True, False,  True])

# 불리언 마스크를 사용하여 항목 제거
filtered_fruits = fruits[mask]
print("remove() 후 배열:", filtered_fruits)









