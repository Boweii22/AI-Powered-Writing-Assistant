from flask import Flask, render_template, request
from gpt2_model import generate_content

# Initialize the Flask application
app = Flask(__name__)

# Define the home route
@app.route('/')
def index():
    return render_template('index.html')

# Route for generating content based on user input
@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']  # Get the user's input
    generated_responses = generate_content(prompt, max_length=150)  # Generate text using GPT-2

    return render_template('index.html', prompt=prompt, responses=generated_responses)

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5001)
