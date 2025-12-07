# 🤖 KoreAruImage

**KoreAruImage** is a powerful yet simple tool that leverages Google's Gemini 1.5 Pro and Flash models to perform advanced visual reasoning. This application allows users to upload a target object and a scene, and the AI determines if the object is present and describes its context (e.g., "The coffee mug is on the wooden desk").

This project demonstrates the integration of multimodal AI capabilities into a user-friendly web interface, showcasing the potential of Generative AI in computer vision tasks.

## ✨ Features

- **Object Detection & Contextualization**: Goes beyond simple bounding boxes to understand _where_ an object is and _how_ it interacts with the scene.
- **Dual Model Support**: Choose between `gemini-1.5-flash` for speed and efficiency, or `gemini-1.5-pro` for complex reasoning.
- **Interactive UI**: Built with Streamlit for a seamless, responsive user experience.
- **Secure API Key Handling**: Input your API key directly in the UI, ensuring no keys are hardcoded.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A Google Cloud Project with the Gemini API enabled.
- An API Key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ai-nexus-jp/KoreAruImage.git
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  **Set up environment variables:**
    Copy the example environment file and add your API key:
    ```bash
    cp .env.example .env
    ```
    Open `.env` and replace `your_api_key_here` with your actual Google Gemini API Key.

### Usage

1.  **Run the application:**

    ```bash
    streamlit run app.py
    ```

2.  **Open your browser:**
    The app should automatically open at `http://localhost:8501`.

3.  **Analyze Images:**
    - The app will automatically load your API Key from the `.env` file (you can also enter it manually).
    - Upload a **Target Image** (the object you want to find).
    - Upload a **Scene Image** (the photo of the room or environment).
    - Click **Analyze Images** and watch Gemini work its magic!

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Model**: [gemini-2.5-flash](https://deepmind.google/technologies/gemini/)
- **Image Processing**: Pillow (PIL)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

_Created by Hiroshi Nishito - [AI Nexus](https://ai-nexus.jp)_
