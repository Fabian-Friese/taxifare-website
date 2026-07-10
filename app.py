import streamlit as st
import datetime
import requests
'''
# TaxiFareModel front
'''





pickup_date = st.date_input("Pickup date", datetime.date(2013, 7, 6))
pickup_time = st.time_input("Pickup time", datetime.time(17, 18))
pickup_datetime = f"{pickup_date} {pickup_time}"

pickup_longitude = st.number_input("Pickup longitude", value=-73.950655, format="%.6f")
pickup_latitude = st.number_input("Pickup latitude", value=40.783282, format="%.6f")
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.984365, format="%.6f")
dropoff_latitude = st.number_input("Dropoff latitude", value=40.769802, format="%.6f")
passenger_count = st.number_input("Passenger count", min_value=1, max_value=8, value=1, step=1)

url = 'https://taxifare-555874397383.europe-west1.run.app/predict'

params = dict(
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count,
)

if st.button('Predict fare'):
    response = requests.get(url, params=params)
    prediction = response.json()
    fare = prediction['fare']

    st.header(f'💰 Predicted fare: ${fare:.2f}')
