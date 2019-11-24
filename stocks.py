import requests
from my_token import token

def get_stock(company):
    url = 'https://cloud.iexapis.com/stable/stock/{}/quote?token={}'.format(company, token)
    response = requests.get(url)
    data = response.json()
    print("The company {} open at {} today.".format(data['companyName'], data['open']))
    return data


data = get_stock('fb')