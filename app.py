import streamlit as st
from trip_info_form import show_trip_info_form
from itinerary_planner import show_itinerary_planner

# Initialize the session variable if not already
if "current_page" not in st.session_state:
    st.session_state.current_page = "form"

# Routing based on session state
if st.session_state.current_page == "form":
    show_trip_info_form()
elif st.session_state.current_page == "itinerary":
    show_itinerary_planner()
