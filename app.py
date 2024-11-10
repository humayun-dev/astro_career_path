# from flask import Flask, request, render_template
# from utils.astrology_calculator import generate_birth_chart

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/calculate', methods=['POST'])
# def calculate():
#     # Retrieve form data
#     birth_date = request.form.get('birth_date')
#     birth_time = request.form.get('birth_time')
#     latitude = request.form.get('latitude')
#     longitude = request.form.get('longitude')

#     # Validate that all required fields are filled
#     if not all([birth_date, birth_time, latitude, longitude]):
#         return render_template('result.html', error="All fields are required.")

#     # Generate the birth chart (including career suggestions)
#     result = generate_birth_chart(birth_date, birth_time, float(latitude), float(longitude))

#     # Render the result template and pass the result
#     return render_template('result.html', result=result)

# if __name__ == '__main__':
#     app.run(debug=True)

# -------------- code without streamlit ------------------------ #
# from flask import Flask, request, render_template
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderTimedOut, GeocoderServiceError
# from utils.astrology_calculator import generate_birth_chart

# app = Flask(__name__)

# geolocator = Nominatim(user_agent="astrology_birth_chart_app")

# def get_lat_lon_from_city_country(city, country):
#     """Function to convert city and country to latitude and longitude"""
#     try:
#         location = geolocator.geocode(f"{city}, {country}")
#         if location:
#             return location.latitude, location.longitude
#         else:
#             return None, None
#     except GeocoderTimedOut:
#         return None, None
#     except GeocoderServiceError:
#         return None, None

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/calculate', methods=['POST'])
# def calculate():
#     # Retrieve form data
#     birth_date = request.form.get('birth_date')
#     birth_time = request.form.get('birth_time')
#     city = request.form.get('city')
#     country = request.form.get('country')

#     # Validate that all required fields are filled
#     if not all([birth_date, birth_time, city, country]):
#         return render_template('result.html', error="All fields are required.")

#     # Convert city and country to latitude and longitude
#     latitude, longitude = get_lat_lon_from_city_country(city, country)

#     if latitude is None or longitude is None:
#         return render_template('result.html', error="Could not find coordinates for the given city and country.")

#     # Generate the birth chart (including career suggestions)
#     result = generate_birth_chart(birth_date, birth_time, latitude, longitude)

#     # Render the result template and pass the result
#     return render_template('result.html', result=result)

# if __name__ == '__main__':
#     app.run(debug=True)


# using streamlit
import streamlit as st
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from utils.astrology_calculator import generate_birth_chart

# Set up geolocator
geolocator = Nominatim(user_agent="astrology_birth_chart_app")

def get_lat_lon_from_city_country(city, country):
    """Function to convert city and country to latitude and longitude"""
    try:
        location = geolocator.geocode(f"{city}, {country}")
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return None, None
    except GeocoderServiceError:
        return None, None

# Streamlit app front-end
st.title("Astrology Career Recommendation App")
st.write("Enter your details to get astrology-based career suggestions.")

# Input fields
birth_date = st.text_input("Birth Date (YYYY-MM-DD)")
birth_time = st.text_input("Birth Time (HH:MM AM/PM)")
city = st.text_input("City")
country = st.text_input("Country")

# Button to calculate result
if st.button("Calculate"):
    if not all([birth_date, birth_time, city, country]):
        st.error("All fields are required.")
    else:
        latitude, longitude = get_lat_lon_from_city_country(city, country)
        
        if latitude is None or longitude is None:
            st.error("Could not find coordinates for the given city and country.")
        else:
            # Generate the birth chart (including career suggestions)
            result = generate_birth_chart(birth_date, birth_time, latitude, longitude)
            st.write("Career Recommendations based on your birth chart:")
            st.write(result)
