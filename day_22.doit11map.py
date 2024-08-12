import json
geo = json.load(open('data/SIG.geojson', encoding = 'UTF-8'))

#행정구역 코드 출력
geo['features'][0]['properties']

#위도, 경도 좌표 출력
geo['features'][0]['geometry']

##2.시군구별 인구 데이터 준비하기
import pandas as pd
df_pop = pd.read_csv('./data/Population_SIG.csv')
df_pop.head()
df_pop.info()
df_pop['code'] = df_pop['code'].astype(str)

##3.단계 구분도 만들기
#!pip install folium
import folium
folium.Map(location = [35.95, 127.7], zoom_start = 8)

map_sig = folium.Map(location = [35.95, 127.7],
                    zoom_start = 8,
                    tiles = 'cartodbpositron')
map_sig


folium.Choropleth(
    geo_data = geo,
    data = df_pop,
    columns = ('code', 'pop'),
    key_on = 'feature.properties.SIG_CD') \
      .add_to(map_sig)

map_sig

#------------------------------------11-2: 서울시 동별 외국인 인구 단계 구분도
import json
geo_seoul = json.load(open("./data/SIG_Seoul.geojson", encoding="UTF-8"))


#데이터 탐색
type(geo_seoul)
len(geo_seoul)
geo_seoul.keys()
geo_seoul["features"][0]
len(geo_seoul["features"])
len(geo_seoul["features"][0])
geo_seoul["features"][0].keys()
geo_seoul["features"][0]["properties"]
geo_seoul["features"][0]["geometry"].keys()

#숫자가 바뀌면 "구"가 바뀐다.
coordinate_list=geo_seoul["features"][0]["geometry"]["coordinates"]
len(coordinate_list[0][0])
coordinate_list[0][0]

#재정리
len(coordinate_list) # 1 , 대괄호 4개
len(coordinate_list[0])  # 1, 대괄호 3개
len(coordinate_list[0][0]) # 2332개

import numpy as np
coordinate_array=np.array(coordinate_list[0][0])
x=coordinate_array[:,0]
y=coordinate_array[:,1]


import matplotlib.pyplot as plt
plt.plot(x, y)
#plt.plot(x[::10], y[::10]) 성능은 올라가지만 해상도가 떨어짐
plt.show()
plt.clf()
#-------------------
#함수를 넣어 지역을 달리하여 그래프 만들기
def draw_seoul(num):
    gu_name=geo_seoul["features"][num]["properties"]["SIG_KOR_NM"]
    coordinate_list=geo_seoul["features"][num]["geometry"]["coordinates"]
    coordinate_array=np.array(coordinate_list[0][0])
    x=coordinate_array[:,0]
    y=coordinate_array[:,1]

    plt.rcParams.update({"font.family": "Malgun Gothic"})
    plt.plot(x, y)
    plt.title(gu_name)
    # 축 비율 1:1로 설정
    plt.axis('equal')
    plt.show()
    plt.clf()
    
    return None

draw_seoul(12)

#--------------------
#Population까지, 서울시 전체 시각화해보기
import pandas as pd
import json
geo = json.load(open('data/SIG.geojson', encoding = 'UTF-8'))

#구 이름을 리스트 만들기
# 방법 1
gu_name=list()
for i in range(25):
    gu_name.append(geo_seoul["features"][i]["properties"]["SIG_KOR_NM"])
gu_name

# 방법 2
gu_name = [geo_seoul["features"][i]["properties"]["SIG_KOR_NM"] for i in range(25)]
gu_name





# x, y 판다스 데이터 프레임_앞의 과정을 하지 않아도 한번에 가능하다.
import pandas as pd

def make_seouldf(num):
    gu_name=geo_seoul["features"][num]["properties"]["SIG_KOR_NM"]
    coordinate_list=geo_seoul["features"][num]["geometry"]["coordinates"]
    coordinate_array=np.array(coordinate_list[0][0])
    x=coordinate_array[:,0]
    y=coordinate_array[:,1]

    return pd.DataFrame({"gu_name":gu_name, "x": x, "y": y})

make_seouldf(1)


result = pd.DataFrame({})

for i in range(25):
    result = pd.concat([result, make_seouldf(i)], ignore_index = True)

result
#----------------------------------------서울그래프 그리기
import seaborn as sns
sns.scatterplot(data = result,
    x = 'x', y = 'y', hue = 'gu_name', legend = False, palette = "Blues", s = 2,)
plt.show()
plt.clf()


## 데이터프레임 concat 예제
#df_a = pd.DataFrame({
#    'ID': [],
#    'Name': [],
#    'Age': []
#})
#
#df_b = pd.DataFrame({
#    'ID': [4, 5, 6],
#    'Name': ['David', 'Eva', 'Frank'],
#    'Age': [40, 45, 50]
#})
#df_a=pd.concat([df_a, df_b])

#---------------------서울그래프 그리기
import seaborn as sns
gangnam_df = result.assign(is_gangnam = np.where(result["gu_name"]!="강남구", "안강남","강남"))
sns.scatterplot(
    data=gangnam_df,
    x='x', y='y', legend = False, palette = ['grey', 'red'],
    hue = 'is_gangnam', s = 2)
plt.show()
plt.clf()
gangnam_df["is_gangnam"].unique() #안강남, 강남순이라서 파레트 순서도 그렇게 지정됨 



#팔레트를 딕셔너리로 넣어서 색상이랑 연결시키기 
import seaborn as sns
gangnam_df = result.assign(is_gangnam = np.where(result["gu_name"]!="강남구", "안강남","강남"))
sns.scatterplot(
    data=gangnam_df,
    x='x', y='y', legend = False, palette = {'안강남': 'grey', '강남': 'red'},
    hue = 'is_gangnam', s = 2)
plt.show()
plt.clf()
#----------------------------------
import pandas as pd
import numpy as np
import json
geo_seoul = json.load(open("./data/SIG_Seoul.geojson", encoding="UTF-8"))
geo_seoul["features"][0]["properties"]

df_pop = pd.read_csv("data/Population_SIG.csv")
df_seoulpop = df_pop.iloc[1:26]
df_seoulpop["code"] = df_seoulpop["code"].astype(str)
df_seoulpop.info() #code가 object 로 바뀐것을 확인할 수 있음

#패키지 설치
#!pip install folium
import folium
center_x = result["x"].mean()
center_y = result["y"].mean()
#p.304
#흰 도화지 맵 가져오기
map_sig = folium.Map(location = [37.551, 126.973],
                     zoom_start = 12,
                     tiles = "cartodbpositron")
map_sig.save('map_seoul.html')

#코로플릿 사용해서 - 구 경계선 그리기
geo_seoul
geo_seoul["features"][0]["properties"]["SIG_CD"]
folium.Choropleth(
    geo_data=geo_seoul,
    data = df_seoulpop,
    columns=("code", "pop"),
    key_on = "feature.properties.SIG_CD").add_to(map_sig)
    
    
map_sig.save("map_seoul.html")


#코로플릿 with bins
bins = list(df_seoulpop["pop"].quantile([0, 0.2, 0.4, 0.6, 0.8, 1]))
folium.Choropleth(
    geo_data=geo_seoul,
    data = df_seoulpop,
    columns=("code", "pop"),
    bins = bins,
    fill_color = "YlGnBu",
    key_on = "feature.properties.SIG_CD").add_to(map_sig)
    

map_sig.save("map_seoul.html")


#점 찍는 법
make_seouldf(0).iloc[:,1:3].mean()
folium.Marker([37.583744, 126.983800], popup = "종로구").add_to(map_sig)

map_sig.save("map_seoul.html")



