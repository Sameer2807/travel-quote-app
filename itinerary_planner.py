import streamlit as st

# Page 2: Daily Itinerary
if 'cities' in st.session_state:
    # Function to get available options for each day
    def get_available_options(city, next_city=None, is_transition_day=False):
        options = []
        if city in city_tours:
            options.extend(city_tours[city])  # Add city tours

        if is_transition_day:
            if next_city:
                # Add transition transfer between cities (Baku to next city or last day to airport)
                options.append(f"One-way transfer from {city} to {next_city}")
                # Add enroute tours
                options.extend(enroute_tours)
            else:
                # Last day in city, one-way transfer to airport
                options.append(f"One-way transfer to {city} Airport")

        return options

    # Iterate over cities and build day-wise options
    def generate_daily_itinerary():
        all_days = []  # To store all the days' information

        total_days = 0
        # Loop through cities
        for i, city in enumerate(st.session_state.cities):
            city_name = city["name"]
            nights = city["nights"]
            total_days += nights  # Add nights (which are same as days-1)

            # For each day in the city (including transition day)
            for day in range(1, nights + 2):  # Adding +1 for last day
                is_transition_day = (day == nights + 1)
                next_city = st.session_state.cities[i + 1]["name"] if i + 1 < len(st.session_state.cities) else None

                st.subheader(f"Day {total_days - nights + day} - {city_name}")

                available_options = get_available_options(city_name, next_city, is_transition_day)

                selected_tour = st.selectbox(f"Select Tour/Transfer for Day {total_days - nights + day}", available_options, key=f"day_{total_days - nights + day}")

                all_days.append({"day": total_days - nights + day, "city": city_name, "selected_tour": selected_tour})

        return all_days

    # Generate daily itinerary
    itinerary = generate_daily_itinerary()

    # Displaying the final itinerary (for testing purposes)
    st.subheader("Final Itinerary")
    for day_info in itinerary:
        st.write(f"Day {day_info['day']} in {day_info['city']} - Selected: {day_info['selected_tour']}")
else:
    st.warning("Please complete the first page to select cities and nights.")
