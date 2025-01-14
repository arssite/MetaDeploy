import logging
from config import db
from send_message import send_language_options, send_message
from extract_message import extract_language, extract_name, extract_age

# Sequence of questions
questions = ["language", "name", "age"]

def handle_user_interaction(user_number, user_message):
    user_collection = db.get_collection(user_number)
    user_data = user_collection.find_one({})

    if not user_data:
        # New user, start with the first question
        user_collection.insert_one({"phone_number": user_number, "language": None, "name": None, "age": None})
        logging.info(f"New user added with phone number {user_number}")
        send_language_options(user_number)
        return

    # Check for the next missing question and process
    for question in questions:
        if not user_data.get(question):
            # Extract message and update MongoDB
            if question == "language":
                language = extract_language(user_message)
                user_collection.update_one({"phone_number": user_number}, {"$set": {"language": language}})
                logging.info(f"User {user_number} selected language: {language}")
                send_message(user_number, f"Language set to {language}, what is your name?")
            elif question == "name":
                name = extract_name(user_message)
                user_collection.update_one({"phone_number": user_number}, {"$set": {"name": name}})
                logging.info(f"User {user_number} provided name: {name}")
                send_message(user_number, f"Thank you {name}! How old are you?")
            elif question == "age":
                age = extract_age(user_message)
                user_collection.update_one({"phone_number": user_number}, {"$set": {"age": age}})
                logging.info(f"User {user_number} provided age: {age}")
                send_message(user_number, f"Thank you for sharing your details, {name}. All your details are saved.")
            return
