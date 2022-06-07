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

    url = 'https://theburstapp.herokuapp.com/page1'

    if st.button('FILL FORM NOW 💡'):
        webbrowser.open(url, new=2)

main_page()
















# def page1():
#     st.markdown("""# 👉 FILL WITH YOUR COMPANY DATA

# """)

#     with st.form(key='my_form'):

#         number = st.slider('How many employees does your company have?', 0, 3000)
#         st.write("Employeess number is", number)



#         budget = st.text_input('What is your budget?')
#         st.write('Your budget is', budget)

#         option = st.selectbox(
#             'In which business sector are you located?',
#             ('Education',
#             'Public service',
#             'Financial services',
#             'Health services',
#             'Agriculture, plantations, other rural sectors',
#             'Food, beverages, tobacco',
#             'Trade',
#             'Construction',
#             'Manufacture of transport equipment',
#             'Hotel, catering, tourism',
#             'Chemical industry',
#             'Mechanical engineering and electrical engineering',
#             'Media, culture, graphics',
#             'Mining',
#             'Petroleum and gas production',
#             'Base metal production',
#             'Postal and telecommunication and telecommunications services',
#             'Professional services',
#             'Utilities (water, gas, electricity)',
#             'Forestry, pulp',
#             'Textiles, apparel, leather, footwear',
#             'Transportation',
#             'Maritime transport, fishing, inland transport'))


#         st.write('Company sector:', option)


#         option = st.selectbox(
#         'How close do you want your headquarter to be to the train / airport (kilometers)?',
#         ('0-50', '50-100', '>100'))

#         st.write('Optime distance to transport:', option, 'KM')



#         st.sidebar.markdown("QUESTION FORM  📈 ")


#         uploaded_files = st.file_uploader("EXTRA INFO", accept_multiple_files=True)
#         for uploaded_file in uploaded_files:
#             bytes_data = uploaded_file.read()
#             st.write("filename:", uploaded_file.name)
#             st.write(bytes_data)

#         # with st.form(key='my_form'):
#         submit_button = st.form_submit_button(label='Submit form')

#         if submit_button:
#             st.write('Submit succes')

#     with st.spinner('Wait for it...'):
#         time.sleep(5)
#         st.success('Model done!')


# def page2():
#     st.markdown("# 👉 THE BURST RESULTS")

#     st.text('Recomendation order')



#     first_rel = st.checkbox('1) First city')

#     if  first_rel:
#      st.text(' Plot down the results details')

#     second_rel = st.checkbox('2) Second city')

#     if second_rel:
#      st.text(' Plot down the results details')

#     third_rel = st.checkbox('3) Third city')

#     if third_rel:
#      st.text(' Plot down the results details')


#     # st.text('1) First city, Plot down the results details')
#     # st.text('2) Second city, Plot down the results details')
#     # st.text('3) Third city, Plot down the results details')

#     st.text('DATA RESULTS OVERVIEW')


#     chart_data = pd.DataFrame(
#      np.random.randn(100, 3), #### ----- labels = Params of model and number ----- ###
#      columns=["First city", "Second city", "Third city"])

#     st.bar_chart(chart_data)

#     df = pd.DataFrame(
#      np.random.randn(10000, 2) / [50, 50] + [46.0000000, 2.0],
#      columns=['lat', 'lon'])

#     st.map(df)


#     st.sidebar.markdown("OPTIMATION RESULT ✅ ")



# def page3():
#     st.markdown("# 👉 THANKS!!")
#     st.sidebar.markdown("DOWNLOAD MODEL")



#     st.download_button(
#      label="Download model result as CSV",
#      data='csv',
#      file_name='large_df.csv', #### ----- put the model data result ------ ###
#      mime='text/csv')
