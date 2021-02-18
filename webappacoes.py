import streamlit as st
import pandas as pd


# nome da aplicação
st.write(
    """
  ** Ações web app **
  """
)

# Criando uma sidebar

st.sidebar.header('Escolha sua ação')

# ler arquivo de ações


def get_data():
