from abc import ABC, abstractmethod
import pandas as pd
import streamlit as st

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
