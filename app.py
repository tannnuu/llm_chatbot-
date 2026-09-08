import pandas as pd
import requests
import json
import streamlit as st

# Define your Google Gemini API key and endpoint
GEMINI_API_KEY = "AIzaSyA9pYRt95gwUm3UvoZTy30PQ0P65F8niYA"  # Replace with your actual API key
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

# Load your CSV file into a pandas DataFrame
df = pd.read_csv("Medicine_Details.csv")

# Function to search for medicine details in the CSV dataset
def search_in_csv(medicine_name):
    result = df[df['Medicine Name'].str.lower().str.contains(medicine_name.strip().lower())]
    if not result.empty:
        medicine_info = result.iloc[0]
        response = f"Here are the details I found for {medicine_info['Medicine Name']}:\n\n" \
                   f"Composition: {medicine_info['Composition']}\n" \
                   f"Uses: {medicine_info['Uses']}\n" \
                   f"Side Effects: {medicine_info['Side_effects']}\n" \
                   f"Manufacturer: {medicine_info['Manufacturer']}\n" \
                   f"Reviews:\n" \
                   f"  - Excellent: {medicine_info['Excellent Review %']}%\n" \
                   f"  - Average: {medicine_info['Average Review %']}%\n" \
                   f"  - Poor: {medicine_info['Poor Review %']}%\n" \
                   f"[Image of {medicine_info['Medicine Name']}]({medicine_info['Image URL']})"
        return response
    return None

# Function to fetch information from Google Gemini
def fetch_from_gemini(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        try:
            result = response.json()
            if 'candidates' in result and len(result['candidates']) > 0:
                return result['candidates'][0]['content']['parts'][0]['text']
            else:
                return "I'm sorry, but I couldn't retrieve the information you requested."
        except json.JSONDecodeError:
            return "I'm sorry, there was an error processing your request."
    else:
        return f"Error fetching information from Google Gemini: {response.status_code} - {response.text}"

# Function to handle the submission
def submit_data():
    if 'input_text' in st.session_state and st.session_state.input_text:
        user_input = st.session_state.input_text

        if user_input.strip().lower() == 'exit':
            st.write("Thank you for using the assistant. Stay healthy!")
            st.session_state.input_text = ""
            return

        # Add the user's query to the conversation
        st.session_state.conversation.append(f"<div class='user-message'><strong>You:</strong> {user_input}</div>")

        # Check if it's a follow-up question
        if user_input.strip().lower() in ["its uses", "its side effects", "tell me more", "composition", "its composition"]:
            if st.session_state.conversation:
                last_message = st.session_state.conversation[-2].split(":")[-1].strip()
                user_input = f"Tell me about the {user_input.strip()} of {last_message}."
            else:
                st.session_state.conversation.append("<div class='assistant-message'><strong>Assistant:</strong> Could you please specify the name of the medicine first?</div>")
                st.session_state.input_text = ""
                return

        # First check the CSV dataset
        csv_response = search_in_csv(user_input)
        if csv_response:
            st.session_state.conversation.append(f"<div class='assistant-message'><strong>Assistant:</strong> {csv_response}</div>")
        else:
            # If not found in CSV, fetch from Google Gemini
            st.session_state.conversation.append("<div class='assistant-message'><strong>Assistant:</strong> I couldn't find details for this medicine in the dataset, so I'm fetching information from Google Gemini...</div>")
            response = fetch_from_gemini(user_input)
            st.session_state.conversation.append(f"<div class='assistant-message'><strong>Assistant:</strong> {response}</div>")

        # Clear input field
        st.session_state.input_text = ""

# Streamlit app
def main():
    st.set_page_config(page_title="MediSum Chatbot", page_icon="💊", layout="wide")

    # Sidebar for app title and instructions
    st.sidebar.title("MediSum Chatbot 💬")
    st.sidebar.write("Enter your query below and get information about medicines. The conversation history will be preserved until you close the bot.")

    # Initialize or retrieve the context from session state
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    # Call the submission handler before rendering the input box
    submit_data()

    # Apply custom CSS based on theme
    st.markdown(
        """
        <style>
        .user-message {
            color: blue;
        }
        .assistant-message {
            color: var(--text-color);
        }
        body {
            background-color: var(--background-color);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Chat container with scrollable history
    chat_container = st.container()

    # Display the conversation history
    with chat_container:
        for chat in st.session_state.conversation:
            st.markdown(chat, unsafe_allow_html=True)

    # Input box for the user query
    st.text_input("Type your message here:", value="", key="input_text", on_change=submit_data)

if __name__ == '__main__':
    main()
