from multiprocessing.sharedctypes import Value
from this import d
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def run():
    st.write("Arpit's App😄")
    data = pd.read_csv("JINDRILL.csv")
    D = pd.DataFrame(data)
    st.write(D[["Date","Open Price"]].set_index("Date"))
    c_data = D["Open Price"]
    st.line_chart(c_data)

    fig = go.Figure(
        data=[go.Pie(
            labels=['A', 'B', 'C'],
            values=[30, 20, 50]
        )]
    )
    st.plotly_chart(fig)
    st.write("Pie chart in Streamlit")

if __name__ == "__main__":
    run()
