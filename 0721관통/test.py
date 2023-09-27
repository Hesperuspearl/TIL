import requests

url = 'https://fakestoreapi.com/carts'
response = requests.get(url).json()

print(response)
#print(response.json()) reponsedp .jason 붙이거나, 이렇게.
