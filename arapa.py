import streamlit as st

# Configuración para que el link se vea oficial en Instagram
st.set_page_config(page_title="arapa eres el de la foto?", page_icon="😔")

st.title("Arapa es cabro paletón?")
st.write("presiona beibe")
#Creamos dos columnas para que los botontes estén uno al lado del otro
col1, col2 = st.columns(2)

with col1:
    if st.button("cabrazo","paletón","gordo onicham"):
        st.success("AY QUE RICO UWUWUWUWWU WAAAAAAAEH OEEEH")
        st.image("arapa2.jpg")
with col2:
    if st.button("Claro que no","es 100 por ciento hetero"):
        st.error("Di que si mrd waaehh")
        st.image("arapa1.jpg", ":v")





