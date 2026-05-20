import requests

CITY = input("Введите город: ")

# wttr.in — бесплатный погодный API, не требует ключа
url = f"https://wttr.in/{CITY}?format=%l:+%t,+%h+влажность,+%w+ветер,+%C"

try:
    response = requests.get(url, timeout=10)
    
    if response.status_code == 200 and "Unknown" not in response.text:
        print(f"\n{response.text}")
    else:
        print("Ошибка: город не найден. Проверьте название.")
        
except requests.exceptions.RequestException:
    print("Ошибка подключения к серверу погоды.")
