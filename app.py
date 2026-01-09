"""
Streamlit frontend for Weather API.
"""

import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/weather"

st.set_page_config(
    page_title="Weather App",
    page_icon="🌦️",
)

st.title("🌦️ Weather Information App")
st.write(
    "Get current weather, latitude and longitude for any city."
)

city = st.text_input(
    "Enter City Name",
    placeholder="e.g. London",
)

output_format = st.selectbox(
    "Select Output Format",
    ["json", "xml"],
)

if st.button("Get Weather"):
    if not city:
        st.error("Please enter a city name.")
    else:
        payload = {
            "city": city,
            "output_format": output_format,
        }

        try:
            response = requests.post(
                API_URL,
                json=payload,
                timeout=10,
            )

            if response.status_code == 200:
                st.success("Weather fetched successfully!")

                if output_format == "json":
                    data = response.json()

                    st.json(data)
                    st.metric(
                        "Temperature (°C)",
                        data["temperature_celsius"],
                    )
                    st.metric("Latitude", data["latitude"])
                    st.metric("Longitude", data["longitude"])
                    st.write(
                        "Condition:",
                        data["condition"],
                    )
                else:
                    st.code(
                        response.text,
                        language="xml",
                    )
            else:
                st.error(
                    response.json().get(
                        "detail",
                        "Something went wrong.",
                    )
                )
        except requests.exceptions.RequestException:
            st.error("Cannot connect to Weather API server.")