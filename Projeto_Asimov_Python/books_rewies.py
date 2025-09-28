import pandas as pd
import streamlit as st

st.set_page_config(page_icon=":book:", layout="wide")

df_reviews = pd.read_csv("customer reviews.csv")
df_top100books = pd.read_csv("Top-100 Trending Books.csv")

books = df_top100books["book title"].unique()
book = st.sidebar.selectbox("Books", books)


df_book = df_top100books[df_top100books['book title'] == book]
df_book

df_review = df_reviews[df_reviews['book name'] == book]
df_review   

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = df_book["book price"].iloc[0]
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)

col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)              