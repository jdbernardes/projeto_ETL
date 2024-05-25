import streamlit as st
import pandas as pd
import sqlite3

#Connectar no DB
db_path = '..\data\ml.db'
conn = sqlite3.connect(db_path)

# Carregar dados da tabela em um DF
df = pd.read_sql_query('SELECT * FROM mercadolivre_items', conn)

#Fechar Conexão
conn.close()

#Titulo da Aplicação
st.title('Pesquisa de Mercado - Tênis Esportivos no Mercado Livre')

#Subheader and DF
st.subheader('KPIs Principais')
#st.dataframe(df)

#Set Collumns
col1, col2, col3 = st.columns(3)

#KPI1
total_itens = df.shape[0]
col1.metric(label="Numero Total de Itens", value=total_itens)

#KPI2
unique_brands = df['brand'].nunique()
col2.metric(label="Numero Marcas Unicas", value=unique_brands)

#KPI3
avg_new_price = df['new_price'].mean()
col3.metric(label="Media dos preços", value=round(avg_new_price, 2))

#KPI4
st.subheader('Marcas mais encontradas')
col1, col2 = st.columns([4,2])
top_10 = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10) 
col2.write(top_10)

#KPI4
st.subheader('Preço medio por marca')
col1, col2 = st.columns([4,2])
df_non_zero_prices = df[df['new_price']>0]
avg_price_per_brand = df_non_zero_prices.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(avg_price_per_brand) 
col2.write(avg_price_per_brand)


#KPI5
st.subheader('Satisfação por marca')
col1, col2 = st.columns([4,2])
df_non_zero_reviews = df[df['reviews_rating_number']>0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand) 
col2.write(satisfaction_by_brand)