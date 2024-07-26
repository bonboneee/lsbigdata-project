#do it 167페이지. <데이터 합치기>

#중간고사 데이터 만들기
import pandas as pd
import numpy as np
test1 = pd.DataFrame({'id' : [1, 2, 3, 4, 5], 'midterm' : [60, 80, 70, 90, 85]})
test2 = pd.DataFrame({'id' : [1, 2, 3, 4, 5], 'midterm' : [70, 83, 65, 95, 80]})
test1
test2

total = pd.merge(test1, test2, how = 'left', on = 'id')
total



#40번 학생의 test1값 없음. 총 학생은 6명
test1 = pd.DataFrame({'id' : [1, 2, 3, 4, 5], 'midterm' : [60, 80, 70, 90, 85]})
test2 = pd.DataFrame({'id' : [1, 2, 3, 40, 5], 'midterm' : [70, 83, 65, 95, 80]})
#left join: 왼쪽 기준으로 정렬.
total = pd.merge(test1, test2, how = 'left', on = 'id')
total
#right join: 오른쪽 기준 정렬.
total = pd.merge(test1, test2, how = 'right', on = 'id')
total
#Inner join: 두 데이터의 교집합.
total = pd.merge(test1, test2, how = 'inner', on = 'id')
total
#outer join: 두 데이터의 합집합.
total = pd.merge(test1, test2, how = 'outer', on = 'id')
total


#169p data 가로로 합치기 연습
exam = pd.read_csv("data/exam.csv")
name = pd.DataFrame({'nclass' : [1, 2, 3, 4, 5], 'teacher' : ['kim', 'lee', 'park', 'choi', 'jung']})
name
pd.merge(exam, name, how = "left", on = "nclass")


#데이터를 세로로 쌓는 방법
score1 = pd.DataFrame({'id' : [1, 2, 3, 4, 5], 'score' : [60, 80, 70, 90, 85]})
score2 = pd.DataFrame({'id' : [1, 2, 3, 40, 5], 'score' : [70, 83, 65, 95, 80]})
score1
score2
pd.concat([score1, score2])


test1
test2
pd.concat([test1, test2], axis = 0) #pandas cheat sheet 참고

#07. P.178.데이터 정제
df = pd.DataFrame({"sex" : ["M", "F", np.nan, "M", "F"],
                   "score" : [5, 4, 3, 4, np.nan]})
df
pd.isna(df) #nan값이 있는 것만 true로 뜸!

df["score"] + 1

pd.isna(df).sum() #nan 개수 확인

#결측치 제거
df.dropna() #모든 결측치 제거
df.dropna(subset = "score") #score변수에서 결측치 제거
df.dropna(subset = ["score", "sex"]) #여러 변수 결측치 제거법

exam = pd.read_csv("data/exam.csv")
#데이터 프레임 location을 사용한 인덱싱
exam.loc[[2, 7, 14], ["math"]] = np.nan #exam.loc[행 인덱스, 열 인덱스]
exam
exam.iloc[[2, 7, 14], 2] = np.nan #해당 위치에 nan 들어감
exam
exam.loc[[0],["id", "nclass"]]
exam.iloc[0:2, 0:4]

#수학점수가 50점 이하인 학생들 점수를 점수 50점으로 상향 조정하기
exam.loc[exam['math']<=50, "math"] = 50
exam

#영어점수 90점 이상 90으로 하향 조정 
#iloc조회는 안됨됨
exam.iloc[exam['english']>=90, 3] = 90
exam

#iloc은 숫자벡터로 해야 조회가능
exam.iloc[np.where(exam["english"] >= 90)[0], 3] #np.where도 튜플이라 넘파이 어레이를 인덱스[0]으로 조회시켜줘야함.
exam.iloc[np.array(exam["english"]>= 90), 3] #실행됨.
exam.iloc[exam["english"]>=90, 3] #실행 안됨.


#math점수 50점 이하 "-"로 변경
exam.loc[exam["math"]<=50, "math"] = "-"
exam

#위의 결과를 바탕으로 "-"결측치를 수학점수 평균으로 바꾸고 싶은 경우
#1
math_mean = exam.loc[(exam["math"] != "-"), "math"].mean()
exam.loc[exam['math']=="-", "math"] = math_mean
exam

#2
math_mean = exam.query('math not in ["-"]')["math"].mean()
exam.loc[exam['math']=='-', 'math'] = math_mean
exam

#3
math_mean = exam[exam["math"] != "-"]["math"].mean()
exam.loc[exam["math"]=="-", "math"] = math_mean
exam

#4
exam.loc[exam["math"]=="-",["math"]] = np.nan
math_mean = exam["math"].mean()
exam.loc[pd.isna(exam["math"]),["math"]] = math_mean
exam

#5
#math_mean = exam.loc[exam['math']=='-', 'math'] = math_mean
import pandas as pd
math_mean = np.nanmean(np.array([np.nan if x == "-" else float(x) for x in exam["math"]]))
exam["math"] = np.where(exam["math"] == "-", math_mean, exam["math"])
exam

#6
math_mean = exam[exam["math"] != "-"]["math"].mean()
exam["math"] = exam["math"].replace("-", math_mean)
exam




