from decouple import config
from trycourier import Courier

client = Courier(auth_token=config('COURIER_TOKEN'))

def verify_account_mail(email:str, first_name:str, link:str):
    client.send_message(
        message={
            "to": {
            "email": email,
            },
            "template": config('ACCOUNT_VERIFICATION_TEMP_ID'),
            "data": {
            "appName": "Shelves",
            "firstName": first_name,
            "link": link,
            },
        }
    )

def password_reset_mail(email:str, first_name:str, link:str):
    client.send_message(
        message={
            "to": {
            "email": email,
            },
            "template": config('PASSWORD_RESET_TEMP_ID'),
            "data": {
            "appName": "Shelves",
            "firstName": first_name,
            "link": link,
            },
        }
    )