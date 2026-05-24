import requests

city = input("Enter city name: ")

URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e43abfcda2944a6979fc7bed52d818ea&units=metric"

response = requests.get(URL)

data = response.json()

print(data)   # Debug output

if response.status_code == 200:

    print("\n------ WEATHER REPORT ------\n")

    print("City:", data["name"])
    print("Country:", data["sys"]["country"])

    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]["feels_like"], "°C")

    print("Humidity:", data["main"]["humidity"], "%")

    print("Weather:", data["weather"][0]["main"])
    print("Description:", data["weather"][0]["description"])

    print("Wind Speed:", data["wind"]["speed"], "m/s")

else:
    print("Error:", data["message"])