from flask import Flask, request
import json
import logging
from process_message import handle_user_interaction

# Flask app setup
app = Flask(__name__)

# Logging setup
logging.basicConfig(
    filename="app.log",  # Log file location
    level=logging.DEBUG,  # Log level, you can use DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verify token for webhook setup
        verify_token = "SHRIRAM"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == verify_token:
            app.logger.info(f"Webhook verification successful with challenge: {challenge}")
            return challenge, 200
        else:
            app.logger.error("Invalid verification token")
            return "Invalid token", 403

    if request.method == 'POST':
        try:
            data = request.get_json()
            app.logger.debug(f"Webhook data: {json.dumps(data, indent=4)}")

            # Check if 'messages' field exists
            if 'messages' not in data.get('entry', [{}])[0].get('changes', [{}])[0].get('value', {}):
                app.logger.error("Missing 'messages' field in webhook payload")
                return "Missing 'messages' field", 400

            # Process incoming message
            message = data["entry"][0]["changes"][0]["value"]["messages"][0]
            user_number = message["from"]
            user_message = message["text"]["body"]

            # Handle user interaction
            handle_user_interaction(user_number, user_message)

        except Exception as e:
            app.logger.error(f"Error processing webhook: {e}")
            return f"Error: {e}", 500

        app.logger.info("Webhook event received and processed successfully.")
        return "Event received", 200

if __name__ == '__main__':
    app.run(debug=True)
