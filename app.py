import time
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image
import webbrowser


# https://www.youtube.com/watch?v=nSw96qUbK9o (for integrate de data)




def main_page():
    st.sidebar.markdown("COMPANY INFO")

    image = Image.open('image/logorecortado.png')

    st.image(image, width=700)


    st.title('WELCOME')

    st.write('What is THE BURST?')


    st.markdown(
    """
    A optimization model for decentralization of corporate headquarters to rural areas and small cities

    ### What do we do?
    - Optimize your data
    - Predicting your company's success with AI
    - City or town recommendations to place your headquarter with a model based on your business preferences

    ### BENEFITS

    👉 CHOOSE --> THE BEST PLACE FOR YOU HEADQUARTERS

    👉 GAIN --> QUALITY OF LIFE

    👉 SUPPORT --> REGIONAL ECONOMIES""")

    url = 'http://localhost:8501/page1'

    if st.button('FILL FORM NOW 💡'):
        webbrowser.open(url, new=2)

main_page()
