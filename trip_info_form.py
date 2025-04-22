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

updated_cities = []
for i, city in enumerate(st.session_state.cities):
    col1, col2, col3 = st.columns([3, 1, 0.3])
    with col1:
        selected_city = st.selectbox(
            f"City {i+1}", city_options, index=city_options.index(city["name"]), key=f"city_{i}"
        )
    with col2:
        nights = st.number_input(
            f"Nights in {selected_city}", min_value=1, value=city["nights"], key=f"nights_{i}"
        )
    with col3:
        remove = False
        if i > 0:
            remove = st.button("❌", key=f"remove_city_{i}")
        if not remove:
            updated_cities.append({'name': selected_city, 'nights': nights})

if st.button("Add City"):
    updated_cities.append({'name': 'Baku', 'nights': 1})

st.session_state.cities = updated_cities

# ---------- Transfer validation ----------
def is_invalid_route(cities):
    for i in range(1, len(cities)):
        cur = cities[i]['name']
        prev = cities[i - 1]['name']
        if (cur in ["Shahdag", "Quba"] and prev in ["Gabala", "Shamakhi", "Sheki"]) or \
           (prev in ["Shahdag", "Quba"] and cur in ["Gabala", "Shamakhi", "
