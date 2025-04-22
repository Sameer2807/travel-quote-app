import streamlit as st
from datetime import datetime

# Function to add cities and nights
def city_input(city_list):
    for i, city in enumerate(city_list):
        col1, col2 = st.columns([3, 1])
        with col1:
            city_name = st.selectbox(f"City {i+1}", 
                                     options=["Baku", "Gabala", "Shamakhi", "Sheki", "Shahdag", "Quba"], 
                                     index=["Baku", "Gabala", "Shamakhi", "Sheki", "Shahdag", "Quba"].index(city['name']), 
                                     key=f"city_{i}")
        with col2:
            nights = st.number_input(f"Nights in {city_name}", min_value=1, value=city['nights'], key=f"nights_{i}")
        city_list[i]['name'] = city_name
        city_list[i]['nights'] = nights

    return city_list

# Initialize city data
if 'cities' not in st.session_state:
    st.session_state.cities = [{'name': 'Baku', 'nights': 2}]

# Title and date picker
st.title("Travel Info Form")
start_date = st.date_input("Select Travel Start Date", datetime.today())

# Add cities dynamically
st.header("Cities & Nights")
city_input(st.session_state.cities)

# Add city button (appears below the last city)
if st.button("Add City"):
    st.session_state.cities.append({'name': '', 'nights': 1})

# Room Configuration (Dynamic)
st.header("Room Configuration")
if 'rooms' not in st.session_state:
    st.session_state.rooms = [{'adults': 1, 'children': 0}]

# Display room inputs
for i, room in enumerate(st.session_state.rooms):
    st.subheader(f"Room {i+1}")
    col1, col2 = st.columns([1, 1])
    with col1:
        adults = st.number_input(f"Number of Adults in Room {i+1}", min_value=1, value=room['adults'], key=f"adults_{i}")
    with col2:
        children = st.number_input(f"Number of Children in Room {i+1}", min_value=0, value=room['children'], key=f"children_{i}")
    st.session_state.rooms[i]['adults'] = adults
    st.session_state.rooms[i]['children'] = children

# Add room button (appears below the last room input)
if st.button("Add Room"):
    st.session_state.rooms.append({'_
