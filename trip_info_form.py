import streamlit as st
from datetime import datetime

def show_trip_info_form():
    st.title("Travel Info Form")
    start_date = st.date_input("Select Travel Start Date", datetime.today())

    if "cities" not in st.session_state:
        st.session_state.cities = [{'name': 'Baku', 'nights': 2}]
    if "rooms" not in st.session_state:
        st.session_state.rooms = [{'adults': 2, 'children': 0}]

    city_options = ["Baku", "Gabala", "Shamakhi", "Sheki", "Shahdag", "Quba"]

    st.subheader("Cities & Nights")
    for i, city in enumerate(st.session_state.cities):
        col1, col2, col3 = st.columns([3, 1, 0.3])
        with col1:
            selected_city = st.selectbox(
                f"City {i+1}", city_options,
                index=city_options.index(city["name"]),
                key=f"city_{i}"
            )
        with col2:
            nights = st.number_input(
                f"Nights in {selected_city}", min_value=1,
                value=city["nights"], key=f"nights_{i}"
            )
        with col3:
            if i > 0:
                if st.button("❌", key=f"remove_city_{i}"):
                    st.session_state.cities.pop(i)
                    st.rerun()

    if st.button("Add City"):
        st.session_state.cities.append({'name': 'Baku', 'nights': 1})

    def is_invalid_route(cities):
        for i in range(1, len(cities)):
            cur = cities[i]['name']
            prev = cities[i - 1]['name']
            if (cur in ["Shahdag", "Quba"] and prev in ["Gabala", "Shamakhi", "Sheki"]) or \
               (prev in ["Shahdag", "Quba"] and cur in ["Gabala", "Shamakhi", "Sheki"]):
                return True
        return False

    if is_invalid_route(st.session_state.cities):
        st.warning("⚠️ Direct transfer between Shahdag/Quba and Gabala/Shamakhi/Sheki is not possible. Please take at least one night stay in Baku.")

    st.subheader("Room Configuration")
    for i, room in enumerate(st.session_state.rooms):
        col1, col2, col3 = st.columns([1, 1, 0.3])
        with col1:
            st.number_input(f"Adults (Room {i+1})", min_value=1, value=room["adults"], key=f"adults_{i}")
        with col2:
            st.number_input(f"Children (Room {i+1})", min_value=0, value=room["children"], key=f"children_{i}")
        with col3:
            if i > 0:
                if st.button("❌", key=f"remove_room_{i}"):
                    st.session_state.rooms.pop(i)
                    st.rerun()

    if st.button("Add Room"):
        st.session_state.rooms.append({'adults': 2, 'children': 0})

    total_adults = sum(r['adults'] for r in st.session_state.rooms)
    total_children = sum(r['children'] for r in st.session_state.rooms)
    st.markdown(f"**Total Pax:** {total_adults + total_children} (Adults: {total_adults}, Children: {total_children})")

    st.markdown("---")
    if st.button("Next"):
        st.session_state.page = "itinerary"
        st.rerun()
