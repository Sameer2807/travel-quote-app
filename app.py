import streamlit as st
from trip_info_form import show_trip_info_form
from itinerary_planner import show_itinerary_planner

# Session-based navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "form"

if st.session_state.current_page == "form":
    show_trip_info_form()
elif st.session_state.current_page == "itinerary":
    show_itinerary_planner()
