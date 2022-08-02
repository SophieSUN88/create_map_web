'''
Implement a web(HTML) maping with Python(folium): interactive mapping of volcanoes with 
map popup window to introduce different latitudes and longitudes information, 
and populations by adding another polygon layer from JSON data, combined with layer control panel.
'''
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000 :
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [38,-99], zoom_start = 4) #, tiles = "Mapbox Bright"

fgv = folium.FeatureGroup(name = "Volcanoes")

# add circle point
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt,ln], radiums = 8, popup='The elevation : ' + str(el)+' m',
    fill_color=color_producer(el), color = 'grey', fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "Population")
# add polygon layer
fgp.add_child(folium.GeoJson(data = (open('world.json','r',encoding='utf-8-sig').read()),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('Map.html')