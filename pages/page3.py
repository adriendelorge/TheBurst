import time
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image
import webbrowser



def page3():
    st.markdown("# 👉 THANKS!!")
    st.sidebar.markdown("DOWNLOAD MODEL")



    st.download_button(
     label="Download model result as CSV",
     data='csv',
     file_name='large_df.csv', #### ----- put the model data result ------ ###
     mime='text/csv')


page3()
