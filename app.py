import streamlit as st

# Fungsi untuk mengonversi Celsius ke Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Fungsi untuk mengonversi Fahrenheit ke Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Judul aplikasi
st.title("Temperature Conversion App")

# Pilihan konversi yang diinginkan
option = st.selectbox(
    'Select the conversion:',
    ('Celsius to Fahrenheit', 'Fahrenheit to Celsius')
)

# Jika pengguna memilih Celsius ke Fahrenheit
if option == 'Celsius to Fahrenheit':
    celsius = st.number_input("Enter temperature in Celsius:", format="%.2f")
    if st.button("Convert"):
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.success(f'{celsius}°C = {fahrenheit:.2f}°F')

# Jika pengguna memilih Fahrenheit ke Celsius
if option == 'Fahrenheit to Celsius':
    fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f")
    if st.button("Convert"):
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.success(f'{fahrenheit}°F = {celsius:.2f}°C')
