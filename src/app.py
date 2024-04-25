import streamlit as st
import pandas as pd
import plotly.express as px


#streamlit page config
st.set_page_config(
    page_title="Top 100 Amazon Books Reviews",
    page_icon="📚",
    layout='wide',
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!",
    } #items in 3 point menu top right side
)



df_reviews = pd.read_csv(f"/workspaces/amazon_books/dataset/customer reviews.csv")
df_top100_books = pd.read_csv(f"/workspaces/amazon_books/dataset/Top-100 Trending Books.csv")

price_min = df_top100_books['book price'].min() #slider min value
price_max = df_top100_books['book price'].max() #slider max value

max_price = st.sidebar.slider('Price range', price_min, price_max, price_max) #slider with price data

df_books = df_top100_books[df_top100_books['book price'] <= max_price] #filtering data table with slider
df_books
#plot bar with plotly

fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)

col1.plotly_chart(fig)
col2.plotly_chart(fig2)