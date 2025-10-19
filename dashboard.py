import streamlit as st
import pandas as pd
import plotly.express as px

# Load cleaned data
df = pd.read_csv("data/processed/netflix_clean.csv")
df_exploded_genre = pd.read_csv("data/processed/netflix_clean_genre.csv")
df_exploded_country = df.assign(country=df['country']).explode('country')
df_exploded_country['country'] = df_exploded_country['country'].str.strip()

# Title
st.title("Netflix EDA Dashboard")

# Sidebar filters
content_type = st.sidebar.multiselect("Select Type", df['type'].unique(), default=df['type'].unique())
year_range = st.sidebar.slider("Select Year Range", int(df['year_added'].min()), int(df['year_added'].max()), (2010, 2023))

# Filter data
df_filtered = df[(df['type'].isin(content_type)) & (df['year_added'] >= year_range[0]) & (df['year_added'] <= year_range[1])]

# Plot: Movies vs TV Shows
fig1 = px.histogram(df_filtered, x="type", title="Movies vs TV Shows")
st.plotly_chart(fig1)

# Plot: Top Genres
top_genres = df_exploded_genre['genre'].value_counts().head(10)
fig2 = px.bar(x=top_genres.index, y=top_genres.values, title="Top 10 Genres")
st.plotly_chart(fig2)

# Plot: Top Countries
top_countries = df_exploded_country['country'].value_counts().head(10)
fig3 = px.bar(x=top_countries.index, y=top_countries.values, title="Top 10 Countries")
st.plotly_chart(fig3)
