import streamlit as st
import pandas as pd

df_reviews = pd.read_csv('/home/castro/Desktop/projects/amazon_books/dataset/customer reviews.csv')
df_top100_books = pd.read_csv('/home/castro/Desktop/projects/amazon_books/dataset/Top-100 Trending Books.csv')

books = df_top100_books['book title'].unique()
book = st.sidebar.selectbox("Books", books)

df_book = df_top100_books[df_top100_books['book title'] == book]


df_reviews_f = df_reviews[df_reviews['book name'] == book]


#Top side

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)
col1.metric(label='Price', value=book_price)
col2.metric(label='Rating', value=book_rating)
col3.metric(label='Year of Publication', value=book_year)

st.divider()

for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])