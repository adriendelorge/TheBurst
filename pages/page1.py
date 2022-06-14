import csv
import time
import webbrowser
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import webbrowser
import streamlit as st
import altair as alt
from PIL import Image
import folium
from streamlit_folium import folium_static
import requests
from streamlit_chat import message




###------PART 1: FORM------###


hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden; }
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_menu_style, unsafe_allow_html=True)


st.markdown("""# 👉 FILL WITH YOUR COMPANY DATA

""")

with st.form(key='my_form'):

    employees = st.slider('How many employees does your company have?', 0, 3000)
    st.write("Employees number is", employees)



    budget = st.text_input('What is your budget?')
    st.write('Your budget is', budget)


    sector = st.selectbox(
        'In which business sector are you located?',
        ('BE - Manufacturing',
        'FZ - Construction',
        'GI - Retail, transports, hotels, restaurants',
        'JZ - Information and communication',
        'KZ - Financial and Insurance activities',
        'LZ - Real Estate',
        'MN - Specialized activities, science and technology, administrative services',
        'OQ - Education, public administration, health, social action',
        'RU - Others'))

    sector = sector[0:2]


    st.write('Company sector:', sector)


    competitors = st.radio('How important is it to you that there are companies from the same business sector in the city?'

    , ('low', 'medium', 'high'))

    st.write('Importance:', competitors)


    dist_airplane = st.selectbox(
    'What is the maximum distance between your headquarter and the airport (kilometers)?',
    ('50', '100', '500', '1000'))

    st.write('Optime distance to transport:', dist_airplane, 'KM')


    dist_train = st.selectbox(
    'What is the maximum distance between your headquarter and the train (kilometers)?',
    ('20', '50', '100', '500', '1000'))

    st.write('Optime distance to transport:', dist_train, 'KM')


    quality = st.radio('How important is the quality of life of your employees?'

    , ('low', 'medium', 'high'))

    st.write('Our Quality of Life score is calculated on the basis of:')
    st.write('- The average available income per household (after all basic life expenses : buying/renting a home, food etc.')
    st.write('- Security level')
    st.write('- Access to education')
    st.write('- Sports facilities')
    st.write('- Access to medical facilities')
    st.write('- Access to other basic facilities (shops, cultural facilities, leisure etc.)')

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

        with st.spinner('Wait for it... 🤖 '):
            time.sleep(5)
            st.success('Model done!')


# url = 'http://localhost:8501/page2'





 ###--------PART 2: API AND RESULTS-------####



# if submit_button:
st.markdown("# 👉 THE BURST RESULTS")



response = requests.get(
    f'http://localhost:8086/?employees={employees}&budget={budget}&dist_airplane={dist_airplane}&dist_train={dist_train}&quality={quality}&subsidies={subsidies}',
    ).json()


st.subheader('RECOMMENDATION ORDER (press the squares for more individual information)')

first_rel = st.checkbox(f'1) {response["nom_commune_complet"][0]}📍')

if  first_rel:
    st.text(f'📍 Located in {response["nom_departement"][0]} deparment, {response["nom_region"][0]} region')
    st.text(f'🛫 The nearest airport is {response["Airport"][0]}, located {round(response["Distance_x"][0])} KM away')
    st.text(f'🚆 The nearest train station is {response["Train"][0]}, located {round(response["Distance_y"][0])} KM away')
    st.text(f'👥 The population in the city is {round(response["Population"][0])} people')
    st.text(f'💰 The average m2 price is  ${round(response["PrixMoyen_M2"][0])}')

second_rel = st.checkbox(f'2) {response["nom_commune_complet"][1]}📍')

if second_rel:
    st.text(f'📍 Located in {response["nom_departement"][1]} deparment, {response["nom_region"][1]} region')
    st.text(f'🛫The nearest airport is {response["Airport"][1]}, located {round(response["Distance_x"][1])} KM away')
    st.text(f'🚆The nearest train station is {response["Train"][1]}, located {round(response["Distance_y"][1])} KM away')
    st.text(f'👥 The population in the city is {round(response["Population"][1])} people')
    st.text(f'💰The average m2 price is  ${round(response["PrixMoyen_M2"][1])}')

third_rel = st.checkbox(f'3) {response["nom_commune_complet"][2]}📍')

if third_rel:
    st.text(f'📍 Located in {response["nom_departement"][2]} deparment, {response["nom_region"][2]} region')
    st.text(f'🛫The nearest airport is {response["Airport"][2]}, located {round(response["Distance_x"][2])} KM away')
    st.text(f'🚆The nearest train station is {response["Train"][2]}, located {round(response["Distance_y"][2])} KM away')
    st.text(f'👥 The population in the city is {round(response["Population"][2])} people')
    st.text(f'💰The average m2 price is  ${round(response["PrixMoyen_M2"][2])}')


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



#---- Export result as a file ----#


path = 'model_result.csv'

results1 = [response["nom_commune_complet"][0],response["nom_commune_complet"][1],response["nom_commune_complet"][2]]

data1 = {'City': results1}

dataframe = pd.DataFrame(data1).to_csv(path)


csv = pd.DataFrame(data1).to_csv()


def page3(csv):

    st.sidebar.markdown("DOWNLOAD MODEL")

    st.download_button(
    label="Download model result as CSV",
    data=csv,
    file_name='model_result.csv',
    mime='text/csv')


page3(csv)


# url = 'http://localhost:8501/page3'


if st.button('Contact us'):

    # time.sleep(3)
    time.sleep(1)
    message("Thank you very much for using The Burst")

    time.sleep(2)
    message("Leave us your contact if you want to get more detailed information about the model.")

    time.sleep(2)
    message("👇")


    number = st.text_input('NUMBER / EMAIL')
