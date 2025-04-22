import streamlit as st
from datetime import datetime

# Function to add cities and nights
def city_input(city_list):
    for i, city in enumerate(city_list):
        col1, col2 = st.columns([3, 1])
        with col1:
            city_name = st.text_input(f"City {i+1}", value=city['name'], key=f"city_{i}")
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
add_city = st.button("Add City")

if add_city:
    st.session_state.cities.append({'name': '', 'nights': 1})

# Display cities and nights input
st.session_state.cities = city_input(st.session_state.cities)

# Room Configuration (Dynamic)
st.header("Room Configuration")
rooms = st.number_input("Number of Rooms", min_value=1, value=1)

room_data = []
for i in range(rooms):
    st.subheader(f"Room {i+1}")
    adults = st.number_input(f"Number of Adults in Room {i+1}", min_value=1, value=1)
    children = st.number_input(f"Number of Children in Room {i+1}", min_value=0, value=0)
    room_data.append({"adults": adults, "children": children})

# Show the calculated total pax (adults + children)
total_pax = sum(room['adults'] + room['children'] for room in room_data)
st.write(f"Total Pax: {total_pax}")

# Next button
if st.button("Next"):
    st.write("Proceeding to the next step...")
