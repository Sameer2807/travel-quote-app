import streamlit as st
from datetime import datetime

# ---------- Initialize session state ----------
if "cities" not in st.session_state:
    st.session_state.cities = [{'name': 'Baku', 'nights': 2}]
if "rooms" not in st.session_state:
    st.session_state.rooms = [{'adults': 2, 'children': 0}]

# ---------- Title ----------
st.title("Travel Info Form")
start_date = st.date_input("Select Travel Start Date", datetime.today())

# ---------- City Section ----------
st.subheader("Cities & Nights")
city_options = ["Baku", "Gabala", "Shamakhi", "Sheki", "Shahdag", "Quba"]

# Dynamic city UI
updated_cities = []
for i, city in enumerate(st.session_state.cities):
    col1, col2, col3 = st.columns([3, 1, 0.3])
    with col1:
        selected_city = st.selectbox(f"City {i+1}", city_options, index=city_options.index(city["name"]), key=f"city_{i}")
    with col2:
        nights = st.number_input(f"N_
