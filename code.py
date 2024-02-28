import streamlit as st
from gtts import gTTS
import openai
import requests
from PIL import Image
from io import BytesIO

# Set your OpenAI API key and Clipboard API key
openai.api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")
clipboard_api_key = st.sidebar.text_input("Enter your Clipboard API key:", type="password")

# Typing animation HTML code with "Project by Deekshith B"
typing_animation = """
<h1 align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=35&center=true&vCenter=true&width=500&height=70&lines=Project+by+Deekshith+B" alt="Typing Animation" />
</h1>
"""

# Display the typing animation
st.markdown(typing_animation, unsafe_allow_html=True)

# Function to generate text response using GPT-3
def generate_text_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content'].strip()

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text, lang='en')
    audio_file_path = "output_audio.mp3"
    tts.save(audio_file_path)
    st.audio(audio_file_path, format="audio/mp3")

# Function to generate image response
def generate_image_response(prompt, api_key):
    # Make a POST request to the ClipDrop API endpoint
    r = requests.post('https://clipdrop-api.co/text-to-image/v1',
                      files={'prompt': (None, prompt, 'text/plain')},
                      headers={'x-api-key': api_key})

    # Check if the request was successful
    if r.ok:
        # Display the image
        image = Image.open(BytesIO(r.content))
        st.image(image, caption='Generated Image', use_column_width=True)
    else:
        st.error("Failed to generate image.")

def main():
    st.title("AI Assistant")

    # Initialize an empty list to store questions and responses
    question_responses = []

    # Loop for asking questions and displaying responses
    for i in range(10):
        # Get user input for the prompt
        user_input = st.text_input(f"Enter your question {i+1}:")

        # Get user's choice for response format
        response_format = st.sidebar.radio(f"Choose response format for question {i+1}:", ["Text", "Speech", "Image"])

        if response_format == "Image":
            clipdrop_api_key = clipboard_api_key

        # Generate response based on user's choice
        if st.button(f"Submit {i+1}"):
            if response_format == "Text":
                chatgpt_response = generate_text_response(user_input)
                st.write(f"Response {i+1}:", chatgpt_response)
                question_responses.append((user_input, chatgpt_response))
            elif response_format == "Speech":
                chatgpt_response = generate_text_response(user_input)
                text_to_speech(chatgpt_response)
                question_responses.append((user_input, chatgpt_response))
            elif response_format == "Image":
                generate_image_response(user_input, clipdrop_api_key)
                question_responses.append((user_input, "Image response"))

 


if __name__ == "__main__":
    main()
