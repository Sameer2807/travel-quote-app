import streamlit as st
from datetime import datetime

# ---------- Initialization ----------
if 'cities' not in st.session_state:
    st.session_state.cities = [{'name': 'Baku', 'nights': 2}]
if 'city_to_remove' not in st.session_state:
    st.session_state.city_to_remove = None
if 'rooms' not in st.session_state:
    st.session_state.rooms = [{'adults': 2, 'children': 0}]
if 'room_to_remove' not in st.session_state:
    st.session_state.room_to_remove = None

# ---------- Page Title ----------
st.title("Travel Info Form")
start_date = st.date_input("Select Travel Start Date", datetime.today())

# ---------- Cities Section ----------
st.subheader("Cities & Nights")
city_options = ["Baku", "Gabala", "Shamakhi", "Sheki", "Shahdag", "Quba"]

for i, city in enumerate(st.session_state.cities):
    col1, col2, col3 = st.columns([3, 1, 0.3])
    with col1:
        st.session_state.cities[i]['name'] = st.selectbox(
            f"City {i+1}", city_options, index=city_options.index(city['name']), key=f"city_{i}"
        )
    with col2:
        st.session_state.cities[i]['nights'] = st.number_input(
            f"Nights in {city['name']}", min_value=1, value=city['nights'], key=f"nights_{i}"
        )
    with col3:
        if i > 0:
            if st.button("❌", key=f"remove_city_{i}"):
                st.session_state.city_to_remove = i

# ---------- Remove City ----------
if st.session_state.city_to_remove is not None:
    st.session_state.cities.pop(st.session_state.city_to_remove)
    st.session_state.city_to_remove = None
    st.experimental_rerun()

# ---------- Add City ----------
if st.button("Add City"):
    st.session_state.cities.append({'name': 'Baku', 'nights': 1})

# ---------- Geography Validation ----------
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

# ---------- Rooms Section ----------
st.subheader("Room Configuration")

for i, room in enumerate(st.session_state.rooms):
    col1, col2, col3 = st.columns([1, 1, 0.3])
    with col1:
        st.session_state.rooms[i]['adults'] = st.number_input(
            f"Adults (Room {i+1})", min_value=1, value=room['adults'], key=f"adults_{i}"
        )
    with col2:
        st.session_state.rooms[i]['children'] = st.number_input(
            f"Children (Room {i+1})", min_value=0, value=room['children'], key=f"children_{i}"
        )
    with col3:
        if i > 0:
            if st.button("❌", key=f"remove_room_{i}"):
                st.session_state.room_to_remove = i

# ---------- Remove Room ----------
if st.session_state.room_to_remove is not None:
    st.session_state.rooms.pop(st.session_state.room_to_remove)
    st.session_state.room_to_remove = None
    st.experimental_rerun()

# ---------- Add Room ----------
if st.button("Add Room"):
    st.session_state.rooms.append({'adults': 2, 'children': 0})

# ---------- Pax Summary ----------
total_adults = sum(room['adults'] for room in st.session_state.rooms)
total_children = sum(room['children'] for room in st.session_state.rooms)
total_pax = total_adults + total_children

st.markdown(f"**Total Pax:** {total_pax} (Adults: {total_adults}, Children: {total_children})")

# ---------- Next Button ----------
st.markdown("---")
if st.button("Next"):
    st.success("Proceeding to the next step...")
