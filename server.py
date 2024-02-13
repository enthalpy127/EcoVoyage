#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request
import flask

import stripe

# This is your test secret API key.
stripe.api_key = 'sk_test_51OiughCTv3u198xwuF0qQ4idBa1M48jwj0ItOMTLCvhZ8QZCnzKTOWjI19S0GKlMkukPNAJgyrSojryJ5Gz0Ge3H00YgYYkfc7'

app = Flask(__name__, static_url_path='', static_folder='templates/public')

YOUR_DOMAIN = 'http://localhost:4242'


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1OixtICTv3u198xwuBeUFdfi',
                    'quantity': 2,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url='http://localhost:5000',
            automatic_tax={'enabled': True},
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


# @app_flask.route('/showpayment_method')
# def render_payment():
#     return flask.redirect(':4242/payment_method/checkout.html')


if __name__ == '__main__':
    app.run(port=4242)
