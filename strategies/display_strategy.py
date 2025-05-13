from abc import ABC, abstractmethod
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, data):
        pass

class TableDisplayStrategy(DisplayStrategy):
    def display(self, data):
        if not data:
            st.warning("No se encontraron ligas para este país.")
            return
        df = pd.DataFrame([
            {
                "Nombre": league["league"]["name"],
                "Temporada actual": league["seasons"][-1]["year"],
                "Tipo": league["league"]["type"]
            } for league in data
        ])
        st.dataframe(df)

class BarChartDisplayStrategy(DisplayStrategy):
    def display(self, data):
        if not data:
            st.warning("No hay datos para mostrar en la gráfica.")
            return

        # Contar cuántas ligas hay por país
        country_counts = {}
        for league in data:
            country = league["country"]["name"]
            country_counts[country] = country_counts.get(country, 0) + 1

        # Seleccionar países a mostrar
        selected_countries = st.multiselect(
            "Selecciona los países a mostrar en la gráfica:",
            options=sorted(country_counts.keys()),
            default=list(country_counts.keys())
        )

        filtered_counts = {k: v for k, v in country_counts.items() if k in selected_countries}

        if not filtered_counts:
            st.info("Selecciona al menos un país para mostrar la gráfica.")
            return

         # Mostrar la gráfica con estilo oscuro
        fig, ax = plt.subplots(figsize=(8, 4), facecolor='black')  # ancho=8, alto=4
        ax.set_facecolor('black')  # Fondo del área de la gráfica

        bars = ax.bar(filtered_counts.keys(), filtered_counts.values(), color='white')  # Barras blancas
        ax.set_title("Cantidad de ligas por país", color='white')
        ax.set_ylabel("Número de ligas", color='white')
        ax.set_xlabel("País", color='white')

        ax.tick_params(colors='white')  # Colores de los ticks del eje
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')

        plt.xticks(rotation=45, color='white')
        plt.yticks(color='white')

        st.pyplot(fig)
