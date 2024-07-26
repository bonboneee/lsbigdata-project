#do it 교재 99페이지
import pandas as pd
import numpy as np

exam = pd.read_csv("data/exam.csv")
exam.head(10)
exam.tail(10)
exam.shape #(20, 5) #메서드가 아닌 어트리뷰트라서 괄호 없음.
#메서드 vs 속성(어트리뷰트)
exam.info()
exam.describe()

#데이터 탐색색 함수
#head()
#tail()
#shape
#info()
#describe


#내장함수: 설치 x, 로드 x
#패키지함수: 설치o, 로드o
#매서드: 로드o, 객체생성o
type(exam) #판다스 데이터 프레임
var = [1, 2, 3]
type(var) #<class 'list'> 각각의 객체에 사용할 수 있는 매서드가 다르다
#그래서 list는 .head() 불가한 것.

#복사본에 변수명 바꾸기
exam2 = exam.copy()
exam2.rename(columns={"nclass" : "class"}) #임시적이니까 아래의 코드처럼 변수 설정해주기
exam2 = exam2.rename(columns={"nclass" : "class"})
exam2

#총계 변수 만들기
exam2["total"] = exam2["math"] + exam2["english"] + exam2["science"]
exam2.head()

#조건 충족 여부 확인해서 구별남기기
exam2['test'] = np.where(exam2["total"] >= 200, 'pass', 'fail')
exam2


import matplotlib.pyplot as plt
exam2["test"].value_counts().plot.bar(rot=0)

plt.show()
plt.clf()
#value_counts()까지의 결과값
#pass    11
#fail     9
#Name: count, dtype: int64


exam2['test2'] = np.where(exam2["total"] >= 200, "A",
                 np.where(exam2["total"]>= 100, "B", "C"))
exam2.head()


#isin
exam2["test2"].isin(["A", "C"])


#do it 책, 132, 06. 자유자재로 데이터 가공하기
#데이터 전처리 함수
#query()
#df[]
#sort_values()
#groupby()
#assign()
#agg()
#merge()
#concat()

exam = pd.read_csv("data/exam.csv")
#조건에 맞는 행을 걸러내는 .query()
exam.query("nclass == 1")
#exam[exam["nclass"] == 1]
exam.query("nclass != 1")
exam.query("nclass in [1, 2]")
exam.query("nclass not in [1, 2]")
#exam[~exam["nclass"].isin([1, 2])]

exam.query('math > 50')
exam.query('math < 50')
exam.query('english >= 50')
exam.query('english <= 80')

exam.query('nclass == 1 and math >= 50')
exam.query('nclass == 1 & math >= 50')
exam.query('nclass == 2 & english >= 80')

exam.query('math >= 90 or english >= 90')
exam.query('math >= 90 | english >= 90')
exam.query('math < 90 | science < 50')

exam.query('nclass == 1 | nclass == 3 | nclass == 5')
exam.query('nclass in [1, 3, 5]')

nclass1 = exam.query("nclass == 1")
nclass2 = exam.query("nclass == 2")

nclass1['math'].mean()
nclass2['math'].mean()


#145페이지 06.3 필요한 변수만 추출하기
exam[["id", "nclass"]]
exam["id"] #Name: id, dtype: int64: 시리즈임
exam.drop(columns = ["math", "english"]) #이것도 임시적이라 변수 할당해줘야 저장됨.
exam

exam.query("nclass == 1")[["math", "english"]]#두개 이상은 리스트 형태로 안에 넣어주면 된다.
exam.query("nclass == 1")\
    [["math", "english"]]\
    .head()

#정렬하기
exam.sort_values("math")
exam.sort_values("math", ascending = False) # 내림차순
exam.sort_values(["nclass", "english"], ascending = [True, False]) # 각각 오름, 내림차순

#변수 추가_assign
exam = exam.assign(
    total = exam["math"]+exam["english"]+exam["science"],
    mean = (exam["math"]+exam["english"]+exam["science"]) / 3
    )\
    .sort_values("total", ascending = False)
    #이것도 임시, 그래서 변수에  재할당.
exam.head()


#lamda : 짧게 가능
exam2 = pd.read_csv("data/exam.csv")
exam2 = exam.assign(
    total = lambda x: x["math"]+x["english"]+x["science"],
    mean = lambda x: x["total"] / 3 #앞줄에서 total, lambda만 이렇게 가능함.
    )\
    .sort_values("total", ascending = False)
exam2.head()

#그룹을 나눠서 요약을 하는 .groupby() + .agg() 콤보
exam2.agg(mean_math = ("math", "mean"))
exam2.groupby("nclass")\
     .agg(mean_math = ("math", "mean")) #반별 수학 평균
     

#반별 과목별 평균
exam.groupby("nclass")\
    .agg(mean_math = ("math", "mean"),
         mean_eng = ("english", "mean"),
         mean_sci = ("science", "mean"),
    )


#165페이지, 오류 있음
import pydataset
df = pydataset.data("mpg")
df_new = df.query('category == "suv"')\
           .assign(total = (df['hwy'] + df['cty']) / 2) \
           .groupby('manufacturer')\
           .agg(mean_tot = ('total', 'mean'))\
           .sort_values('mean_tot', ascending = False) \
           .head()
df_new



