"""Data Dashboard Bar Graph with Slider Using Streamlit"""

import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def data_getter(file="tmp/sales_data.xlsx"):
    """Get data from a file."""
    if not os.path.exists(file):
        raise FileNotFoundError(f"File not found: {file}")
    return pd.read_excel(file)


if __name__ == "__main__":
    df = data_getter()
    st.title("Sales Data Visualization")
    year = st.slider(
        "Select a Year", min_value=min(df["Year"]), max_value=max(df["Year"])
    )
    sales_value = df[df["Year"] == year]["Sales"].values[0]
    st.write(f"Sales for the year {year}: ${sales_value}")
    fig, ax = plt.subplots()
    ax.bar(df["Year"], df["Sales"])
    ax.set_xlabel("Year")
    ax.set_ylabel("Sales")
    ax.set_title("Sales Over the Years")
    ax.axvline(x=year, color="red", linestyle="--")
    st.pyplot(fig)
