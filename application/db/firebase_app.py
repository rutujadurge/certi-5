import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "apiKey": os.getenv("AIzaSyCQ4oIou5Qx1p8l9aAzwd2sCb8YoRdIII8"),
    "authDomain": os.getenv("certificate-verification-f48fc.firebaseapp.com"),
    "databaseURL": os.getenv(""),
    "projectId": os.getenv("certificate-verification-f48fc"),
    "storageBucket": os.getenv("certificate-verification-f48fc.appspot.com"),
    "messagingSenderId": os.getenv("645894215793"),
    "appId": os.getenv("1:645894215793:web:e4e16033c5ade9fcaa23d0"),
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def register(email, password):
    try:
        auth.create_user_with_email_and_password(email, password)
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "failure"

def login(email, password):
    try:
        auth.sign_in_with_email_and_password(email, password)
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "failure"