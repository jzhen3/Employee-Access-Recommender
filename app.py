import streamlit as st
import prediction
from viz import show_viz

page =  st.sidebar.selectbox("Select Features", ('Query', 'Assessment'))
show_viz() if page == 'Query' else prediction.show_prediction()