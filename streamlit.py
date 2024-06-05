import streamlit as st
import pandas as pd
import numpy as np
data = pd.read_csv("f111.csv", quoting=1, doublequote=False)
chart_data = {'F.Alonso': 2300, 'V.Bottas': 1797, 'L.Hamilton': 4681, 'C.Sainz': 746, 'S.Perez': 1593, 'D.Ricciardo': 1322, 'C.Lecrec': 1090, 'M.Verstappen': 2755}
#chart_data = pd.DataFrame([2300, 1797, 4681, 746, 1593, 1322, 1090, 2755])

st.bar_chart(chart_data)
st.title("F1 Driver Stats")
st.write('hhhe')
st.dataframe(data)
st.table(data.iloc[0:10])

st.sidebar.title('Drivers') 
st.sidebar.checkbox('Max Verstappen')
st.sidebar.checkbox('Charles Lecrec')
st.sidebar.checkbox('Fernando Alonso')
st.sidebar.checkbox('Lewis Hamilton')
st.sidebar.checkbox('Lando Norris')
st.sidebar.checkbox('Carlos Sainz')