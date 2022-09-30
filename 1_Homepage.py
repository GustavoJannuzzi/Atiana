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
    st.title("Olá!")
    st.subheader("Para Giant Steps Capital")
    st.markdown("Através dessa aplicação eu gostaria de demonstrar meu interesse em aprender e contribuir com esta gigante fábrica de teses.")
    st.markdown("Aqui apresento alguns de meus projetos desenvolvidos sempre buscando criatividade alida a um breve conhecimento técnico.")
    st.markdown("Atualmente trabalho na Accenture como junior Application Developer. No início da minha carreira nesta empresa, passei por vários desafios, aprendi novas tecnologias, contribui para o desenvolvimento de projetos em empresas de telecomunicações e tive a oportunidade de me desenvolver pessoalmente com uma cultura que abraça a diversidade.")
    st.markdown("Apesar de morar em Curitiba-PR, teria o enorme prazer de passar minhas férias contribuindo e desenvolvendo minhas habilidades em um dos melhores fundos do Brasil. ")
    st.markdown("Aprecio a consideração de analisar este portfolio que fiz especialmente para esta oportunidade Gigante de summer job.")
    st.markdown("Os projetos estão separados em estratégias fundamentalisata(Value-invest), Especulativa e  Estudo.")
    st.markdown("Caso se interessem em acessar, tenho um portfólio pessoal de Data Science/Analysis. ")
    
    if st.button('Acessar Portfólio'):
        mf_url = "window.open('https://www.gustavojannuzziportfolio.com/')"
        html = '<img src onerror="{}">'.format(mf_url)
        div = Div(text=html)
        st.bokeh_chart(div)
        
    st.markdown("") #espaços para rodapé
    st.markdown("") #espaços para rodapé
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("[LinkedIn](https://www.linkedin.com/in/gustavo-jannuzzi-a74901196/)")
    with col2:
        st.write("[Medium](https://medium.com/@gustavojannuzzi)")
    with col3:
        st.write("Telefone: (45)99123-2009")
                 
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
       if st.button('Momentum'):
           #Alterar URL
           mf_url = "window.open('https://gustavojannuzzi-top50ibovstocks-linearregr-streamlit-app-l7n4bm.streamlitapp.com/')"
           html = '<img src onerror="{}">'.format(mf_url)
           div = Div(text=html)
           st.bokeh_chart(div)              


    with col2:
       st.header("Notícias, NLP e O Mercado")
       st.image("imagens/news_sent_anal.png")
       st.markdown('Benjamin Graham, autor do Investidor Inteligente, introduz o "Sr. Mercado" como um persongem muito racional a longo prazo, porém no curto prazo ele tende a ser muito sensível e volátil com divulgação de notícias.')
       st.markdown('Com SentimentIntensityAnalyzer foi possível criar uma breve visualização dos sentimentos do "Sr. Mercado" no momento.')   
       st.markdown("Acesse esta estratégia!")
       if st.button('Análise de sentimento'):
           mf_url = "window.open('https://gustavojannuzzi-giant-news-sentiment--sentiment-analysis-bq2cy8.streamlitapp.com/')"
           html = '<img src onerror="{}">'.format(mf_url)
           div = Div(text=html)
           st.bokeh_chart(div)        

    with col3:
       st.header("L.R. 50 ações do IBOV")
       st.image("imagens/top50_ibov_lin_reg.png")
       if st.button('Ver valor de fechamento'):
           mf_url = "window.open('https://gustavojannuzzi-top50ibovstocks-linearregr-streamlit-app-l7n4bm.streamlitapp.com/')"
           html = '<img src onerror="{}">'.format(mf_url)
           div = Div(text=html)
           st.bokeh_chart(div)  
    
# estudos - PAGE #
if selected2 == "Estudos":
    st.title('Estudos')
    st.image("imagens/estudo.jpg")
    st.markdown("Após escolher quais ativos adotar na carteira surge a pergunta de como combinar esses ativos pra maximizar a relação risco retorno, ou Sharp.")
    st.video("https://www.youtube.com/watch?v=leSqma5s7nE&t=173s")
    
