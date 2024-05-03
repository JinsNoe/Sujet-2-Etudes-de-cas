#%%
import pandas as pd
import folium
import webbrowser

pd.set_option('display.precision', 2)


data_path_feb = "..\\Data\\01_Courses_usagers\\2023_02\\"
data_path_jun = "..\\Data\\01_Courses_usagers\\2023_06\\"

render_map_path = "render_map\\"
#%%
stations = pd.read_csv(data_path_feb + "All_data_courses.csv", sep=";").loc[:, ['from_stat', 'Latitude_start', 'longitude_start']].drop_duplicates().reset_index()
stations = stations.rename(columns={"from_stat": "nom", "Latitude_start": "lat", "longitude_start": "long"})

print(stations)
#%%
avg_loc = stations[['lat', 'long']].mean()
map_paris = folium.Map(locaion=avg_loc, zoom_start=15)

for station in stations.itertuples():
    marker = folium.Marker(location=(station.lat, station.long), tooltip=station.nom)
    marker.add_to(map_paris)
#%%