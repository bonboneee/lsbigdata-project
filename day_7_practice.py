import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#(단기체류외국인) 월별 단기체류외국인 국적(지역)별 현황


df_exam = pd.read_csv('data/foreigner.csv',  encoding='euc-kr')
df_exam.columns

df_exam2 = df_exam.copy()

#1. 변수명을 변경
df_exam2 = df_exam.rename(columns={
    '년': 'year',
    '월': 'month',
    '국적지역': 'nationality',
    '단기체류외국인 수': 'visitors'
})
df_exam2

#2. 행 필터링
df_2022 = df_exam2.query('year == 2022')
df_2022

#나라별로 묶어주기
df_2022_nat = df_2022.groupby('nationality')
df_2022_nat

#3.새로운 변수 생성?
df_2022['visitors_sum'] = 

#
