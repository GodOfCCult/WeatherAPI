import requests

city = input("Введите город: ")
url = f"https://wttr.in/{city}?format=%l:+%t,+%h+влажность,+%w+ветер,+%C"

response = requests.get(url)
print(response.text)
