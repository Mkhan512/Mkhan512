from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined responses for the chatbot
responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm just a bot, but I'm functioning perfectly! How about you?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't quite understand that. Can you please rephrase?"
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

@app.route('/')
def index():
    return "<h1>Welcome to the Custom Chatbot!</h1><p>Use the /chat endpoint to interact with the bot.</p>"

if __name__ == '__main__':
    app.run(debug=True)
