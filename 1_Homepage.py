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
    col1, col2, col3 = st.columns(3)
    with col1:
       st.header("Joel Greenblatt - Magic Formula")
       st.image("imagens/joel_greenblat_mf.png")

    with col2:
       st.header("Quantamental - value investig")
       st.image("imagens/value_invest.png")

    with col3:
       st.header("corujinha")
       st.image("https://static.streamlit.io/examples/owl.jpg")

# ESPECULATIVA - PAGE #
if selected2 == "Epeculativa":
    col1, col2, col3 = st.columns(3)
    with col1:
       st.header("Momentum Strategy")
       st.image("imagens/momentum.png")

    with col2:
       st.header("Notícias, NLP e O Mercado")
       st.image("imagens/news_sent_anal.png")

    with col3:
       st.header("L.R. 50 ações do IBOV")
       st.image("imagens/top50_ibov_lin_reg.png")
    
# VALUE-INVEST - PAGE #
if selected2 == "Estudos":
    st.title('Estudos')
