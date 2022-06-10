import time
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image
import webbrowser
# from TheBurst.main_file import final_dataframe
import folium
from streamlit_folium import folium_static
import requests
# from page1 import employees,budget,dist_airplane,dist_train,quality,subsidies
# import page1



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

    # isbn = '0-7475-3269-9'
    # key = f'ISBN:{isbn}'

    # response = requests.get(
    # f'http://localhost:8000/?employees={employees}&budget={budget}&dist_airplane={dist_airplane}&dist_train={dist_train}&quality={quality}&subsidies={subsidies}',
    # # params={'employees':employees, 'budget':budget, 'dist_airplane':dist_airplane, 'dist_train':dist_train, 'quality':quality, 'subsidies':subsidies},
    # ).json()
    # st.write(response)

    chart_data = pd.DataFrame(
     np.random.randn(100, 3), #### ----- labels = Params of model and number ----- ###
     columns=["First city", "Second city", "Third city"])

    st.bar_chart(chart_data)

    df = pd.DataFrame(
     np.random.randn(10000, 2) / [50, 50] + [46.0000000, 2.0],
     columns=['lat', 'lon'])

    st.map(df)


    # final_dataframe()

    st.sidebar.markdown("OPTIMATION RESULT ✅ ")

    url = 'http://localhost:8501/page3'
    if st.button('CONTINUE'):
        webbrowser.open(url, new=2)

def create_map(coord1,city1,coord2,city2,coord3,city3):

    m=folium.Map(location=[46.71109, 1.7191036],zoom_start=6)

    folium.Marker(
        location=coord1, # coordinates for the marker
        popup=city1, # pop-up label for the marker
        icon=folium.Icon(color='green', icon_color='white', icon='ok-sign', angle=0, prefix='glyphicon')).add_to(m)
    folium.Marker(
        location=coord2, # coordinates for the marker
        popup=city2, # pop-up label for the marker
        icon=folium.Icon(color='lightgreen', icon_color='white', icon='ok-sign', angle=0, prefix='glyphicon')).add_to(m)
    folium.Marker(
        location=coord3, # coordinates for the marker
        popup=city3, # pop-up label for the marker
        icon=folium.Icon(color='lightgreen', icon_color='white', icon='ok-sign', angle=0, prefix='glyphicon')).add_to(m)
    return m





map_rel = create_map([48.85341, 2.3488], 'Paris', [43.29695, 5.38107],'Marseille', [45.74846, 4.84671], 'Lyon')

page2()
folium_static(map_rel)

# url = 'http://localhost:8501/page3'
# if st.button('CONTINUE'):
#     webbrowser.open(url, new=2)

# st.write(page1.employees)



# def create_map(coord1,city1,coord2,city2,coord3,city3):
#     m=folium.Map(location=[46.71109, 1.7191036],zoom_start=6)
#     folium.Marker(
#         location=coord1, # coordinates for the marker
#         popup=city1, # pop-up label for the marker
#         icon=folium.Icon(color='green', icon_color='white', icon='ok-sign', angle=0, prefix='glyphicon')).add_to(m)
#     folium.Marker(
#         location=coord2, # coordinates for the marker
#         popup=city2, # pop-up label for the marker
#         icon=folium.Icon(color='lightgreen', icon_color='white', icon='ok-sign', angle=0, prefix='glyphicon')).add_to(m)
#     folium.Marker(
#         location=coord3, # coordinates for the marker
#         popup=city3, # pop-up label for the marker
#         icon=folium.Icon(color='lightgreen', icon_color='white', icon='ok-sign', angle=0, prefix='glyphicon')).add_to(m)
#     return m
# create_map(final.iloc[0,9],final.iloc[0,4],final.iloc[1,9],final.iloc[1,4],final.iloc[2,9],final.iloc[2,4])
