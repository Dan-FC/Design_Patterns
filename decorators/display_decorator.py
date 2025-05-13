from strategies.display_strategy import DisplayStrategy
import pandas as pd
import streamlit as st

# Decorador base
class DisplayDecorator(DisplayStrategy):
    def __init__(self, display_strategy):
        self._display_strategy = display_strategy

    def display(self, data):
        self._display_strategy.display(data)

# Decorador para exportar a Excel
class ExcelExportDecorator(DisplayDecorator):
    def display(self, data):
        super().display(data)
        if data:
            df = pd.DataFrame([
                {
                    "Nombre": league["league"]["name"],
                    "Temporada actual": league["seasons"][-1]["year"],
                    "Tipo": league["league"]["type"]
                } for league in data
            ])
            st.download_button("📥 Descargar como Excel", df.to_csv(index=False).encode('utf-8'), file_name="ligas.csv", mime='text/csv')
