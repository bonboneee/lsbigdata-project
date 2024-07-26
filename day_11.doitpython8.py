#do it 책 199페이지

import pandas as pd
import matplotlib.pyplot as plt
mpg= pd.read_csv("data/mpg.csv")
mpg.shape
mpg

#!pip install seaborn
import seaborn as sns
plt.figure(figsize=(5, 4))
sns.scatterplot(data=mpg, x = "displ", y = "hwy", hue="drv") \
   .set(xlim = [3, 6], ylim = [10, 30])
plt.show()
plt.clf()


#mpg["drv"].unique()
#do it 막대그래프 205페이지
df = mpg.groupby("drv", as_index=False) \
        .agg(mean_hwy=('hwy', 'mean'))
df
plt.clf()


sns.barplot(data=df.sort_values("mean_hwy"), x = "drv", y = "mean_hwy", hue = "drv")
plt.show()
plt.clf()

# p.208 빈도 막대 그래프
df=df.groupby('drv', as_index = False) \
     .agg(n = ('drv', 'count'))

df

#sns.barplot()으로 빈도 막대그래프 만들기
sns.barplot(data = df, x= 'drv', y = 'n')
plt.show()
plt.clf()

#sns.countplot으로 빈도 막대 그래프 만들기
sns.countplot(data = df, x = 'drv')
plt.show()
plt.clf()

