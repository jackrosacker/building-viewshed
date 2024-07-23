import streamlit as st
# import leafmap.maplibregl as leafmap
# from maplibre.plugins import MapboxDrawControls, MapboxDrawOptions
import geopandas as gpd
import os
from folium.plugins import Draw
import folium

from streamlit_folium import st_folium

# MAPTILER_KEY = os.environ["MAPTILER_API"]

rail_buffer = gpd.read_file(
    filename="data/bldg_viewshed.gpkg",
    layer="NYC_Planimetric_Database_ Railroad Line_20240623_buffer_10ft",
)
rail_lines = gpd.read_file(
    filename="data/bldg_viewshed.gpkg",
    layer="NYC_Planimetric_Database_ Railroad Line_20240623",
)
# draw_options = MapboxDrawOptions(
#     display_controls_default=False,
#     controls=MapboxDrawControls(
#         polygon=True, line_string=False, point=False, trash=True
#     ),
# )
# m = leafmap.Map(center=[-73.97, 40.77], zoom=10, style="positron",)

m = folium.Map(location=[40.77, -73.97], zoom_start=10)
Draw(export=True,
     draw_options={
         'line' = False,
         }).add_to(m)

c1, c2 = st.columns(2)
with c1:
    output = st_folium(m, width=700, height=500)

with c2:
    st.write(output)
    
# if 'shapes' not in st.session_state:
#     st.session_state.shapes = {}
# else:
#     st.session_state.shapes = m.draw_feature_collection_all

# st.title("Building Viewshed Generator")

# m.add_draw_control(draw_options)

# st.write(st.session_state.shapes)
# m.to_streamlit()