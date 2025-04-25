import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data(url):
    data = pd.read_csv(url, skiprows=[1], sep="\t")
    medals_by_country = data[['country', 'gold_medals', 'silver_medals', 'bronze_medals']].groupby('country').sum()
    medals_by_country['total_medals'] = medals_by_country['gold_medals'] + medals_by_country['silver_medals'] + medals_by_country['bronze_medals']
    medals_by_country = medals_by_country.sort_values('total_medals', ascending=False)
    medals_by_country = medals_by_country[medals_by_country['total_medals'] > 0]
    medals_by_country = medals_by_country.drop(columns=['total_medals'])
    return data, medals_by_country
data, medals_by_country = load_data("https://raw.githubusercontent.com/tomazc/PRvaje/refs/heads/master/notebooks/data/athletes.tab")

st.write("# Vizualizacija podatkov")
st.write("Na podatkih, ki smo jih uporabljali na vajah, si bomo ogledali nekaj primerov vizualizacije podatkov.")

st.write("Streamlit že vsebuje nekaj funkcij za izris podatkov. Spodaj je primer izrisa podatkov s pomočjo funkcije `st.bar_chart`.")
st.bar_chart(medals_by_country, color=["#CD7F32",  "#FFDF00", "#C0C0C0"] )


st.write("Vendar pa je včasih potrebno uporabiti bolj napredne funkcije za izris podatkov. Takrat lahko uporabimo matplotlib za vizualizacijo podatkov.")
plt.figure()
x = data['height']
y = data['weight']
plt.plot(x, y, "k.")
plt.xlabel('višina (m)')
plt.ylabel('teža (kg)')
st.pyplot(plt)