import streamlit as st
st.set_page_config(page_title="Privado beibi",page_icon="😎")
st.title("Acceso restringido")
clave_usuario = st.text_input("Introduce la clave jeje:", type ="password")

if clave_usuario == "arapacabro":
    st.success("waaaeh")
# Configuración para que el link se vea oficial en Instagram
    st.set_page_config(page_title="arapa eres el de la foto?", page_icon="😔")

    st.title("Arapa es cabro paletón?")
    st.write("presiona beibe")
#Creamos dos columnas para que los botontes estén uno al lado del otro
    col1, col2 = st.columns(2)

    with col1:
    if st.button("cabrazo","paletón","gordo onicham"):
        st.success("AY QUE RICO UWUWUWUWWU WAAAAAAAEH OEEEH")
        st.image("Arapa 2.jpg")
    with col2:
    if st.button("Claro que no","es 100 por ciento hetero"):
        st.error("Di que si mrd waaehh")
        st.image("arapa 1.jpg", ":v")
if clave_usuario =="":
    st.info("Introduce la clave jeje:")
else:
    st.error("Esa no es la contraseña papu")













