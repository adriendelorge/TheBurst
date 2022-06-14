import time
from urllib import request
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image
import webbrowser
from annotated_text import annotated_text
from streamlit_lottie import st_lottie

# from TheBurst import cities_data, main_file, map, transports, utils


# https://www.youtube.com/watch?v=nSw96qUbK9o (for integrate de data)

# def load_lottier1(url):
#     r = request.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# imagen_coding = load_lottier1("https://assets4.lottiefiles.com/packages/lf20_knvn3kk2.json")
# st.sidebar.markdown(imagen_coding)

def main_page():


    st.sidebar.markdown("THE BURST 🤖")

    image = Image.open('image/logorecortado.png')

    st.image(image, width=700)

    if st.button('CONTINUE'):

        st.title('WELCOME')

        st.markdown('#### What is THE BURST?')



        st.markdown(
        """
        A optimization model for decentralization of corporate headquarters to rural areas and small cities

        #### What do we do?
        - Optimize your data
        - City or town recommendations to place your headquarter with a model based on your business preferences
        - Finding nearby options similar to recommended cities with a deep learning clustering AI model


        #### Benefits

        👉 CHOOSE --> THE BEST PLACE FOR YOU HEADQUARTERS

        👉 GAIN --> QUALITY OF LIFE

        👉 SUPPORT --> REGIONAL ECONOMIES""")

    url = 'http://localhost:8501/page1'

    if st.button('FILL FORM NOW 💡'):
        webbrowser.open(url, new=2)

main_page()
