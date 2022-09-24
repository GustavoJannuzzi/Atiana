import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import pandas as pd
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import streamlit as st

### MENU HORIZONTAL ###
st.set_page_config(
    page_title=("Estratégias Quantitativas")
)

selected2 = option_menu(None, ["Home", "Value-invest", "Epeculativa", 'Estudos'], 
    icons=['house', 'bar-chart', "dice-3-fill", 'book'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2


# HOME - PAGE #
if selected2 == "Home":
    st.title("Home-page")

# VALUE-INVEST - PAGE #
if selected2 == "Value-invest":
    with col1:
       st.header("A cat")
       st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
       st.header("A dog")
       st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
       st.header("An owl")
       st.image("https://static.streamlit.io/examples/owl.jpg")

# ESPECULATIVA - PAGE #
if selected2 == "Epeculativa":
    with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")
    
# VALUE-INVEST - PAGE #
if selected2 == "Estudos":
    st.title('Estudos')
