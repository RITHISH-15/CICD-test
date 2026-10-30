from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Sample Thirukkural data
THIRUKKURAL_DATA = {
    "number": 1,
    "verse_line1": "அகர முதல எழுத்தெல்லாம் ஆதி",
    "verse_line2": "பகவன் முதற்றே உலகு.",
    "tamil_meaning": "அகரம் எழுத்துகளுக்கு முதலாக இருப்பது போல, உலகம் கடவுளுக்கு முதலாக இருக்கிறது.",
    "english_explanation": "As 'A' is the first of all letters, so is the eternal God the first in the world.",
    "motivation": "Start your day with foundational wisdom, clarity, and disciplined focus!"
}

@app.route("/")
def home():
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_day = now.strftime("%A")
    return render_template("index.html", 
                           date=current_date, 
                           day=current_day, 
                           kural=THIRUKKURAL_DATA)

@app.route("/health")
def health():
    return {"status": "healthy", "service": "daily-thirukkural"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
