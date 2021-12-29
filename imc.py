import streamlit as st

st.title('Descubra o seu IMC!')
altura = st.slider('Altura',0.,2.,1.,0.01)
peso = st.number_input('Peso',0,100,50,1)

imc = peso/altura**2

delta = 0
if imc < 18.5:
    delta = imc-18.5
elif imc >= 25:
    delta = 25-imc

st.metric('imc', f'{imc:.2f}', f'{delta:.2f}')


