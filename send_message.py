import logging
import requests
from config import REDIS_URL, redis_client

# WhatsApp Cloud API credentials
ACCESS_TOKEN = "EAAXTql4avxgBO2AaH8m9mk3ZAPE22XT4ukCZBbvpFcAaE2zGZCTPwj36fzZARu3cBfY4CQxrJZBeU6nqc02hok9MqybPjZAptHwZAyxdVorffgzOBIUv8Cvji4oI4ZCdaTpIwdm5GBNWcTOsQxYNJwJVe4FhqyZAnLOFgW9cUNkBZBYfgVotoXYuwDz6y3UeOWiVP5rCdBkkdpptzrbAeaGZAeZCqu97en3o1gZDZD"
PHONE_NUMBER_ID = "455890610951428"

def send_language_options(phone_number):
    # Send language selection options to the user
    language_buttons = [
        {"type": "postback", "title": language, "payload": language} for language in ["English", "Hinglish"]
    ]
    
    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "header": {"type": "text", "text": "Please select your preferred language."},
            "body": {"text": "Choose your language:"},
            "action": {"buttons": language_buttons}
        }
    }
    
    send_message(phone_number, payload)

def send_message(phone_number, message):
    # Send message to the user
    url = f"https://graph.facebook.com/v21.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {"body": message}
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        logging.info(f"Message sent to {phone_number}: {response.json()}")
    except Exception as e:
        logging.error(f"Failed to send message to {phone_number}: {e}")
