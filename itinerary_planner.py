import streamlit as st

def show_itinerary_planner():
    # Page 2: Daily Itinerary

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
        "Shahdag": ["Shahdag City Tour", "Quba City Tour with Khinaliq Village", "Quba City Tour"],
        "Quba": []
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

    if 'cities' in st.session_state:
        def get_available_options(city, next_city=None, is_transition_day=False):
            options = []
            if city in city_tours:
                options.extend(city_tours[city])
            if is_transition_day:
                if next_city:
                    options.append(f"One-way transfer from {city} to {next_city}")
                    options.extend(enroute_tours)
                else:
                    options.append(f"One-way transfer to Baku Airport")
            return options

        def generate_daily_itinerary():
            all_days = []
            total_days = 1
            for i, city in enumerate(st.session_state.cities):
                city_name = city["name"]
                nights = city["nights"]

                for day in range(nights):
                    st.subheader(f"Day {total_days} - {city_name}")
                    options = get_available_options(city_name)
                    selected = st.selectbox(f"Select Tour/Transfer for Day {total_days}", options, key=f"day_{total_days}")
                    all_days.append({"day": total_days, "city": city_name, "selected_tour": selected})
                    total_days += 1

                # Add transition day
                next_city = st.session_state.cities[i + 1]["name"] if i + 1 < len(st.session_state.cities) else None
                if next_city:
                    st.subheader(f"Day {total_days} - {next_city}")
                    options = get_available_options(city_name, next_city=next_city, is_transition_day=True)
                    selected = st.selectbox(f"Select Tour/Transfer for Day {total_days}", options, key=f"day_{total_days}")
                    all_days.append({"day": total_days, "city": next_city, "selected_tour": selected})
                    total_days += 1

            return all_days

        itinerary = generate_daily_itinerary()
        st.subheader("Final Itinerary")
        for day_info in itinerary:
            st.write(f"Day {day_info['day']} in {day_info['city']} - Selected: {day_info['selected_tour']}")
    else:
        st.warning("Please complete the first page to select cities and nights.")

