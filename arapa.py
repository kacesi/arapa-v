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
        st.image("https://github.com/kacesi/arapa-v/blob/main/Screenshot_2025-02-26-00-19-46-399_com.whatsapp-edit.jpg")
with col2:
    if st.button("Claro que no","es 100 por ciento hetero"):
        st.error("Di que si mrd waaehh")
        st.image("https://github.com/kacesi/arapa-v/blob/main/IMG_20241015_195427_306.jpg", ":v")




