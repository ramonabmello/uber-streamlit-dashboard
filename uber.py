# import necessary packages
import pandas as pd
import numpy as np
import streamlit as st

DATA_URL = "https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"

@st.cache
def load_data(nrows):
    # alterar nome das colunas
    columns = {"Date/Time": "date",
               "Lat": "lat",
               "Lon": "lon"
               }

    # importar dataframe e limpar os dados
    df = pd.read_csv(DATA_URL, compression="gzip", nrows=nrows)
    df = df.rename(columns=columns)
    df.date = pd.to_datetime(df.date)
    df = df[list(columns.values())]

    return df

# MAIN
st.title("Viagens Uber em NYC")
st.markdown(
    f"""
    Dashboard para análise de viagens Uber
    no mês de **Setembro de 2014**
    na cidade de **Nova York**.
    """
)

# SIDEBAR Filters
st.sidebar.header("Filtros de exibição:")

# N Rows
n = st.sidebar.number_input("Número de linhas para análise:", 0)
df = load_data(n)

# Data
st.subheader("Dados")
if st.sidebar.checkbox("Dados"):
    # imprimir tabela
    st.write(df)

# Map
st.subheader("Mapa")
hora_selecionada = st.empty()
if st.sidebar.checkbox("Mapa"):
    hora = st.sidebar.slider("Horário:", 0, 23, 0)
    df_hour_filtered = df[df.date.dt.hour == hora]
    hora_selecionada.markdown(
        f"""{df_hour_filtered.shape[0]} viagens às {hora} horas.
        """
    )
    st.map(df_hour_filtered)

# Histogram
st.subheader("Histograma")
if st.sidebar.checkbox("Histograma"):
    hist = np.histogram(df.date.dt.hour, bins=24, range=(0, 24))[0]
    st.bar_chart(hist)
