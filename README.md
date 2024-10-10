# AI-Powered Writing Assistant

![627_1x_shots_so](https://github.com/user-attachments/assets/a935a4fb-17ac-4375-8ce2-cfaf10aa1fef)


This project is an AI-powered writing assistant that helps users generate written content based on prompts. The app uses the GPT-2 model to create text based on user input, providing a useful tool for drafting articles, generating ideas, or expanding on existing topics. It is built using Python's Flask web framework and the Hugging Face `transformers` library.

## Features
- **Content Generation**: Generates relevant text based on user prompts.
- **AI-Powered**: Uses the GPT-2 language model for content creation.
- **Web Interface**: Simple and intuitive web interface for input and output.
- **Interactive**: Users can submit any text prompt and get a response from the AI model.

## Technologies Used
- **Frontend**: HTML, CSS (for user input and displaying generated content).
- **Backend**: Python (Flask) for routing and handling requests.
- **AI Model**: GPT-2 from Hugging Face's `transformers` library for text generation.
- **Additional Libraries**: `torch` for model handling, `requests` for API requests (if needed).

## Installation and Setup

### Prerequisites
- Python 3.6 or higher
- `pip` package manager

### Steps to Install
1. **Clone the repository**:
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

    If you don’t have a `requirements.txt` file, here are the key dependencies:
    ```bash
    pip install flask transformers torch
    ```

4. **Run the Flask app**:
    ```bash
    python app.py
    ```

    The app should now be running locally on `http://127.0.0.1:5000/` or the specified port.

### Troubleshooting
If the app doesn't load:
- Ensure the correct port is specified in the `app.py` file.
- Try accessing the app via `http://127.0.0.1:5001/`
- Check for long-path issues on Windows and enable long-path support if needed.

## Usage
1. **Open the web interface**:
    - Visit `http://127.0.0.1:50001` (or `http://localhost:50001`).
    
2. **Enter a prompt**:
    - In the text box on the homepage, enter a prompt such as “Write a paragraph about AI.”

3. **Submit the form**:
    - After submitting, the AI will generate content based on your input and display the result on the same page.

## File Structure

## Example
Here's how you might use the app:

- **Input**: “Explain the importance of artificial intelligence in healthcare.”

## Future Improvements
- **Model Customization**: Implement more advanced models like GPT-3 or fine-tune GPT-2 for specific content generation tasks.
- **Improved UI**: Enhance the design of the user interface to make it more user-friendly.
- **Error Handling**: Add more robust error handling for better user experience.

## Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and make a pull request.

## Contact
For any inquiries or support, please contact **Tombri Bowei** at `tombribowei01@gmail.com`.

