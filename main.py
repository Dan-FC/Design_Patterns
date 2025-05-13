import streamlit as st
from api.factory import EndpointFactory
from strategies.display_strategy import TableDisplayStrategy, BarChartDisplayStrategy

st.title("Ligas de Fútbol por País")
country = st.text_input("Escribe un país:", "Mexico")

if country:
    leagues_endpoint = EndpointFactory.create_endpoint("leagues")
    data = leagues_endpoint.get_data(country=country)

    # Mostrar tabla
    table_strategy = TableDisplayStrategy()
    table_strategy.display(data)

# Consulta para varios países
st.markdown("---")
st.subheader("Visualización general de ligas por país")

# Aquí puedes permitir ingresar más de un país
multi_country = st.text_input("Escribe países separados por coma:", "Mexico, Spain, England, Italy")
if multi_country:
    countries = [c.strip() for c in multi_country.split(",")]
    all_data = []
    for c in countries:
        endpoint = EndpointFactory.create_endpoint("leagues")
        all_data.extend(endpoint.get_data(country=c))

    bar_strategy = BarChartDisplayStrategy()
    bar_strategy.display(all_data)
