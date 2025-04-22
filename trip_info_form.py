import streamlit as st
from datetime import timedelta

st.title("🧳 Travel Quote - Basic Trip Info")

# Travel Start Date
start_date = st.date_input("Select Travel Start Date")

# City & Nights Section
st.subheader("🏙️ Cities and Stay Duration")
cities = []
num_cities = st.number_input("How many cities in the itinerary?", min_value=1, step=1, value=1)

for i in range(num_cities):
    city = st.text_input(f"City #{i+1} Name", key=f"city_{i}")
    nights = st.number_input(f"Number of nights in {city or 'city'}", min_value=1, step=1, key=f"nights_{i}")
    cities.append({"city": city, "nights": nights})

# Calculate End Date
if start_date and all(c['nights'] > 0 for c in cities):
    total_nights = sum(c['nights'] for c in cities)
    end_date = start_date + timedelta(days=total_nights)
    st.markdown(f"**End Date:** {end_date.strftime('%Y-%m-%d')} ({total_nights} nights)")

# Room Configuration
st.subheader("🛏️ Room Configuration")
room_configs = []
num_rooms = st.number_input("Number of Rooms", min_value=1, step=1, value=1)

for i in range(num_rooms):
    col1, col2 = st.columns(2)
    with col1:
        adults = st.number_input(f"Room #{i+1} - Adults", min_value=1, step=1, key=f"adults_{i}")
    with col2:
        children = st.number_input(f"Room #{i+1} - Children", min_value=0, step=1, key=f"children_{i}")
    room_configs.append({"adults": adults, "children": children})

# Calculate Total Pax
total_adults = sum(r['adults'] for r in room_configs)
total_children = sum(r['children'] for r in room_configs)
total_pax = total_adults + total_children

st.markdown(f"**Total Pax:** {total_pax} (Adults: {total_adults}, Children: {total_children})")

# Proceed Button
if st.button("Next: Choose Components"):
    st.success("Proceeding to component selection...")
