import streamlit as st
import numpy as np
import pandas as pd


# st.markdown("""# Fill the form with your company data
# ## This is a sub header
# This is text""")

# df = pd.DataFrame({
#           'first column': list(range(1, 11)),
#           'second column': np.arange(10, 101, 10)
#         })

# # this slider allows the user to select a number of lines
# # to display in the dataframe
# # the selected value is returned by st.slider
# line_count = st.slider('Select a line count', 1, 10, 3)

# # and used in order to select the displayed lines
# head_df = df.head(line_count)

# head_df

def main_page():

    st.write("# ⚡️ WELCOME TO THE BURST ⚡️")

    st.sidebar.success("Select a demo above.")

    st.markdown(
    """
    Optimization model for business development in rural areas and small cities (what is this?)

    ### What do we do?
    -
    -
    -

    ### BENEFITS

    👉 CHOOSE --> THE BEST PLACE FOR YOU HEADQUARTERS

    👉 GAIN --> QUALITY OF LIFE

    👉 SUPPORT --> REGIONAL ECONOMIES""")

    st.button(" FILL NOW 💡")




def page1():
    st.markdown("""# 👉 FILL THE FORM WITH YOUR COMPANY DATA

""")
    st.sidebar.markdown("QUESTION FORM  📈 ")

def page2():
    st.markdown("# 👉 RESULTS")
    st.sidebar.markdown("OPTIMATION RESULT  ✅ ")

def page3():
    st.markdown("# 👉 THANKS!!")
    st.sidebar.markdown("EXTRA")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 1": page1,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
