import streamlit as st
from api.factory import EndpointFactory
from strategies.display_strategy import TableDisplayStrategy

st.title("Ligas de Fútbol por País")
country = st.text_input("Escribe un país:", "Mexico")

if country:
    leagues_endpoint = EndpointFactory.create_endpoint("leagues")
    data = leagues_endpoint.get_data(country=country)

    strategy = TableDisplayStrategy()
    strategy.display(data)
