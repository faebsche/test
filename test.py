import streamlit as st
st.set_page_config(layout="wide")
st.write('Hello world!')

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import json
import re

# Load the GeoPandas DataFrame
f = open('platten.json')
data = json.load(f)
df = pd.json_normalize(data["features"], sep="_")
df = df[~df['attributes_tischtennisplatten'].isna()]
geometry = gpd.points_from_xy(df['geometry_x'], df['geometry_y'])

# create GeoDataFrame with the original DataFrame and the geometry column
gdf = gpd.GeoDataFrame(df['attributes_tischtennisplatten'], geometry=geometry)
gdf.crs = 'EPSG:4326'


def remove_non_numbers(column):
    column = column.apply(lambda x: re.sub(r'\D', '', str(x)))
    return column.astype(int)

gdf.attributes_tischtennisplatten = remove_non_numbers(gdf.attributes_tischtennisplatten)
gdf['lat'] = gdf.geometry.centroid.y
gdf['lon'] = gdf.geometry.centroid.x

# Create a Streamlit map plot
st.title('Map Plot Example')
st.map(gdf)


