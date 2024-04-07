import streamlit as st

# Import des fonctions IA depuis le sous-répertoire

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)