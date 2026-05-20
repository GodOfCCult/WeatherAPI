import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = input("Введите город: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ru"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"\nГород: {data['name']}")
    print(f"Температура: {data['main']['temp']}°C")
    print(f"Ощущается как: {data['main']['feels_like']}°C")
    print(f"Погода: {data['weather'][0]['description']}")
    print(f"Влажность: {data['main']['humidity']}%")
    print(f"Ветер: {data['wind']['speed']} м/с")
else:
    print("Ошибка:", data.get("message", "Город не найден"))