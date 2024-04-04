import requests

def fetch_weather(city):
    api_key = "12345678901234567890123456789012"  # Replace this with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    print(f'Weather data for {city}: {data}')
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    return temperature, description

city = input("Enter the name of the city: ")
temperature, description = fetch_weather(city)
print(f"The current temperature in {city} is {temperature}°C with {description}.")
