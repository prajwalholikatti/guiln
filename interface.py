import streamlit as st
import pandas as pd
import VALUES


st.set_page_config(
    page_title="Stock Comparison Dashboard",
    layout="wide"
)

st.title("📈 Stock Comparison Dashboard")

company1 = st.text_input("Company 1")
company2 = st.text_input("Company 2")

if st.button("Compare"):

    df = VALUES.get_data(company1, company2)



    try:
        st.dataframe(df)
        st.success("Dataframe rendered successfully")
    except Exception as e:
        st.error(str(e))