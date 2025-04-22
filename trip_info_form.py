import streamlit as st
from datetime import datetime

# ---------- Setup Session State ----------
if 'cities' not in st.session_state:
    st.session_state.cities = [{'name': 'Baku', 'nights': 2}]
if 'rooms' not in st.session_state:
    st.session_state.rooms = [{'adults': 2, 'children': 0}]

# ---------- Action Triggers ----------
def add_city():
    st.session_state.cities.append({'name': 'Baku', 'nights': 1})

def remove_city(index):
    st.session_state.cities.pop(index)

def add_room():
    st.session_state.rooms.append({'adults': 2, 'children': 0})

def remove_room(index):
    st.session_state.rooms.pop(index)

# ---------- Title ----------
st.title("Travel Info Form")
start_date = st.date_input("Select Travel Start Date", datetime.today())

# ---------- Cities ----------
st.subheader("Cities & Nights")
city_options = ["Baku", "Gabala", "Shamakhi", "Sheki", "Shahdag", "Quba"]

for i, city in enumerate(st.session_state.cities):
    col1, col2, col3 = st.columns([3, 1, 0.3])
    with col1:
        selected = st.selectbox(
            f"City {i+1}", city_options, index=city_options.index(city['name']), key=f"city_{i}"
        )
        st.session_state.cities[i]['name'] = selected
    with col2:
        nights = st.number_input(
            f"Nights in {selected}", min_value=1, value=city['nights'], key=f"nights_{i}"
        )
        st.session_state.cities[i]['nights'] = nights
    with col3:
        if i > 0:
            if st.button("❌", key=f"remove_city_{i}"):
                remove_city(i)
                st.experimental_rerun()

# Add City
if st.button("Add City"):
    add_city()
    st.experimental_rerun()

# ---------- Validation ----------
def check_transfer_rule(cities):
    for i in range(1, len(cities)):
        current = cities[i]['name']
        prev = cities[i - 1]['name']
        if (current in ["Shahdag", "Quba"] and prev in ["Gabala", "Shamakhi", "Sheki"]) or \
           (prev in ["Shahdag", "Quba"] and current in ["Gabala", "Shamakhi", "Sheki"]):
            return True
    return False

if check_transfer_rule(st.session_state.cities):
    st.warning("❗ Direct transfer between Shahdag/Quba and Gabala/Shamakhi/Sheki is not possible. Please take at least one night stay in Baku.")

# ---------- Rooms ----------
st.subheader("Room Configuration")

for i, room in enumerate(st.session_state.rooms):
    col1, col2, col3 = st.columns([1, 1, 0.3])
    with col1:
        adults = st.number_input(
            f"Adults (Room {i+1})", min_value=1, value=room['adults'], key=f"adults_{i}"
        )
        st.session_state.rooms[i]['adults'] = adults
    with col2:
        children = st.number_input(
            f"Children (Room {i+1})", min_value=0, value=room['children'], key=f"children_{i}"
        )
        st.session_state.rooms[i]['children'] = children
    with col3:
        if i > 0:
            if st.button("❌", key=f"remove_room_{i}"):
                remove_room(i)
                st.experimental_rerun()

# Add Room
if st.button("Add Room"):
    add_room()
    st.experimental_rerun()

# ---------- Pax Summary ----------
total_adults = sum(room['adults'] for room in st.session_state.rooms)
total_children = sum(room['children'] for room in st.session_state.rooms)
total_pax = total_adults + total_children
st.markdown(f"**Total Pax:** {total_pax} (Adults: {total_adults}, Children: {total_children})")

# ---------- Continue ----------
st.markdown("---")
if st.button("Next"):
    st.success("Proceeding to the next step...")
