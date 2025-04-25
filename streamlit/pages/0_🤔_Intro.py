import streamlit as st
from datetime import datetime

st.write("Za začetek vnesi ime. Ostali deli strani bodo do takrat ostali skriti.")
name = st.text_input("Vnesi ime", key="name")
if name:
    st.write(f'Živijo, {name}!')
    st.write('V nadaljevanju si bomo ogledal nekaj primerov uporabe Streamlita.')

    st.write('Za začetek bomo pogledali vgrajen koledar. Na podlagi vnosa bomo izračunali starost.')
    birthdate = st.date_input("Izberi datum rojstva:", min_value=datetime(1900, 1, 1), max_value="today")
    today = datetime.now().date()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    if birthdate!=today:
        st.write(f"Imaš {age} let.")