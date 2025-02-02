"""Europe Map with Folium and Streamlit"""

import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium


def europe_map():
    """Europe Map with Folium and Streamlit"""
    st.markdown(
        "<h1 style='color: #50A6D9; text-align: center;'>European Countries Map</h1>",
        unsafe_allow_html=True,
    )
    m = folium.Map(location=[55.0, 10.0], zoom_start=4)
    data = pd.read_csv("europe.csv")
    for row in data.itertuples(index=False):
        name, lat, lon = row.Country, row.Latitude, row.Longitude
        folium.Marker(
            [lat, lon],
            popup=f"({lat}, {lon})",
            tooltip=name,
            icon=folium.Icon(color="blue", icon_color="white", icon="map-marker"),
        ).add_to(m)

    st_folium(m, width=700, height=700)


if __name__ == "__main__":
    europe_map()
