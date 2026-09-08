# 💊 MediSum: Medical Information Chatbot

A smart, interactive chatbot built with Streamlit and powered by Google's Gemini LLM. MediSum provides users with detailed information about medicines by first checking a local database for quick, structured answers and then leveraging a powerful AI for more general queries.

**Live Preview**:-[https://llmchatbot-dtlt9bfmcqup4kqek6yzfo.streamlit.app/](https://llmchatbot-dtlt9bfmcqup4kqek6yzfo.streamlit.app/)

## ✨ Core Features

-   **Hybrid Search:** First queries a local `Medicine_Details.csv` file for fast, reliable information on composition, uses, side effects, and more.
-   **LLM-Powered Intelligence:** If a medicine isn't in the local dataset, it uses the Google Gemini 1.5 Flash model to provide comprehensive answers from the web.
-   **Interactive Chat UI:** A clean, user-friendly interface built with Streamlit that displays the conversation history.
-   **Image Display:** Shows an image of the medicine when found in the local dataset.
-   **Context-Aware Follow-ups:** Basic understanding of follow-up questions like "what are its uses?" or "tell me more".

## 🛠️ Tech Stack

| Category        | Technology    | Description                                                        |
| --------------- | ------------- | ------------------------------------------------------------------ |
| **Frontend** | Streamlit     | For creating the interactive web-based user interface.             |
| **Language** | Python        | The core language for the application logic.                       |
| **Data Handling** | Pandas        | Used to load, search, and manage the local `Medicine_Details.csv` dataset. |
| **AI / LLM** | Google Gemini | The Large Language Model used for answering queries not in the local data. |
| **HTTP Requests** | Requests      | For making API calls to the Google Gemini endpoint.                |

---

## ⚙️ How It Works

The application follows a simple yet powerful workflow:

1.  **User Input:** The user types a query (e.g., the name of a medicine) into the Streamlit chat input.
2.  **Local Database Search:** The app first performs a case-insensitive search within the `Medicine_Details.csv` file.
3.  **Response Generation:**
    -   **If Found:** It formats the medicine's details (composition, uses, side effects, image, etc.) into a clean response and displays it to the user.
    -   **If Not Found:** It informs the user that it's fetching data from a broader source and sends the user's query to the Google Gemini API. The LLM's response is then displayed.
4.  **Conversation Update:** The user's query and the assistant's response are added to the chat history, which persists for the duration of the session.

---

## 🚀 Getting Started

Follow these steps to run the MediSum chatbot on your local machine.

### Prerequisites

-   Python 3.8 or newer
-   A Google Gemini API Key. You can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YooshaMirza/llm_chatbot.git](https://github.com/YooshaMirza/llm_chatbot.git)
    cd llm_chatbot
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Add your API Key:**
    Open the `app.py` file and replace the placeholder with your actual Google Gemini API key.
    ```python
    # In app.py
    GEMINI_API_KEY = "YOUR_GOOGLE_GEMINI_API_KEY_HERE"
    ```
    > ⚠️ **Security Warning:** For a public project, it is strongly recommended to use Streamlit Secrets or environment variables to protect your API key instead of hardcoding it directly in the script.

### Running the Application

Once your setup is complete, run the following command in your terminal:

```bash
streamlit run app.py
```

Your web browser will automatically open a new tab with the MediSum chatbot interface.

---

## 📁 Project Structure

```
llm_chatbot/
├── Medicine_Details.csv    # The local database of medicine information
├── app.py                  # The main Streamlit application script
├── requirements.txt        # A list of required Python packages
└── README.md               # This file
```

## 📜 License

This project is open source. Consider adding a LICENSE file (e.g., MIT) to define how others can use your code.
