import streamlit as st
from trip_info_form import show_trip_info_form
from itinerary_planner import show_itinerary_planner

if "page" not in st.session_state:
    st.session_state.page = "trip_info"

if st.session_state.page == "trip_info":
    show_trip_info_form()
elif st.session_state.page == "itinerary":
    show_itinerary_planner()
