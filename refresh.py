import requests

secret_word = "axaxloleslivslomaesh"
response = requests.get('http://www.rlspace.ru/refresh?secret_word=' + secret_word)

