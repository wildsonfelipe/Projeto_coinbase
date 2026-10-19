import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(
    page_title="Dashboard de Criptomoedas",
    layout="wide"
)
st.markdown(
    "<h1 style='color: #1E88E5;'>Dashboard de Criptomoedas</h1>",
    unsafe_allow_html=True
)

st.write("Visualização dos dados coletados da API da Coinbase")

@st.cache_data(ttl=60)

# Conexão com o banco
def carregar_dados():
    conexao = sqlite3.connect("coinbase5.db")
    try: 
        df = pd.read_sql_query("SELECT moeda, preco, data_hora FROM precos ORDER BY data_hora",
                               conexao,)
    finally:
        conexao.close()
    df["dat_hora"] = pd.to_datetime(df["data_hora"])
    df["preco"] = pd.to_numeric(df["preco"], errors="coerce")

    return df


# Carregar os dados do banco

try:
    df = carregar_dados()
except Exception as erro:
    st.error(f"Não foi possível ler o banco de dados: {erro}")
    st.stop()
if df.empty:
    st.warning("Ainda não existem dados no banco.")
    st.stop()

#-------------------------------------- A partir dessa linha começa a parte de visualização.

moedas = df["moeda"].unique()
for coluna, moeda in zip(st.columns(len(moedas)), moedas):
    precos = df.loc[df["moeda"]== moeda,"preco"]

    atual = precos.iloc[-1]
    anterior = precos.iloc[-2] if len(precos) > 1 else  None
    delta = f"{atual - anterior:,.2f}" if anterior is not None else None

    with coluna:
        st.metric(moeda, f"${atual:,.2f}", delta=delta)
        st.write(f"Maior preco: ${precos.max():,.2f}")
        st.write(f"Menor preco: ${precos.min():,.2f}")

st.divider()

moeda_selecionada = st.selectbox("Selecione a Cryptomoeda desejada para análise", moedas)
dados_moeda=df[df["moeda"]== moeda_selecionada]

# Exibir os dados
st.subheader(f"Histórico de preços - {moeda_selecionada}")
st.line_chart(dados_moeda.set_index("data_hora")["preco"])
#st.dataframe(df,use_container_width=True)
