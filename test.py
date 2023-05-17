import streamlit as st
st.set_page_config(layout="wide")

import pandas as pd
data = pd.read_csv('platten.csv')

# Create a Streamlit map plot
st.title('Hallo Nömselchen, wo spielen wir bald mal?')
st.write('mfg nmb')
st.map(data)
