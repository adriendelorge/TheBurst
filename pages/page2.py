import time
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image
import webbrowser


def page2():
    st.markdown("# 👉 THE BURST RESULTS")

    st.text('Recomendation order')



    first_rel = st.checkbox('1) First city')

    if  first_rel:
     st.text(' Plot down the results details')

    second_rel = st.checkbox('2) Second city')

    if second_rel:
     st.text(' Plot down the results details')

    third_rel = st.checkbox('3) Third city')

    if third_rel:
     st.text(' Plot down the results details')


    st.text('DATA RESULTS OVERVIEW')


    chart_data = pd.DataFrame(
     np.random.randn(100, 3), #### ----- labels = Params of model and number ----- ###
     columns=["First city", "Second city", "Third city"])

    st.bar_chart(chart_data)

    df = pd.DataFrame(
     np.random.randn(10000, 2) / [50, 50] + [46.0000000, 2.0],
     columns=['lat', 'lon'])

    st.map(df)


    st.sidebar.markdown("OPTIMATION RESULT ✅ ")

    url = 'https://theburstapp.herokuapp.com/page3'
    if st.button('CONTINUE'):
        webbrowser.open(url, new=2)

page2()
