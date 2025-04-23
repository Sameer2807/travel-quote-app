import streamlit as st
from trip_info_form import show_trip_info_form
from itinerary_planner import show_itinerary_planner

st.set_page_config(page_title="Travel Quote App", layout="wide")

# Simple navigation
page = st.sidebar.selectbox("Choose Page", ["Trip Info", "Itinerary Planner"])

if page == "Trip Info":
    show_trip_info_form()
elif page == "Itinerary Planner":
    show_itinerary_planner()
