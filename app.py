from flask import Flask, render_template, request

app = Flask(__name__)

# Function to detect mood based on keywords
def detect_mood(text):
    text = text.lower()
    
    # Keywords for mood categories
    mood_keywords = {
        "happy": ["happy", "amazing", "excited", "great", "best"],
        "sad": ["sad", "low", "lonely", "down", "upset"],
        "stressed": ["stressed", "anxious", "overwhelmed", "worried"],
        "angry": ["angry", "annoyed", "frustrated", "mad"],
        "relaxed": ["calm", "relaxed", "peaceful", "easy", "balanced"],
        "confused": ["confused", "stuck", "complicated", "lost", "unsure"],
        "curious": ["curious", "explore", "learn", "try", "discover"],
        "grateful": ["grateful", "thankful", "blessed", "appreciate", "happy"],
    }

    # Match keywords to moods
    for mood, keywords in mood_keywords.items():
        if any(keyword in text for keyword in keywords):
            return mood

    return "neutral"  # Default mood if no keywords match

# Response generator based on detected mood
def generate_response(mood):
    responses = {
        "happy": "That's wonderful! Keep spreading those good vibes! 😊",
        "sad": "I'm sorry you're feeling this way. Remember, brighter days are ahead. 🌈",
        "stressed": "Take a deep breath. You've got this! Maybe a short break could help. 🌱",
        "angry": "It's okay to feel angry sometimes. Try to channel that energy positively! 💪",
        "relaxed": "Sounds like you're having a peaceful moment. Enjoy it! 🌸",
        "confused": "It's okay to feel unsure. Take it one step at a time, and things will clear up. 💡",
        "curious": "Curiosity is the key to growth! Explore and learn something new today. 🌟",
        "grateful": "Gratitude is such a powerful feeling. Keep appreciating the little things in life. 🌻",
        "neutral": "I'm here to chat! Let me know how you're feeling or what's on your mind. 🤗",
    }

    return responses.get(mood, "I'm here to help with whatever you're feeling. Let's chat! 🌟")

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for processing the user's input
@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form['message']
    detected_mood = detect_mood(user_input)
    response = generate_response(detected_mood)

    return render_template('index.html', user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(debug=True)
