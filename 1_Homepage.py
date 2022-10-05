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
    st.markdown("Os projetos estão separados em estratégias fundamentalista (Value-invest), Especulativa e  Estudo.")
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
           mf_url = "window.open('https://gustavojannuzzi-jgmagicformulab3-streamlitmagicformula-xgzgt5.streamlitapp.com/')"
           html = '<img src onerror="{}">'.format(mf_url)
           div = Div(text=html)
           st.bokeh_chart(div)
          
        

    with col2:
       st.header("Quantamental - value investing")
       st.image("imagens/value_invest.png")
       st.markdown("Investidores normalmente usam uma cesta composta de métricas de avaliação para construir estratégias de valor quantitativas robustas. Nesta estratégia, foram filtradas as ações com os percentis mais baixos nas métricas:P/L, P/VBA ou P/B,  PSR  e EV/EBITDA.")
       st.markdown("Acesse esta estratégia!")
       
       if st.button('Quantamental'):
           mf_url = "window.open('https://gustavojannuzzi-quantamental-app-quantamental-app-3q76yt.streamlitapp.com/')"
           html = '<img src onerror="{}">'.format(mf_url)
           div = Div(text=html)
           st.bokeh_chart(div)


# ESPECULATIVA - PAGE #
if selected2 == "Epeculativa":
    col1, col2, col3 = st.columns(3)
    with col1:
       st.header("Momentum Strategy")
       st.image("imagens/momentum.png")
       st.markdown(" Momentum é um sistema de compra de ações ou outros títulos que tiveram retornos elevados nos últimos três a doze meses e de venda daqueles que tiveram retornos insatisfatórios no mesmo período.")
       st.markdown("Neste projeto foram realizadas duas estratéggias de momentum gernado uma carteira dos 50 melhores ativos no S&P 500")
       st.markdown("Acesse o notebook no Google colab!")
       if st.button('Momentum'):
           #Alterar URL
           mf_url = "window.open('https://colab.research.google.com/drive/1HXg5KOcwrAimwmAx1wge8VSi81LT1JNX#scrollTo=QXDyPofhMP-p')"
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
       st.markdown('Com uma regressão linear aplicada a alguns fatores e movimentações no valore das ações do mercado, foi possível prevere um valor aproximado de fechamento dos ativos.') 
       st.markdown('O Web-app filtra as 50 ações com maior participação no Índice Bovespa, apresenta as estatísticas do modelo gerado para cada e as informações sobre cada ativo')   
       if st.button('Ver valor de fechamento'):
           mf_url = "window.open('https://gustavojannuzzi-top50ibovstocks-linearregr-streamlit-app-l7n4bm.streamlitapp.com/')"
           html = '<img src onerror="{}">'.format(mf_url)
           div = Div(text=html)
           st.bokeh_chart(div)  
    
# estudos - PAGE #
if selected2 == "Estudos":
    st.title('Alocando em carteiras especulativas e fundamentalistas')
    st.image("imagens/estudo.jpg")
    st.markdown("Após escolher quais ativos adotar na carteira surge a pergunta de como combinar esses ativos pra maximizar a relação risco retorno, ou Sharp.")
    st.subheader("Princípio 1 - Inversamente proporcional á correlação")
    st.markdown("Toda alocação em determinado ativo ou estratégia deveria ser inversamente proporcional á correlação que uma estratégia tem, com a outra estratégia que possuo na carteira. Ativos ou estratégias descorrelacionados trazem diversificação para a carteira.")
    st.markdown("Se a correlação de um ativo é muito baixa ou negativa com outro, a alocação deve ser maior para fins de diversificar a carteira.")   
    st.subheader("Princípio 2 - Inversamente proporcional á volatilidade")
    st.markdown("Após verificada a volatilidade de cada estratégia, podemos alocar o capital de acorodo com a proporção contrária a sua volatilidade encontrada.")
    st.markdown("")
    st.subheader("Alocação da carteira")
    st.markdown("Neste estudo de alocação estou usando duas carteiras que foram apresentadas neste web-app, a carteira da Magic Formula do Joel Greenblatt e a uma carteira criada com Momentum Strategy.")
    st.markdown("A carteia gerada com a Magic Formula, aplicou suas métricas de avaliação ao mercado brasileiro e gerou os seguintes ativos: ")
    MagicFormula = pd.read_csv('carteira_magicformula.csv')
    MagicFormula
    
    st.markdown("Sua volatilidade média EWMA em uma janela de 252 dias foi de 2,59%. O gráfico apresenta a volatilidade de cada ativo integrante na carteira.")
    st.image('imagens/volatilidade_mf.png')
    st.markdown("")
    st.markdown("")
    st.markdown("Já a carteira criada com Momentum Strategy na bolsa americana teve uma volatilidade EWMA média de 1,86% no período de 252 dias, sendo composta pelos seguintes ativos:")
    Momentum = pd.read_csv('carteira_momentum.csv')
    Momentum    
    
    st.image('imagens/volatlidade_momentum.png')
    st.markdown("")
    st.markdown("A Correlação entre as duas foi calculada através dos preços históricos dos ativos correspondentes a cada carteira no período de 2 anos. Obviamente, produtos do passado não garantia de ganhos futuros, porém neste caso usei dados históricos para obter as métricas estatísticas favorecendo a alocação na carteira.")
    st.image('imagens/correlacao.png')
    st.markdown("Desta forma, considerando a correlação de 0.235 das carteiras com seus retornos históricos, é possível realizar alocação de forma diversificada.")
    st.markdown("A carteira Momentum Strategy apresentou uma volatilidade 28,1853% menor do que a volatilidade da Magic Formula. Recapitulando, a volatilidade da Magic Formula foi de 2,59 e Momentum foi de 1,86. ")
    st.markdown('No cenário de uma carteira com RS 8 Bilhões sob gestão, como a Giant Steps Capital, seriam alocados RS 2.254.826.254.826,25 na carteira da Magic Formula e RS 5.745.173.600.000,00 na carteira gerada pelo modelo Momentum Strategy.')
    
    st.write("O notebook com os modelos e as avaliações estatísticas estão disponpiveis aqui:[Jupyter Notebook](https://github.com/GustavoJannuzzi/Atiana/blob/main/Estudo%20de%20alocacao%20de%20estrat%C3%A9gias.ipynb)")
    
    st.markdown("")
    st.markdown("")
    st.markdown("**Referências:**")
    st.write("[Volatilidade GARCH(1,1) para carteira com N ativos](https://www.linkedin.com/pulse/volatilidade-garch11-para-carteira-com-n-ativos-python-r-mota/?originalSubdomain=pt)")
    st.write("[Correlação entre Ativos](https://opencodecom.net/post/2021-09-01-correlacao-entre-ativos-no-python/#:~:text=Quando o coeficiente entre duas,as variávies são correlacionáveis negativamente)")
    
    
    
    

    
