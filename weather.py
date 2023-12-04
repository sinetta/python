import requests
city='kochi'
api_key='360e4bc3865e745ec844bd7ec054ca11'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response=requests.get(url)
data=response.json()
# print(data)
print(data['weather'][0]['description'])
print(data['main']['temp'])
print(data['main']['temp_max'])
print(data['main']['temp_min'])
print(data['main']['feels_like'])