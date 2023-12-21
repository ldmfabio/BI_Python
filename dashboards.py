import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Com uma visão mensal
# Faturamento por unidade
# Tipo de produto mais vendido, contribuição por filial
# Desempenho das formas de pagamento
# Como estão as avaliações das filiais

# Load data
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")

# Transform data
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")
highest_total = df["Total"].max()
lowest_total = df["Total"].min()
average_total = df["Total"].mean()

# Criando grupos para classificar por meses
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Selecione o mês", df["Month"].unique())
gender = st.sidebar.selectbox("Gênero", df["Gender"].unique())
total = st.sidebar.slider("Total da Compra", lowest_total, highest_total, average_total)

# Filtrando os dados
df_filtered = df[
    (df["Month"] == month) &
    (df["Gender"] == gender) &
    (df["Total"] <= total)
]

# Criando um gráfico de barras, definindo quantidade de colunas
# Aqui também já atendeu o segundo gráfico
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Primeiro gráfico - faturamento por dia, filtrado pelo mês selecionado
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

# Terceiro gráfico - Tipo de produto mais vendido, contribuição por filial
fig_product = px.bar(df_filtered, x="Date", y="Product line", color="City", title = "Faturamento por Tipo de Produto", orientation="h")
col2.plotly_chart(fig_product, use_container_width=True)

city_total = df_filtered.groupby("City")["Total"].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por Filial")
col3.plotly_chart(fig_city, use_container_width=True)

# Quarto gráfico - Desempenho das formas de pagamento
fig_kind = px.pie(df_filtered, names="Payment", values="Total", title="Faturamento por Tipo de Pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

# Quinto gráfico - Como estão as avaliações das filiais
city_total = df_filtered.groupby("City")["Rating"].mean().reset_index()
fig_rating = px.bar(df_filtered, x="City", y="Rating", title="Avaliação por Filial")
col5.plotly_chart(fig_rating, use_container_width=True)

df_filtered