import logging

def extract_language(message):
    # Implement logic to detect language from the user's response
    language_options = ["English", "Hindi", "Bengali", "Tamil", "Telugu", "Marathi"]
    for language in language_options:
        if language.lower() in message.lower():
            return language
    logging.warning(f"Language extraction failed for message: {message}")
    return "English"  # Default language

def extract_name(message):
    # Extract name from user message (simple case)
    name = message.strip()
    if not name:
        logging.warning(f"Name extraction failed for message: {message}")
    return name

def extract_age(message):
    # Attempt to extract age from the message
    try:
        age = int(message.strip())
        return age
    except ValueError:
        logging.warning(f"Age extraction failed for message: {message}")
        return None  # If age extraction fails, return None
