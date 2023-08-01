import requests

def get_weather_data(location):
    api_url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={location}&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(api_url)
    return response.json()

def get_weather_for_date(weather_data, date):
    for forecast in weather_data['list']:
        if forecast['dt_txt'].startswith(date):
            return forecast['main']['temp']
    return None

def get_wind_speed_for_date(weather_data, date):
    for forecast in weather_data['list']:
        if forecast['dt_txt'].startswith(date):
            return forecast['wind']['speed']
    return None

def get_pressure_for_date(weather_data, date):
    for forecast in weather_data['list']:
        if forecast['dt_txt'].startswith(date):
            return forecast['main']['pressure']
    return None

def main():
    location = input("Enter the city name: ")
    weather_data = get_weather_data(location)

    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_weather_for_date(weather_data, date)
            if temperature:
                print(f"Temperature on {date}: {temperature}°C")
            else:
                print("No weather data found for the given date.")
        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_for_date(weather_data, date)
            if wind_speed:
                print(f"Wind speed on {date}: {wind_speed} m/s")
            else:
                print("No weather data found for the given date.")
        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_for_date(weather_data, date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("No weather data found for the given date.")
        elif choice == 0:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()