import base64
import requests
import re
import os
from mimetypes import guess_type

# Get OpenAI API Key from the system environment variables
api_key = os.environ.get('OPENAI_API_KEY')

if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Define a function to convert an image to a base64 encoded string
def encode_image(image_path):
    # Read the image file
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # Get the MIME type of the image
    mime_type, _ = guess_type(image_path)
    if not mime_type or not mime_type.startswith('image'):
        raise ValueError(f"Unsupported image format for file: {image_path}")

    # Convert image data to a base64 encoded string
    base64_image = base64.b64encode(image_data).decode('utf-8')

    # Return a base64 encoded string with the correct MIME type
    return f"data:{mime_type};base64,{base64_image}"

# Use regular expressions to separate the image URL and text content from the user input
def process_input(user_input):
    match = re.match(r"[\"\'](.*?)[\"\'](.*)", user_input)
    if match:
        image_path, text = match.groups()
        return image_path, text.strip()
    else:
        return None, user_input.strip()

# Conversation history data
conversation_history = []

while True:
    user_input = input("User: ")

    # Exit the chat program when user inputs "end conversation"
    if user_input == "End the conversation":
        break

    image_path, text = process_input(user_input)
    # If an unsupported image format is encountered, an exception will be thrown
    if image_path:
        try:
            base64_image = encode_image(image_path)
        except ValueError as e:
            print(f"Error: {e}")
            continue

        image_message = {
            "type": "image_url",
            "image_url": {
                "url": base64_image
            }
        }
        conversation_history.append({"role": "user", "content": [{
          "type": "text",
          "text": text
        }, image_message]})
    else:
        conversation_history.append({"role": "user", "content": [{
          "type": "text",
          "text": text}]})

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": conversation_history,
        "max_tokens": 1000
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    assistant_response = response.json()["choices"][0]["message"]["content"]
    print("ChatGPT: ", assistant_response)

    # Update conversation history data
    conversation_history.append({"role": "assistant", "content": assistant_response})