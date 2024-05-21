import streamlit as st
import pandas as pd
import plotly.express as px

st.write('**APP Futebol**')
st.sidebar.header('Escolha dos times')

df = pd.read_csv('../1_bases_tratadas/dadostratados.csv', sep=';', encoding='utf-8')

times = df['home_team_name'].drop_duplicates()
escolha_time = st.sidebar.selectbox('Escolha um time', times)

df2 = df[df['home_team_name']==escolha_time]

st.write('Pontos do jogo do time mandante')
fig = px.box(df2, x='home_ppg')
st.plotly_chart(fig)