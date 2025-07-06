# Smart Medical Assistant Chatbot

This project features a smart medical assistant chatbot designed to offer preliminary diagnoses and recommend suitable doctors based on user-provided symptoms. It includes implementations using both Gradio and Chainlit for different user interface experiences.

## Features

* **Preliminary Diagnosis:** Provides an initial diagnosis for user-described symptoms.
* **Doctor Recommendation:** Suggests relevant doctors (specialty, availability) based on the diagnosis.
* **Dual Interfaces:**
    * **Gradio:** A simple, quick web UI.
    * **Chainlit:** An interactive, conversational chat interface.

## Technologies

* **Azure OpenAI:** Powers the diagnostic capabilities.
* **Gradio:** For the web-based UI.
* **Chainlit:** For the chat-based UI.
* **Python:** Core programming language.
* **`python-dotenv`:** For environment variable management.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Abdelrahman-Elshahed/Konecta_Tasks.git
    cd Medical_Chatbot_Gradio
    ```
2.  **Install dependencies:**
    ```bash
    pip install openai gradio chainlit python-dotenv
    ```
3.  **Configure `.env`:** Create a `.env` file with your Azure OpenAI credentials:
    ```
    AZURE_API_KEY="your_azure_api_key"
    AZURE_API_VERSION="your_api_version"
    AZURE_ENDPOINT="your_azure_endpoint"
    DEPLOYMENT_NAME="your_deployment_name"
    ```

## Usage

### Gradio Interface

Run:
```bash
python Medical_Chatbot_Gradio.py
```
- Access at http://127.0.0.1:7860
<img width="1919" height="987" alt="Image" src="https://github.com/user-attachments/assets/e375de65-ef1a-455f-89ca-4a9ca25cfe69" />
<img width="1915" height="990" alt="Image" src="https://github.com/user-attachments/assets/5ef2615a-7d57-4783-b9f1-b806b54b0990" />

### Chainlit Interface

Run:
```bash
chainlit run chainlit run chainlit_app.py -w
```
- Access at http://localhost:8000
<img width="1919" height="992" alt="Image" src="https://github.com/user-attachments/assets/1aea027f-651e-4808-b9b7-af545cae13f7" />
