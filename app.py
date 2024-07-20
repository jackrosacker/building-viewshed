import streamlit as st
import leafmap.maplibregl as leafmap
from maplibre.plugins import MapboxDrawControls, MapboxDrawOptions
import geopandas as gpd
import os

rail_buffer = gpd.read_file(
    filename="data/bldg_viewshed.gpkg",
    layer="NYC_Planimetric_Database_ Railroad Line_20240623_buffer_10ft",
)
rail_lines = gpd.read_file(
    filename="data/bldg_viewshed.gpkg",
    layer="NYC_Planimetric_Database_ Railroad Line_20240623",
)

MAPTILER_KEY = os.environ["MAPTILER_API"]

st.title("Building Viewshed Generator")

col1, col2 = st.columns([5, 1])

with col1:
    m = leafmap.Map(center=[-73.97, 40.77], zoom=10, style="positron")
    draw_options = MapboxDrawOptions(
        display_controls_default=False,
        controls=MapboxDrawControls(
            polygon=True, line_string=False, point=False, trash=True
        ),
    )
    # Add 3D buildings to map
    # m.add_basemap("Esri.WorldImagery", visible=False)
    # source = {
    #     "url": f"https://api.maptiler.com/tiles/v3/tiles.json?key={MAPTILER_KEY}",
    #     "type": "vector",
    # }

    # layer = {
    #     "id": "3d-buildings",
    #     "source": "openmaptiles",
    #     "source-layer": "building",
    #     "type": "fill-extrusion",
    #     "min-zoom": 15,
    #     "paint": {
    #         "fill-extrusion-color": [
    #             "interpolate",
    #             ["linear"],
    #             ["get", "render_height"],
    #             0,
    #             "lightgray",
    #             200,
    #             "royalblue",
    #             400,
    #             "lightblue",
    #         ],
    #         "fill-extrusion-height": [
    #             "interpolate",
    #             ["linear"],
    #             ["zoom"],
    #             15,
    #             0,
    #             16,
    #             ["get", "render_height"],
    #         ],
    #         "fill-extrusion-base": [
    #             "case",
    #             [">=", ["get", "zoom"], 16],
    #             ["get", "render_min_height"],
    #             0,
    #         ],
    #     },
    # }
    # m.add_source("openmaptiles", source)
    # m.add_layer(layer)
    m.add_draw_control(draw_options)
    m.to_streamlit()

with col2:
    bldg_height_ft = st.number_input(
        "Max. Building Height (ft)", min_value=1, max_value=1000, value=50, step=1
    )
    calculate_viewshed = st.button(label="Calculate Viewshed", type="primary")

    st.divider()

    start_over = st.button(label="Start Over")
# mod_message = "Number to add to final roll results. Can be positive or negative, must be an integer"

# num_of_dice = st.number_input(
#     "Number of dice", min_value=1, max_value=100, value=1, step=1
# )

# sides = st.number_input("Number of sides", min_value=2, max_value=100, value=20, step=2)

# modifier = st.number_input("Modifier", min_value=-1000, max_value=1000, value=0, help=mod_message)

# total, roll_results, modifier = Die(sides=sides).roll_dice(num_of_dice=num_of_dice, modifier=modifier)

# if st.button(f"Roll {num_of_dice} d {sides} + ({modifier})", type="primary"):
#     st.write(f"Total: **{total}**")

#     with st.expander("See individual roll results"):
#         # src: discuss.streamlit.io/t/python-list-output-as-markdown-lists-beautify-lists/23303/2
#         # return list results as unspaced markdown bullets
#         s = ""
#         for result in roll_results:
#             s += f"{result}\n"

#         st.markdown(f"Roll results: {s}")
#         f"Modifier: {modifier}"

# st.divider()

# st.title("Dolmenwood Character Generator")

# tooltip_ability_scores = "Each ability score is generated by rolling and summing 3d6"

# if st.button("Generate Ability Scores", type="primary", help=tooltip_ability_scores):
#     a_character = Character()

#     a_character.generate_ability_scores()

#     replacement_dict = {
#         "str": "Strength",
#         "int": "Intelligence",
#         "wis": "Wisdom",
#         "dex": "Dexterity",
#         "con": "Constitution",
#         "cha": "Charisma",
#     }

#     df = (
#         pd.DataFrame.from_dict(a_character.ability_scores, orient="index")
#         .reset_index()
#         .replace(replacement_dict)
#     )

#     # st.table(df.style.hide())

#     st.dataframe(df, column_config={"index": "Ability", "0": "Score"}, hide_index=True)