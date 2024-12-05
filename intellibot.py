import google.generativeai as genai
import streamlit as st
import time
import toml

# Load the API key from the config file
config = toml.load('config.toml')
api_key = config['api_keys']['gemini']

# Streamlit app layout configuration
def app():
    # Gradient text for the title
    gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 2.9em;
        }
        </style>
        <div class="gradient-text">AI Assistant for High School Students</div>
        """
    st.markdown(gradient_text_html, unsafe_allow_html=True)

    st.write(""" 
    :orange[You can ask any academic question, get study tips, or learn more about a topic you're curious about.]

    Please provide the following details in the text area below:
    1. Subject or topic of interest (e.g., Math, Science, History).
    2. A specific question or concept you'd like explained.
    3. Any additional context or information about what you're trying to learn.
    """)

    # Text area for user input
    user_input = st.text_area("Enter your academic question or topic here:")

    # Configure the Gemini API with the loaded API key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat()

    def generate_answer(user_input):
        prompt = f"""
        Academic Question or Topic:
        {user_input}

        Please act as an intelligent assistant for high school students and provide the following:
        1. A clear and accurate explanation of the topic or answer to the question.
        2. Simple examples or illustrations if necessary to aid understanding.
        3. Additional study tips or resources to explore for better comprehension.

        Ensure the response is friendly, easy to understand, and appropriate for high school students.
        """

        full_response = ""
        try:
            for chunk in chat.send_message(prompt, stream=True):
                full_response += chunk.text
        except genai.types.generation_types.BlockedPromptException as e:
            st.exception(e)
        except Exception as e:
            st.exception(e)

        return full_response

    if st.button("Generate Answer"):
        with st.spinner("Generating answer..."):
            time.sleep(4)
            generated_answer = generate_answer(user_input)
            if generated_answer:
                st.success("Here's the answer:")
                st.text_area("Generated Answer", generated_answer, height=400)
            else:
                st.error("Failed to generate an answer. Please try again.")

if __name__ == "__main__":
    app()
