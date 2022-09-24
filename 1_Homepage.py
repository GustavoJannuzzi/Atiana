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
    ##################
    # MAGIC FORMULA
    ##################

    # função para converter valores percentuais para valores decimais
    def convert_perc(value):
        return pd.to_numeric(value.replace('%','').replace('.', '').replace(',', '.'))

    # mapeando colunas que possuem valores percentuais
    convs = {5: convert_perc, 12: convert_perc, 13: convert_perc, 15: convert_perc, 16: convert_perc, 20: convert_perc}

    url = 'http://fundamentus.com.br/resultado.php'
    agent = {"User-Agent":"Mozzila/5.0"}
    resposta = requests.get(url, headers = agent)
    soup = BeautifulSoup(resposta.text, 'lxml')
    tabela = soup.find_all('table')[0]
    df = pd.read_html(str(tabela), decimal = ',', thousands='.', converters=convs)[0]
    #df = pd.read_html(str(tabela), decimal = ',', thousands='.',index_col='Papel', converters=convs)[0]

    fundamentus = df

    # empresas que possuem alguma liquidez
    fundamentus = fundamentus[fundamentus['Liq.2meses'] > 1000000]

    # com retornos positivos
    fundamentus = fundamentus[fundamentus['ROIC'] > 0]
    fundamentus = fundamentus[fundamentus['EV/EBIT'] > 0]

    #Maiorliquidez
    fundamentus = fundamentus[fundamentus['Patrim. Líq'] > 0]

    fundamentusNovo = fundamentus[['Papel', 'ROIC','EV/EBIT','P/L']]

    EvOrdenado = fundamentusNovo.sort_values(by = 'EV/EBIT')
    EvOrdenado = EvOrdenado.reset_index(drop = True)
    EvOrdenado['EvOrdenado'] = EvOrdenado.index

    roicOrdenado = EvOrdenado.sort_values(by = 'ROIC', ascending = False)
    roicOrdenado = roicOrdenado.reset_index(drop = True)
    roicOrdenado['ROICOrdenado'] = roicOrdenado.index
    dados = roicOrdenado

    dados['score'] = dados['EvOrdenado'] + dados['ROICOrdenado']
    dados.sort_values(by = 'score')

    dados['Papel'] = dados['Papel'] +'.SA'

    stockSectorDF = 'https://raw.githubusercontent.com/GustavoJannuzzi/JGMagicFormulaB3/main/StockSector.csv'
    stockSectorDF = pd.read_csv(stockSectorDF)
    del stockSectorDF['Unnamed: 0']

    dadosNovos = pd.merge(dados, stockSectorDF, on ='Papel', how='inner')

    #Excluir setores 
    filtroSetores = dadosNovos[dadosNovos['sector'] != 'Financial Services']
    filtroSetores = filtroSetores[filtroSetores['sector'] != 'Energy']
    filtroSetores = filtroSetores[filtroSetores['sector'] != 'Utilities']
    filtroSetores = filtroSetores[filtroSetores['sector'] != 'NA']

    # Ranking da Magic Formula
    # MagicWallet = filtroSetores.sort_values(by = 'score').head(QtdStocks)


    ################
    #  STREAMLIT
    ################


    st.title("Magic Formula - B3")

    st.markdown("Joel Greenblatt é um dos investidores mais bem sucedido de todos os tempos e seu modelo de negócio é prestigiado por todo o setor. O executivo é criador do Gotham Capital, um fundo de investimento hedge. Joel esteve à frente do negócio por mais de duas décadas.")

    st.markdown('Para o segundo elemento-chave da estratégia de Buffett, <br> Greenblatt utilizou um múltiplo chamado de earning yield, muito similar ao inverso do popular P/L.Mais uma vez, ele preferiu utilizar o “Ebit” em detrimento do “lucro”, <br> á que o lucro líquido é muito influenciado pela estrutura de capital escolhida por cada empresa. <br> E, em vez de utilizar o “Patrimônio Líquido” no denominador, Greenblatt opta por um múltiplo chamado de Total Enterprise Value (TEV). O TEV indica, basicamente, qual seria o custo que alguém teria que arcar para adquirir a empresa inteira. Ou seja: ele é a soma do valor de mercado da empresa com seu endividamento líquido (a diferença entre a dívida total e o dinheiro em caixa). Por fim, ele batiza esta relação entre EBIT e TEV (EBIT/TEV) de Earnings Yield (EY). EY = Ebit/Tev Com esta composição, a fórmula mágica de Greenblatt nos permite comparar ações com diferentes estruturas de capital e de diferentes setores.'
    ) 

    QtdStocks = st.slider('How many stocks?',10,50,20,10)
    # Ranking da Magic Formula
    MagicWallet = filtroSetores.sort_values(by = 'score').head(QtdStocks)

    Clickerd = st.button("RUN THE MAGIC")
    st.title("Magic Formula - B3")

    if Clickerd:
        st.dataframe(MagicWallet)

# ESPECULATIVA - PAGE #
if selected2 == "Epeculativa":
    # Aplicão de regressão linear das ações que compoem o índice bovespa

    # import libraries
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn import linear_model
    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import r2_score
    import requests
    from bs4 import BeautifulSoup
    import yfinance as yf
    import streamlit as st
    import datetime


    # Web scraping ações do B3 do IBOV
    # https://colab.research.google.com/drive/11uYskZLbH2Y8MuSYHCPJPakY31tXMiwB?usp=sharing#scrollTo=I7cBkX2f29tf
    def busca_carteira_teorica(indice):
      url = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice={}&idioma=pt-br'.format(indice.upper())
      return pd.read_html(url, decimal=',', thousands='.')[0][:-1]

    ibov = busca_carteira_teorica('ibov')
    ibov_ordenado = ibov.sort_values('Part. (%)', ascending=False)
    top50_ibov = ibov_ordenado.head(50)
    top50_ibov = top50_ibov['Código'] + '.SA'
    top50_ibov = top50_ibov.tolist()

    # STREAMLIT
    st.title("Predição das TOP 50 ações do IBOV")

    ticker = st.selectbox('Escolha um ativo', top50_ibov)


    ######################
    ### LINEAR GRESSION 01


    # Stock data 
    df = yf.download(ticker, period = '5y', interval = '1d')
    df['day_prev_close'] = df['Close'].shift(-1)

    #limpa as colunas que eu não preciso
    df = df.drop(columns =['High', 'Low','Adj Close', 'Volume', 'Open'])

    # função para veririficar se o ultimo dia subiu ou caiu 
    def f (row):
        if row ['day_prev_close'] > row['Close']: 
            val = 1
        else:
            val = -1
        return val

    # Criando coluna de trend days
    df['trend_3_day'] = df.apply(f, axis=1)
    df = df.reset_index()
    df = df.dropna()


    #Separando as features do modelo
    features = ['day_prev_close', 'trend_3_day']
    target = 'Close'

    X_train, X_test = df.loc[:600, features], df.loc[600:, features]
    y_train, y_test = df.loc[:600, target], df.loc[600:, target]

    # Create linear regression object
    regr = linear_model.LinearRegression(fit_intercept=False)

    # Train the model using the training set
    regr.fit(X_train, y_train)

    # Make predictions using the testing set
    y_pred = regr.predict(X_test)



    # The mean squared error
    st.write('Root Mean Squared Error: {0:.2f}'.format(np.sqrt(mean_squared_error(y_test, y_pred))))

    'Explained variance score: 1 is perfect prediction'
    st.write('Variance Score: {0:.2f}'.format(r2_score(y_test, y_pred)))

    print('Root Mean Squared Error: {0:.2f}'.format(np.sqrt(mean_squared_error(y_test, X_test.day_prev_close))))


    ### TODAYS PREDICTION ###

    df_today = df.tail(1)

    #previsão de fechamento da ação pra hoje
    features = ['day_prev_close', 'trend_3_day']
    X_test = df_today[features]
    today_pred = regr.predict(X_test)

    # Valor de previsão de fechamento HOJE - tratando dado
    today_pred = ' '.join(str(e) for e in today_pred)
    today_pred = float(today_pred)


    #print valor de fechamento ontem 

    # Valor de fhcamento ontem - tratando dado 
    df_today = df_today['Close'].values.astype(str)
    df_today = ' '.join(str(e) for e in df_today)
    yestday_close = float(df_today)

    percent_change_today = ((today_pred - yestday_close)/yestday_close) *100

    percent_change_today = str(percent_change_today)+'%'

    if today_pred < yestday_close:
        st.error('Looks like today is not a good day for')
    else:
        st.success('Today tends to be a good Day for')

    st.metric(label="Predição do valor de fechamento HOJE", value=today_pred, delta= percent_change_today )


    st.write('Valor de fechamento de ontem', yestday_close)






    ###########################
    ### STOCK INFORMATIONN ####

    st.write('---')
    col1,col2 = st.columns(2)
    with col1:
        # Sidebar
        st.subheader('Query parameters')
        start_date = st.date_input("Start date", datetime.date(2022, 1, 1))
        end_date = st.date_input("End date", datetime.date(2022, 1, 31))

    with col2: 
        # Retrieving tickers data
       #tickerSymbol = st.selectbox('Stock ticker', top50_ibov) # Select ticker symbol
        tickerData = yf.Ticker(ticker) # Get ticker data
        tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker
        # Ticker data
        st.header('**Ticker data**')
        st.write(tickerDf)

    # Ticker information
    string_logo = '<img src=%s>' % tickerData.info['logo_url']
    st.markdown(string_logo, unsafe_allow_html=True)

    string_name = tickerData.info['longName']
    st.header('**%s**' % string_name)

    string_summary = tickerData.info['longBusinessSummary']
    st.info(string_summary)

    # Bollinger bands
    st.header('**Bollinger Bands**')
    qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
    qf.add_bollinger_bands()
    fig = qf.iplot(asFigure=True)
    st.plotly_chart(fig)
    
# VALUE-INVEST - PAGE #
if selected2 == "Estudos":
    st.title('Estudos')
