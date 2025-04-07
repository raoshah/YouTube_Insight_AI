# 🎥 YouTube Insight AI

A full-stack AI-powered web app built with **Django** and **ReactJS**. Users can paste a YouTube video link and extract useful, structured information using AI — such as recipes, book recommendations, example explanations, or even fact-checking the content of the video.

---

## 🚀 Features

- 🔗 Paste any YouTube video link
- 🧠 Get structured insights from the video using AI
- 🍳 Extract step-by-step recipes from cooking videos
- 📚 Generate book recommendation lists from educational videos
- 📖 Create brief examples or summaries of complex topics
- ✅ Fact-check video claims (coming soon)
- 🔄 Future features will include multi-language support and downloadable results

---

## 🧰 Tech Stack

| Layer       | Tech Used                        |
|-------------|----------------------------------|
| Frontend    | ReactJS, Axios, Redux     |
| Backend     | Django, Django REST Framework    |
| AI Layer    | DeepSeek AI |
| Transcript  | youtube-transcript-api (Python)  |
| Extras      | dotenv, CORS, Requests, etc.     |

---

## 📦 Installation Guide

### 🔹 Backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver



### 🔹 Frontend (ReactJS)
cd frontend
npm install
npm start

### Create a .env file in your Django backend/ directory:
AI_API_KEY=your_api_key_here
AI_API_BASE=https://api.provider.ai/v1  # Adjust if using a different provider

### Project Structure
project-root/
│
├── backend/
│   ├── manage.py
│   ├── backend/           # Django settings
│   ├── api/               # Views, serializers, core logic
│   ├── requirements.txt
│   ├── .env
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│  
└── README.md

👨‍💻 Author
❤️ by [Shah Rukh Rao]




