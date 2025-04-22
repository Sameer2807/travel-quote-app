import streamlit as st
from datetime import datetime

# ---------- Initialization ----------
if 'cities' not in st.session_state:
    st.session_state.cities = [{'name': 'Baku', 'nights': 2}]
if 'rooms' not in st.session_state:
    st.session_state.rooms = [{'adults': 2, 'children': 0}]

# ---------- Page Title ----------
st.title("Travel Info Form")
start_date = st.date_input("Select Travel Start Date", datetime.today())

# ---------- Cities Section ----------
st.subheader("Cities & Nights")
city_options = ["Baku", "Gabala", "Shamakhi", "Sheki", "Shahdag", "Quba"]

# Track if city was removed
city_to_remove = None

for i, city in enumerate(st.session_state.cities):
    col1, col2, col3 = st.columns([3, 1, 0.3])
    with col1:
        selected = st.selectbox(
    f"City {i+1}", city_options, index=city_options.index(city['name']), key=f"city_{i}"
)

