import requests
from django.conf import settings


def initiate_chapa_payment(amount, email, first_name, last_name):
    data = {
        'amount': amount,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'currency': 'ETB',
        'callback_url': 'http://yourdomain.com/payment/callback',
        'return_url': 'http://yourdomain.com/payment/success'
    }


    response = requests.post('http://checkout.chapa.co/checkout/web/payment/PL-aAmCO6Tb7QVY', json=data, )

    if response.status_code == 200:
        return response.json()
    else:
        return None