import time
import webbrowser
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image
import webbrowser


###------FORM PART------###



# def page1():
st.markdown("""# 👉 FILL WITH YOUR COMPANY DATA

""")

with st.form(key='my_form'):

    employees = st.slider('How many employees does your company have?', 0, 3000)
    st.write("Employees number is", employees)



    budget = st.text_input('What is your budget?')
    st.write('Your budget is', budget)


    sector = st.selectbox(
        'In which business sector are you located?',
        ('Education',
        'Public service',
        'Financial services',
        'Health services',
        'Agriculture, plantations, other rural sectors',
        'Food, beverages, tobacco',
        'Trade',
        'Construction',
        'Manufacture of transport equipment',
        'Hotel, catering, tourism',
        'Chemical industry',
        'Mechanical engineering and electrical engineering',
        'Media, culture, graphics',
        'Mining',
        'Petroleum and gas production',
        'Base metal production',
        'Postal and telecommunication and telecommunications services',
        'Professional services',
        'Utilities (water, gas, electricity)',
        'Forestry, pulp',
        'Textiles, apparel, leather, footwear',
        'Transportation',
        'Maritime transport, fishing, inland transport'))


    st.write('Company sector:', sector)


    dist_airplane = st.selectbox(
    'What is the maximum distance between your headquarter and the airport (kilometers)?',
    ('50', '100', '1000'))

    st.write('Optime distance to transport:', dist_airplane, 'KM')




    dist_train = st.selectbox(
    'What is the maximum distance between your headquarter and the train (kilometers)?',
    ('20', '50', '100', '2000'))

    st.write('Optime distance to transport:', dist_train, 'KM')


    quality = st.radio('How important is the quality of life of your employees?', ('low', 'medium', 'high'))

    st.write(quality)

    subsidies = st.radio('Do you want subsidies?', ('Yes', 'No'))

    st.write(subsidies)


    st.sidebar.markdown("QUESTION FORM  📈 ")


    uploaded_files = st.file_uploader("OPTIONAL: UPLOAD EXTRA INFO OF YOUR COMPANY", accept_multiple_files=True)

    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)


    submit_button = st.form_submit_button(label='Submit form')

    if submit_button:
        st.write('Submit succes')

        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete + 1)

        with st.spinner('Wait for it...'):
            time.sleep(2)
            st.success('Model done!')
            st.balloons()

url = 'http://localhost:8501/page2'

if st.button('See Results'):

    webbrowser.open(url, new=2)


# page1()






 ###--------API PART-------####


import time
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image
import webbrowser
import folium
from streamlit_folium import folium_static
import requests



# def page2():

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


response = requests.get(
    f'http://localhost:8000/?employees={employees}&budget={budget}&dist_airplane={dist_airplane}&dist_train={dist_train}&quality={quality}&subsidies={subsidies}',
    # params={'employees':employees, 'budget':budget, 'dist_airplane':dist_airplane, 'dist_train':dist_train, 'quality':quality, 'subsidies':subsidies},
    ).json()
st.write(response)



# df = pd.DataFrame(
#     np.random.randn(10000, 2) / [50, 50] + [46.0000000, 2.0],
#     columns=['lat', 'lon'])

# st.map(df)


# final_dataframe()

st.sidebar.markdown("OPTIMATION RESULT ✅ ")

def create_map(coord1,city1,coord2,city2,coord3,city3):
    m=folium.Map(location=[46.71109, 1.7191036],zoom_start=5)
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

map_rel = create_map(response['coordinates'][0],response['nom_commune_complet'][0],response['coordinates'][1],response['nom_commune_complet'][1],response['coordinates'][2],response['nom_commune_complet'][2])
folium_static(map_rel)

chart_data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=["First city", "Second city", "Third city"])

st.bar_chart(chart_data)
# page2()



url = 'http://localhost:8501/page3'
if st.button('CONTINUE'):
    webbrowser.open(url, new=2)
