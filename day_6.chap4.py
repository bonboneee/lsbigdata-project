import pandas as pd
import numpy as np


df=pd.DataFrame({'name':["김지훈", "이유진", "박동현", "김민지"],
                'english' : [90, 80, 60, 70],
                'math' : [50, 60, 100, 20]})

df

type(df) #<class 'pandas.core.frame.DataFrame'>
df['name'] #Name: name, dtype: object가 아래에 뜸(시리즈라서)
type(df['name']) #<class 'pandas.core.series.Series'>

#평균
sum(df["english"])/4

#84페이지 문제
df_1 = pd.DataFrame({'제품' : ["사과", "딸기", "수박"],
            '가격' : [1800, 1500, 3000],
            '판매량' : [24, 38, 13]})
sum(df_1["가격"])/3
sum(df_1["판매량"]/3)

df[["name", "english"]] #리스트만 받음
#df[("name", "english")] #튜플이기때문에 에러 발생



#04-3 외부데이터 이용하기

import pandas as pd
!pip install openpyxl
df_exam = pd.read_excel("data/excel_exam.xlsx")
df_exam

sum(df_exam["math"])/20
sum(df_exam["english"])/20
sum(df_exam["science"])/20

df_exam.shape #(20, 5)
len(df_exam) #20
df_exam.size #100

#헤더가 없는 경우에는
#df_exam = pd.read_excel("data/excel_exam.xlsx", header = None)

#엑셀 시트가 두개인 경우
df_exam = pd.read_excel("data/excel_exam.xlsx", sheet_name="Sheet2")
df_exam

#기존의 항목으로 총계, 평균 셀 만들기
df_exam = pd.read_excel("data/excel_exam.xlsx")
df_exam["total"] = df_exam["math"] + df_exam["english"] + df_exam["science"]
df_exam

df_exam["mean"] = df_exam["total"]/3
df_exam

df_exam["math"] > 50 #시리즈 생성
#수학과 영어 성적이 동시에 50점 초과
(df_exam["math"] > 50) & (df_exam["english"] > 50)

#수학이 평균보다 높고 영어는 평균보다 낮은 사람
mean_m = np.mean(df_exam["math"])
mean_e = np.mean(df_exam["english"])
df_exam[(df_exam["math"] > mean_m) & (df_exam["english"] < mean_e)]
df_exam

#이중에서도 3반학생들만 꺼내오고 수,영,과 성적 포함하기
df_nc3 = df_exam[df_exam["nclass"] == 3]
df_nc3[["math", "english", "science"]]
df_nc3[1:4]
df_nc3[1:2]
df_nc3[0:1] #한줄만 뽑아오는 경우, 독특함.. [0]은 안 먹힘


df_exam = pd.read_excel("data/excel_exam.xlsx")
df_exam[0:10:2]

df_exam.sort_values("math", ascending=False) #do it교재 151페이지
df_exam.sort_values(["nclass", "math"], ascending = [True, False])

#np.where(a>3, "Up", "Down") 
# np. where 조건 만족하는 위치를 찾아서 튜플로 산출
# up, down 쓰고 산출하니 np.array 형태로 산출
df_exam["updown"] = np.where(df_exam["math"] > 50, "Up", "Down")
df_exam








