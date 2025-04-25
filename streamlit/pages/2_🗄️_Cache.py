import streamlit as st
import pandas as pd

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

@st.cache_data
def filter_data(df, value):
    return df[df['Year'] == value].mean()["Temp"]

df = load_data("https://raw.githubusercontent.com/tomazc/PRvaje/refs/heads/master/notebooks/data/stockholm.csv")

st.title("Predpomnjene podatkov in rezultatov funkcij")
st.write("Podatki se sicer nahajajo [na spletu](https://raw.githubusercontent.com/tomazc/PRvaje/refs/heads/master/notebooks/data/stockholm.csv), a se po prvem klicu funkcije shranijo, kar pomeni, da se ne bodo ponovno naložili ob vsakem osveževanju strani.")
st.dataframe(df)

st.write("Predpomnimo lahko tudi delo na podatkih, npr uporabo različnih filtrov.")
st.write("V spodnjem primeru smo predpomnili povprečje temperature za izbrano leto.")
year = st.selectbox("Izberite leto", df['Year'].unique())
st.write("Povprečna temperatura za leto %i je: %.2f" % (year, filter_data(df, year)))