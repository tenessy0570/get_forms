import requests

from db import db

# Variables for test requests
email = "test@gmail.com"
phone = "+7 913 888 88 88"
date_ = "12.12.1999"
text = "some test text"


def send_test_requests():
    endpoint = "http://127.0.0.1:8000/get_form"

    test_payloads = [
        {
            "email_field": email,
            "phone_field": phone,
            "text_field": text,
            "date_field": date_
        },
        {
            "email_field": email,
            "phone_field": phone,
            "text_field": text,
            "date_field": date_,
            "additional_field": text
        },
        {
            "email_field": email,
            "text_field": text,
            "date_field": date_
        },
        {
            "only_phone_field": phone
        },
        {
            "only_phone_field": phone,
            "additional_field": "add field"
        },
        {
            "phone field that never exists 1": phone,
            "email field that never exists 2": email,
            "date_ field that never exists 3": date_,
            "text field that never exists 4": text,
        }
    ]
    print("Existing db forms:")

    for form in db:
        print(form)

    for payload in test_payloads:
        print(f"Sending request with payload: {payload}")
        resp = requests.post(endpoint, json=payload)
        resp_json = resp.json()
        print(f"Got an response with json: {resp_json}")


if __name__ == '__main__':
    send_test_requests()
