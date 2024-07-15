import pandas as pd
import numpy as np


pd.DataFrame({'name':["김지훈", "이유진", "박동현", "김민지"], 'english' : [90, 80, 60, 70], 'math' : [50, 60, 100, 20]})

df

type(df) #<class 'pandas.core.frame.DataFrame'>

type(df['name'])

df

#평균
sum(df["english"])/4

pd.DataFrame({'제품' : ["사과", "딸기", "수박"],
            '가격' : [1800, 1500, 3000],'판매량' : [24, 38, 13]})
sum()



