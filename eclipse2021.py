import geopandas as gpd
import folium

# Load geopandas dataframe of populated places on Earth
cities = gpd.read_file(gpd.datasets.get_path('ne_10m_populated_places_simple'))

# Load the umbral path of the next total solar eclipse in 2021
eclipse2021 = gpd.read_file(gpd.datasets.get_path('TSE_2021_December_04_Umbral_Path-polygon'))

# Spatial join of the eclipse path and populated areas (only 2 points)
ecities=gpd.sjoin(cities, eclipse2021, how='inner')

# Optional alternative appearance of umbral path if using other kind of map to plot
#eclumb = eclipse2021.plot(color='black', edgecolor='orange', categorical=True, alpha=0.5)

# Usual folium Stamen Terrain map in a variable showing where the eclipse is going to take place
designmap = folium.Map(location=(-63.2632994, -55.428932),zoom_start=2,
                                tiles='stamenterrain', attr='http://stamen.com')

# Add eclipse path to the map
folium.GeoJson(eclipse2021, name='Eclipse path').add_to(designmap)

# Add locations of places where eclipse is going to be visible from
folium.Marker(location=[ecities._get_value(4877, 'latitude'), ecities._get_value(4877, 'longitude')],
                      popup='<strong>Orcadas Station</strong>').add_to(designmap)
folium.Marker(location=[ecities._get_value(4878, 'latitude'), ecities._get_value(4878, 'longitude')],
                      popup='<strong>Signy Research Station</strong>').add_to(designmap)

# Save the map to an html file
designmap.save('designmap.html')
