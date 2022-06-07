import time
import webbrowser
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image
import webbrowser

def page1():
    st.markdown("""# 👉 FILL WITH YOUR COMPANY DATA

""")

    with st.form(key='my_form'):

        number = st.slider('How many employees does your company have?', 0, 3000)
        st.write("Employeess number is", number)



        budget = st.text_input('What is your budget?')
        st.write('Your budget is', budget)

        option = st.selectbox(
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


        st.write('Company sector:', option)


        option = st.selectbox(
        'How close do you want your headquarter to be to the train / airport (kilometers)?',
        ('0-50', '50-100', '>100'))

        st.write('Optime distance to transport:', option, 'KM')



        st.sidebar.markdown("QUESTION FORM  📈 ")


        uploaded_files = st.file_uploader("EXTRA INFO", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)

        # with st.form(key='my_form'):
        submit_button = st.form_submit_button(label='Submit form')

        if submit_button:
            st.write('Submit succes')

            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)

            with st.spinner('Wait for it...'):
                time.sleep(2)
                st.success('Model done!')

    url = 'https://theburstapp.herokuapp.com/page2'

    if st.button('See Results'):
        webbrowser.open(url, new=2)




page1()
