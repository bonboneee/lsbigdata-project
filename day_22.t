import numpy as np
import pandas as pd
tab3 = pd.read_csv('data/tab3.csv')
tab3

tab1 = pd.DataFrame({"id": np.arange(1, 13),
                    "score": tab3["score"]})
tab1


tab2 = tab1.assign(gender = ["female"]*7 + ["male"]*5)
tab2


#1표본 t검정(그룹 1개)
#귀무가설 vs. 대립가설
#H0: mu = 10 vs. Ha: mu != 10
#유의수준 5%로 설정
from scipy.stats import ttest_1samp

result = ttest_1samp(tab1["score"], popmean=10, alternative='two-sided')
t_value = result[0] #t검정 통계량
p_value = result[1] #유의확률 (p-value)
result.pvalue
result.statistic
result.df #자유도
ci = result.confidence_interval(confidence_level = 0.95)
ci[0]
ci[1]
