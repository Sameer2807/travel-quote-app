import streamlit as st
from datetime import datetime

# Function to add cities and nights
def city_input(city_list):
    for i, city in enumerate(city_list):
        col1, col2, col3 = st.columns([3, 1, 1])  # Three columns: City, Nights, Remove button
        with col1:
            city_name = st.selectbox(f"City {i+1}", 
                                     options=["Baku", "Gabala", "Shamakhi", "Sheki", "Shahdag", "Quba"], 
                                     index=["Baku", "Gabala", "Shamakhi", "Sheki", "Shahdag", "Quba"].index(city['name']), 
                                     key=f"city_{i}")
        with col2:
            nights = st.number_input(f"Nights in {city_name}", min_value=1, value=city['nights'], key=f"nights_{i}")
        with col3:
            if i > 0:
                # Remove button (cross in red color)
                remove_button = st.markdown(f'<a href="#" onclick="remove_city({i})" style="color: red; font-size: 24px;">&#10005;</a>', unsafe_allow_html=True)

        city_list[i]['name'] = city_name
        city_list[i]['nights'] = nights

        # Add functionality to remove the city if clicked (implementing via Session State)
        if i > 0 and remove_button:
            city_list.pop(i)
            break  # Exit after removing city to re-render

    return city_list

# Function to check the geography rule for transfers
def check_transfer_rule(cities):
    # Check if the rule is violated (i.e., Shahdag or Quba after Gabala/Shamakhi/Sheki or vice versa)
    for i in range(1, len(cities)):
        if (cities[i]['name'] in ["Shahdag", "Quba"] and 
            cities[i-1]['name'] in ["Gabala", "Shamakhi", "Sheki"]) or \
           (cities[i]['name'] in ["Gabala", "Shamakhi", "Sheki"] and 
            cities[i-1]['name'] in ["Shahdag", "Quba"]):
            return True
    return False

# Initialize city data
if 'cities' not in st.session_state:
    st.session_state.cities = [{'name': 'Baku', 'nights': 2}]

# Title and date picker
st.title("Travel Info Form")
start_date = st.date_input("Select Travel Start Date", datetime.today())

# Add cities dynamically
st.header("Cities & Nights")
city_input(st.session_state.cities)

# Check for transfer rule violation
if check_transfer_rule(st.session_state.cities):
    st.warning("Direct transfer between Shahdag/Quba and Gabala/Shamakhi/Sheki is not possible. Please take a minimum 1-night stay in Baku.")

# Add city button (appears below the last city)
if st.button("Add City"):
    st.session_state.cities.append({'name': 'Baku', 'nights': 1})

# Room Configuration (Dynamic)
st.header("Room Configuration")
if 'rooms' not in st.session_state:
    st.session_state.rooms = [{'adults': 1, 'children': 0}]

# Display room inputs
for i, room in enumerate(st.session_state.rooms):
    st.subheader(f"Room {i+1}")
    col1, col2 = st.columns([1, 1])
