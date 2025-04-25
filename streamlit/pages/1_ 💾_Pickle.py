import streamlit as st
import pandas as pd
import pickle

st.sidebar.write("## Nastavite značilke")
sl_slider = st.sidebar.slider(
    'Sepal length (cm)',
    4.0, 9.0, step=0.1,
    value=6.5,format="%0.1f"
)
sw_slider = st.sidebar.slider(
    'Sepal width (cm)',
    1.0, 5.0, step=0.1,
    value=3.0,format="%0.1f"
)
pl_slider = st.sidebar.slider(
    'Petal length (cm)',
    0.5, 8.0, step=0.1,
    value=4.0,format="%0.1f"
)
pw_slider = st.sidebar.slider(
    'Petal width (cm)',
    0.0, 3.5, step=0.1,
    value=1.5,format="%0.1f"
)
new_data = pd.DataFrame([[sl_slider, sw_slider, pl_slider, pw_slider]], columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])

with open("streamlit/pkl/model.pkl", 'rb') as fp:
    model = pickle.load(fp)
prediction = model.predict(new_data)[0]

st.write('# Napoved vrste perunike')
st.write("Ta aplikacija napoveduje vrsto perunike na podlagi značilnosti, ki jih izbere uporabnik z drsniki na levi strani. Model smo že predhodno naučili in ga tu samo naložimo. Če bi aplikacija vsebovala tudi učenje modela, bi se učenje modela zagnalo ob vsakem premiku drsnika.")
st.write("## Izbrane značilnosti:") 
st.write("Dolžina čašnega lista: %.1f cm" % sl_slider)
st.write("Širina čašnega lista: %.1f cm" % sw_slider)
st.write("Dolžina cvetnega lista: %.1f cm" % pl_slider)
st.write("Širina cvetnega lista: %.1f cm" % pw_slider)
st.write("### Napoved")
st.write("Napovedana vrsta perunike: %s" % prediction)