import streamlit

from mpdule14.bar_chart import filterd_df

with col1:
    streamlit.subheader("top 10 book titles")
    top_titles = filterd_books_df['name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    streamlit.subheader("top 10 authors")
    top_titles = filterd_books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

    st.subheader("genre ")


st.subheader("top 15 authors by counts of books published (2009-2022)")
top_authors = filterd_books)_df['author'].value.countes().head(15).rest_index|()
top_authors.columns = ['author' , 'count']


