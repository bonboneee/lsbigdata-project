import pandas as pd
df = pd.read_csv("./data/houseprice-with-lonlat.csv")
df.info()
df[["Latitude", "Longitude"]].mean()
Latitude = df["Latitude"]
Longitude = df["Longitude"]

import folium
map_sig = folium.Map(location = [42.034482, -93.642897],
                     zoom_start = 12,
                     tiles = "cartodbpositron")
map_sig.save('map_houseprice.html')


for i in range(len(Longitude)):
    folium.Marker([Latitude[i], Longitude[i]]).add_to(map_sig)

map_sig.save('map_houseprice.html')
#---------------------------------------------
import pandas as pd
df = pd.read_csv('./data/houseprice-with-lonlat.csv')
df.columns
df[['Longitude', 'Latitude']].mean()

map_house = folium.Map(location=[42.034482,-93.642897 ],
                    zoom_start=13, tiles='cartodbpositron')
Longitude = df['Longitude']
Latitude = df['Latitude']
Price = df['Sale_Price']

# zip을 쓰면 좀 더 깔끔하게 된다.
for i in range(len(Longitude)):
    folium.CircleMarker([Latitude[i], Longitude[i]],
                        popup=f"Price: ${Price[i]}",
                        radius=3, # 집의 면적으로 표현해보기
                        color='skyblue', 
                        fill_color='skyblue',
                        fill=True, 
                        fill_opacity=0.6 ).add_to(map_house)

map_house.save('map_houseprice.html')
webbrowser.open_new('map_houseprice.html')
