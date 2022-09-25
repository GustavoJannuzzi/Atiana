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
import webbrowser
from bokeh.models.widgets import Div
import streamlit.components.v1 as components



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
    st.subheader("Para Giant Steps Capital")
    st.markdown("Através dessa aplicação eu gostaria de demonstrar meu interesse em aprender e contribuir com esta gigante fábrica de teses.")
    st.markdown("Aqui apresento alguns de meus projetos desenvolvidos sempre buscando criatividade alida a um breve conhecimento técnico.")
    
    st.write("Streamlit Docs Example iframe")
    components.iframe("https://docs.streamlit.io/en/latest")
    st.write("different iframe test")
    components.iframe(src="http://smb-analytics-metabase.herokuapp.com/public/dashboard/afefddda-d5d4-43ed-83fd-307eab7ded3c", width=1285, height=1000, scrolling=True)
    
    
# VALUE-INVEST - PAGE #
if selected2 == "Value-invest":
    col1, col2 = st.columns(2)
    with col1:
       st.header("Joel Greenblatt - Magic Formula")
       st.image("imagens/joel_greenblat_mf.png")
       st.markdown("A Magic Formula consiste em um procedimento de escolha de ações que consiste em selecionar ativos com bons fundamentos econômicos e que estão sendo negociados a um preço baixo.")
       st.markdown("A formula consiste em gerar um ranking de ações com melhor ROIC e melhor EV/EBIT.")
       st.markdown("Veja mais sobre como a Magic Formula Funciona e quais ações ela selecionaria agora.")
       
       if st.button('Magic Formula'):
           mf_url = "window.open('https://www.gustavojannuzziportfolio.com/magic-formula')"
           html = '<img src onerror="{}">'.format(mf_url)
           div = Div(text=html)
           st.bokeh_chart(div)
          
        

    with col2:
       st.header("Quantamental - value investing")
       st.image("imagens/value_invest.png")
       st.markdown("Quantamental - value investing Quantamental - value investing Quantamental - value investing Quantamental - value investing")
       st.markdown("Quantamental - value investing Quantamental - value investing Quantamental - value investing")
       st.markdown("Acesse esta estratégia!")
       
       if st.button('Quantamental'):
           mf_url = "window.open('https://www.gustavojannuzziportfolio.com/magic-formula')"
           html = '<img src onerror="{}">'.format(mf_url)
           div = Div(text=html)
           st.bokeh_chart(div)


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
    
# estudos - PAGE #
if selected2 == "Estudos":
    st.title('Estudos')
