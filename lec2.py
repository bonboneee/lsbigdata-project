a=1
a
#ctrl + enter
#shift + 방향
#show folder in new window: 해당위치 탐색기기
#ls 파일 목록
#cd 폴더이동
#.현재 폴더
#..상위폴더
#어느정도 적다가 TAB을 누르면 자동완성, Shift+tab을 누르면 다음 순서 키워드가 도출된다.)
#cls 화면 정리
a=10
a
#같은 변수에 새로운 숫자를 입력하면 리업뎃된다.
#오른쪽에 있는 것을 왼쪽에 넣어줘!(할당의 개념)
a = "안녕하세요!"
a
#이처럼 문자열도 할당 할 수 있다.
a = '안녕하세요!'
a
#작은따옴표, 큰따옴표도 모두 문자열에 들어간다.
a = "'안녕하세요!'라고 아빠가 말했다."
a
#위의 예시처럼 큰따옴표 안에 작은따옴표가 필요한 때가 있기 때문이다.
a = [1, 2, 3]
a
#list개념, 교재 56페이지
b = [4, 5, 6]
a + b
#두가지 변수를 하나로 합치는 과정
a1 = 'LS빅데이터스쿨'
b2 = '화이팅!'
a1 + b2
#문자열도 마찬가지다.
a1 + ' ' +b2
#사이에 따옴표 빈칸을 추가하면 띄어쓰기까지 챙길 수 있다.
print(a1)
#print()를 쓰면 출력하고자 하는 의사를 명확히 할 수 있다. 강의안1.2변수사용하기
#파이썬은 동적 타이핑: 매번 타입을 기재하지 않아도 자동결정된다
#1.3.a변수명규칙(숫자로는 시작할 수없다 1num 안된다)
num1 = 3
num2 = 5
num1 + num2
#변수명이 그 용도를 알 수 있으면 좋다.
#파이썬은 대소문자를 구별한다.
#예약어는 변수명으로 사용할 수 없다.(if, for, class)
#1.3.b 변수명 스타일
#스네이크케이스:ls_bigdata_scool
#카멜케이스:LsBigdataSchool
#2.1 변수할당 및 기본 산술 연산자
a = 10
b = 3.3
print("a+b=", a+b)
print("a-b=", a-b)
print("a*b=", a*b)
print("a/b=", a/b)
print("a%b=", a%b)
print("a//b=", a//b)
print("a**b=", a**b)
#정수와 실수를 계산하니 실수의 값이 나왔다. 
#문자 변수는 연산자와 계산할 수 없다. concatenate: 연결하다.
#Errortype: can only concatenate str (not "list") to str
(a**3)//7
(a**3)%7
#shift+alt+아래화살표 : 아래로 복사
#ctrl+alt+아래화살표 : 커서 여러개 >>> 한꺼번에 여러개 지우고 수정할 때 유용
#강의안3
a == b
a != b
#느낌표 =을 쓰면 아니다 부등호 나옴
a > b
a < b
a >= b
a <= b
# <와 >를 먼저 쓰고, =를 순서대로 넣어줌
#2에 4승과 12453을 7로 나눈 몫을 더해서 8로 나눴을 때 나머지
#9에 7승을 12로 나누고, 36452를 253로 나눈 나머지에 곱한 수
#중 큰 것은?
a = ((2**4)+(12453//7))%8
b = ((9**7)/12)*(36452%253)
a<b
#3.2비교연산자 사용 예
user_age = 25
is_adult = user_age >= 18
#is_adult에는 true, false 두가지 경우가 올 수 있다.
print("성인입니까?", is_adult)

False = 3 #색깔이 다름: 예약어
True = 2

a = "True" #문자열이라서 에러x
b = TRUE #TRUE를 예약어 X, 변수로 인식해서 에러뜸: 변수에 대한 정의 부재(is not defined)
c = true #위의 이유와 동일해서 에러 발생
d = True #예약어

b = TRUE
TRUE = 4
b

#True, False 4-1논리 연산자의 종류류
a = True
b = False
a and b
a or b
not a

True and False #하면 False
True and True
False and False
False and True

True or False
False or False

# True: 1, False: 0으로 처리함
True + True
True + False
False + False

#and는 곱셈으로 치환가능
True *False
True *True
False* False
False* True

#or 연산자 덧셈으로 치환가능
True  or False
True  or True
False or  False
False or  True

a = True
b = False
a or b
min(a+b, 1)

a = False
b = False
a or b
min(a+b, 1)

#5.복합 대입 연산자
a = 3
a += 10
a
#a = a + 10

a -= 4
a
a %= 3
a
a += 12
a **= 2
a /= 7

#연산자 우선순위 표 읽어보기
#5.4문자열에 대한 +연산자
str1 = "hello"
str1 + str1
repeated_str = str1 * 3 #문자열을 반복하는 것에 곱하기가 사용된다. 숫자랑 문자 덧셈 안 됨됨
print("Repeated string", repeated_str)

str1 * 2.5 #can't multiply sequence by non-int of type 'float' 라는 에러뜸.
str1 * -2 #''이렇게 없어져버림.
#정수 : int(eger)
#실수: float(double)

#6.1.a 단항 연산사의 종류 및 기능 읽어보기
x = 5
x
+x #이 아이는 양수야!라고 표시
-x #양수였던 5의 부호를 바꾸어버림
~x

#binary의 약자: bin
bin(5)
bin(-5) #'-0b101'의 결과중에서 0b는 이진수임을 나타냄. 101이 5를 뜻함.(이진수이해)
bin(-4)

#문제1: x =3, bin(~x)의 값?
#~x을 먼저 풀자. 3은 이진수 값이 11이다. -11를 반대로 하면 -4(-00)가 되고
#, bin(-4)값을 구하면 된다.
#-0b(4의 십진수값)임.
#따라서 -0b100이 나온다.
bin(~3)

#1단계: 4를 2진수로 바꾼다.
#00000100
#2단계: 반전시키기
#11111011
#3단계: 1더하기
#11111100
#그래서 파이썬에서는 -0b100 으로 표현된다.

#~(-4)는 00000011이고 0b11
bin(-4)
bin(~-4)

#패키지 함수
max(3, 4)
var1 = [1, 2, 3]
sum(var1)

#책71페이지
pip install pydataset #SyntaxError: invalid syntax
#왜냐하면 pip와 python은 다른 종류라 언어 다름.
#그래서 명령 프롬포트에 작성해야함.

!pip install pydataset
import pydataset
pydataset.data()

df = pydataset.data("AirPassengers")
df
#여기까지가 73페이지

#테스트입니다.
