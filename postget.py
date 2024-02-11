import requests

# URL, на который будут отправляться запросы
url = 'http://94.241.168.97:3000/'

# Отправка GET-запроса
response_get = requests.get(url)
print(f'GET Response: {response_get.text}')

# Данные для POST-запроса
data = {'key1': 'value1', 'key2': 'value2'}

# Отправка POST-запроса
response_post = requests.post(url, data=data)
print(f'POST Response: {response_post.text}')
