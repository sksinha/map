import streamlit as st
import json
import geopandas as gpd
import pyproj
import plotly.graph_objs as go
# reading in the polygon shapefile
polygon = gpd.read_file(r"\Downloads\CityBoundaries.shp")
