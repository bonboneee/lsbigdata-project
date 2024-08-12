import pandas as pd
import numpy as np
import seaborn as sns
#!pip install pyreadstat
#<do it python 9장_한국복지패널 데이터 분석>
raw_welfare = pd.read_spss("./data/koweps/Koweps_hpwc14_2019_beta2.sav")
raw_welfare

welfare = raw_welfare.copy()
welfare.shape
welfare.describe()

welfare=welfare.rename(columns = {
                            "h14_g3": "sex",
                            "h14_g4" : "birth",
                            "h14_g10": "marriage_type",
                            "h14_g11": "religion",
                            "p1402_8aq1": "income",
                            "h14_eco9": "code_job",
                            "h14_reg7": "code_region"})
                            
welfare = welfare[["sex", "birth","marriage_type", "religion","income","code_job","code_region"]]
welfare.shape
welfare


welfare["sex"].dtypes
welfare["sex"].value_counts()
#nan값 확인: welfare["sex"].isna().sum()

welfare["sex"] = np.where(welfare["sex"] == 1, "male", "female")
welfare["sex"].value_counts()

welfare["income"].describe()
welfare["income"].isna().sum()

sum(welfare["income"] > 9998) #무응답이 nan으로 처리된것을 발견

sex_income = welfare.dropna(subset ="income") \
                     .groupby("sex", as_index = False) \
                     .agg(mean_income = ("income", "mean"))



sex_income
import matplotlib.pyplot as plt
import seaborn as sns
sns.barplot(data = sex_income, x = "sex", y = "mean_income", hue = "sex")
plt.show()
plt.clf()

#숙제: 위 그래프에서 각 성별 95% 신뢰구간 계산 후 그리기
#위 아래 검정색 막대기로 표시 
#norm.ppf() 사용해서 그릴 것.



#p. 235 나이와 월급의 관계
welfare["birth"].describe()
sns.histplot(data=welfare, x="birth")
plt.show()
plt.clf()

welfare["birth"].isna().sum()

welfare = welfare.assign(age= 2019 - welfare["birth"] + 1)
welfare["age"]
sns.histplot(data=welfare, x = "age")
plt.show()
plt.clf()

#나이별 월급 평균표 만들기
age_income = welfare.dropna(subset ="income") \
                     .groupby("age", as_index = False) \
                     .agg(mean_income = ("income", "mean"))

age_income.head()

sns.lineplot(data = age_income, x = 'age', y = 'mean_income')
plt.show()
plt.clf()




#나이별 income 칼럼 na 개수 세기(무응답자 수 그래프)
my_df = welfare.assign(income_na= welfare["income"].isna()) \
                .groupby("age", as_index = False) \
                .agg(n = ("income_na", "sum"))

sns.barplot(data= my_df,x= "age",y = "n")
plt.show()
plt.clf()





#9-4연령대에 따른 월급차이
#나이변수 살펴보기
welfare['age'].head()

#연령대 변수 만들기
welfare = welfare.assign(ageg= np.where(welfare['age']<30, 'young',
                               np.where(welfare['age']<=59, 'middle',
                                                            'old')))

                                                                
welfare['ageg'].value_counts()

#빈도 막대 그래프 만들기
sns.countplot(data = welfare, x = 'ageg')
plt.show()
plt.clf()

#연령대별 월급 평균표 만들기
ageg_income = welfare.dropna(subset = 'income') \
                     .groupby('ageg', as_index = False) \
                     .agg(mean_income = ('income', 'mean'))
                     
                     
#막대그래프 만들기
sns.barplot(data = ageg_income, x = 'ageg', y = 'mean_income')
plt.show()
plt.clf()


#막대 정렬하기
sns.barplot(data = ageg_income, x = 'ageg', y = 'mean_income', order = ['young', 'middle', 'old'])
plt.show()
plt.clf()



#version2. 나이대별 수입 분석
#cut(구간 나누기)
bin_cut = np.array([0, 9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 109, 119])
welfare = welfare.assign(age_group = pd.cut(welfare["age"],
                bins=bin_cut,
                labels = (np.arange(12) * 10).astype(str) + "대"))

age_income = welfare.dropna(subset = 'income') \
                     .groupby('age_group', as_index = False) \
                     .agg(mean_income = ('income', 'mean'))
                     
age_income
sns.barplot(data=age_income, x = 'age_group', y = 'mean_income')
plt.show()
plt.clf()

#p.244 연령대 및 성별 월급 차이

#판다스 데이터 프레임을 다룰때, 변수의 타입이 카테고리로 설정되어 있는 경우,
#groupby+agg 콤보 안먹힘. 그래서 object 타입으로 바꿔준 후 수행
welfare["age_group"] = welfare["age_group"].astype("object")



sex_age_income = \
    welfare.dropna(subset="income") \
    .groupby(["age_group", "sex"], as_index = False) \
    .agg(mean_income = ("income", "mean"))
    
    
sex_age_income

sns.barplot(data=sex_age_income,
            x = "age_group", y = "mean_income", hue = "sex")
            
plt.show()
plt.clf()

#연령대별, 성별 상위 4% 수입을 찾아보세요!
def my_f(vec):
    return vec.sum()

sex_age_income = \
    welfare.dropna(subset="income") \
    .groupby(["age_group", "sex"], as_index=False) \
    .agg(top4per_income=("income", lambda x: my_f(x)))
    
sex_age_income


sex_age_income = \
    welfare.dropna(subset="income") \
    .groupby(["age_group", "sex"], as_index=False) \
    .agg(top4per_income=("income", lambda x: np.quantile(x, q=0.96))
    
    


sex_age_income

sns.barplot(data=sex_age_income,
            x="age_group", y="top4per_income", 
            hue="sex")
plt.show()
plt.clf()

#참고(람다를 쓰지 않고 agg로도 구할 수 있다.)
welfare.dropna(subset = 'income') \
        .groupby('sex', as_index = False)[['income']] \ #대괄호 하나하면 시리즈, 두개하면 데이터프레임.
        .agg(['mean', 'std'])


#cut쓰는 법 vers.2
bin_cut = np.array([0:190:10])
pd.cut(welfare['age'], bin_cut)







#day18_doitpython 9-6장
#!pip install  openpyxl

# 9-6장
# merge 복습
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'



welfare = pd.read_spss("data/koweps_hpwc14_2019_beta2.sav")

raw_welfare = pd.DataFrame(welfare)

# 복사본 만들기
welfare = raw_welfare.copy()

# rename
welfare = welfare.rename(
    columns={"h14_g3": "sex",
            "h14_g4": "birth",
            "h14_g10": "marriage_type",
            "h14_g11": "religion",
            "p1402_8aq1": "income",
            "h14_eco9": "code_job",
            "h14_reg7": "code_region"})

welfare = welfare[["sex", "birth", "marriage_type", "religion", "income", "code_job", "code_region"]]

welfare["code_job"]
welfare["code_job"].dtypes

list_job = pd.read_excel("C:/Users/USER/Documents/LS빅데이터스쿨/LSBigdata_Project1/data/Koweps_Codebook_2019.xlsx", sheet_name="직종코드")
list_job.head()

welfare = welfare.merge(list_job, how="left", on="code_job")
welfare.dropna(subset="code_job")[["code_job", "job"]].head()

job_income = welfare.dropna(subset = ["job", "income"]) \
                    .groupby("job", as_index = False) \
                    .agg(mean_income = ("income", "mean"))
job_income.head()

# 수입 top10
top10 = job_income.sort_values("mean_income", ascending = False).head(10)

#막대 그래프 그리기
sns.barplot(data = top10, y = "job", x = "mean_income", hue = "job",)
plt.xticks(fontsize=8)
plt.yticks(fontsize=5)
plt.show()
plt.clf()

# 수입 bottom10
bottom10 = job_income.sort_values("mean_income").head(10)

#막대 그래프 그리기
sns.barplot(data = bottom10, y = "job", x = "mean_income", hue = "job",)
plt.xticks(fontsize=8)
plt.yticks(fontsize=5)
plt.show()
plt.clf()






#263페이지 종교 유무에 따른 이혼율표 만들기
welfare.info()
welfare["marriage_type"]
df = welfare.query("marriage_type != 5") \
            .groupby("religion", as_index = False) \
            ["marriage_type"] \
            .value_counts(normalize = True)#normalize가 핵심
df

df.query("marriage_type == 1") \
    .assign(proportion=df["proportion"]*100) \
    .round(1)






