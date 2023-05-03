import streamlit as st
import pickle

st.header("Gold price prediction")
st.title("Project Handled by Balaji")

model= pickle.load(open("gold.pkl","rb"))

#def prediction(input):
#    pre=model.predict(input)

#    return pre
# SPX	USO	SLV	EUR/USD

SPX=st.number_input("SPX")
USO=st.number_input("USO")
SLV=st.number_input("SLV")
USD=st.number_input("USD")


if st.button("Predict"):
    output=model.predict([[SPX,USO,SLV,USD]])
    st.success(output[0])



