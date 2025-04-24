import streamlit as st

def show_itinerary_planner():
    city_tours = {
        "Baku": [
            "Baku City Tour", "Panoramic Baku City Tour", "Old Baku City Tour",
            "Absheron Tour and Shopping", "Absheron Tour and Heydar Aliyev Centre",
            "Gobustan Tour", "Absheron and Gobustan Tour", "Shahdag Day Tour",
            "Gabala Day Tour", "Quba Day Tour", "Shamakhi Day Tour", "Sheki Day Tour"
        ],
        "Gabala": ["Gabala City Tour", "Sheki City Tour", "Shamakhi City Tour"],
        "Shamakhi": ["Shamakhi City Tour"],
        "Sheki": ["Sheki City Tour", "Gabala City Tour from Sheki"],
        "Shahdag": ["Shahdag City Tour", "Quba City Tour with Khinaliq Village", "Quba City Tour"]
    }

    enroute_tours = [
        "Transfer to Gabala enroute Shamakhi from Baku",
        "Transfer to Shahdag enroute Candy Cane Mountain",
        "Transfer to Shahdag and Shahdag Day Tour",
        "Transfer to Gabala enroute Gabala Day Tour",
        "Transfer to Baku enroute Absheron Tour from Shahdag",
        "Transfer to Baku enroute Gobustan Tour from Gabala",
        "Transfer to Baku enroute Shamakhi Tour from Gabala",
        "Transfer to Baku enroute Sheki Tour from Gabala",
        "Transfer to Baku and Panoramic City Tour",
        "Transfer to Baku and Shopping from Gabala or Shamakhi or Sheki or Shahdag or Quba"
    ]

    def get_available_options(city, next_city=None, is_transition_day=False, is_last_day=False):
        options = []
        if city in city_tours:
            options.extend(city_tours[city])
        if is_transition_day:
            if next_city:
                options.append(f"One-way transfer from {city} to {next_city}")
                options.extend(enroute_tours)
            elif city == "Baku":
                options.append("One-way transfer to Baku Airport")
        return options

    def generate_daily_itinerary():
        all_days = []
        total_day = 1

        for i, city in enumerate(st.session_state.cities):
            nights = city["nights"]
            city_name = city["name"]
            next_city = st.session_state.cities[i + 1]["name"] if i + 1 < len(st.session_state.cities) else None

            for day in range(nights):
                st.subheader(f"Day {total_day} - {city_name}")
                options = get_available_options(city_name)
                selected = st.selectbox(f"Select Tour/Transfer", options, key=f"{city_name}_day_{total_day}")
                all_days.append({"day": total_day, "city": city_name, "activity": selected})
                total_day += 1

            # Transition day (last day of current city == first day of next city)
            if i < len(st.session_state.cities) - 1:
                st.subheader(f"Day {total_day} - {next_city}")
                options = get_available_options(city_name, next_city, is_transition_day=True)
                selected = st.selectbox(f"Select Tour/Transfer", options, key=f"{city_name}_to_{next_city}_day_{total_day}")
                all_days.append({"day": total_day, "city": next_city, "activity": selected})
                total_day += 1
            elif city_name == "Baku":
                st.subheader(f"Day {total_day} - {city_name}")
                options = get_available_options(city_name, is_transition_day=True)
                selected = st.selectbox(f"Select Tour/Transfer", options, key=f"{city_name}_airport_day_{total_day}")
                all_days.append({"day": total_day, "city": city_name, "activity": selected})
                total_day += 1

        return all_days

    if "cities" in st.session_state:
        itinerary = generate_daily_itinerary()

        st.subheader("Final Itinerary Summary")
        for day in itinerary:
            st.markdown(f"**Day {day['day']} - {day['city']}**: {day['activity']}")
    else:
        st.warning("Please fill in the trip info form first.")
