AI Customer Support Bot

An intelligent customer support chatbot powered by Google Gemini AI that handles FAQs, remembers conversation context, and escalates complex queries to human agents.

Features

Natural Language Processing - Understands customer queries in natural language

Contextual Memory - Remembers previous messages in the conversation

Smart Escalation - Automatically detects when to transfer to human support

Fast Responses - Powered by Google Gemini 2.0 Flash (FREE)

Modern UI - Beautiful, responsive chat interface

Session Management - Tracks multiple user conversations simultaneously


Tech Stack

Backend: Flask (Python)

AI Model: Google Gemini 2.0 Flash

Frontend: HTML5, CSS3, JavaScript

API Architecture: RESTful endpoints

Storage: In-memory session storage


Prerequisites

Python 3.8 or higher

Google Gemini API key (FREE)


Installation & Setup

1. Clone the repository
   
bashgit clone https://github.com/Muskan1310/ai-support-bot.git

cd ai-support-bot

2. Install dependencies
   
bashpip3 install -r requirements.txt

3. Get Google Gemini API Key


Go to Google AI Studio

Click "Create API Key"

Copy your API key


4. Create .env file

Create a .env file in the project root:

bashGOOGLE_API_KEY=your-api-key-here

5. Run the application
   
bashpython3 app.py

The backend will start on http://127.0.0.1:5000

8. Open the chat interface
   
Open index.html in your web browser.

📡 API Endpoints

POST /chat
Send a message to the chatbot
Request:
json{
  "session_id": "user123",
  "message": "What are your store hours?"
}
Response:
json{
  "response": "Our store hours are Monday-Saturday 9AM-8PM, Sunday 10AM-6PM.",
  "escalate": false,
  "session_id": "user123"
}
GET /history/<session_id>
Retrieve conversation history for a session
Response:
json{
  "session_id": "user123",
  "history": [...]
}
DELETE /clear/<session_id>
Clear a conversation session
How It Works
LLM Integration
The bot uses Google Gemini 2.0 Flash with:

Model: models/gemini-2.0-flash
Temperature: 0.7 (balanced creativity/accuracy)
Max Tokens: 200 (concise responses)
Context Window: Last 5 messages for conversation memory

System Prompt
The bot is trained with a comprehensive FAQ knowledge base covering:

Shipping policies
Return procedures
Warranty information
Payment methods
Order tracking
Store hours and contact info

Escalation Logic
The bot automatically escalates to human support when:

It cannot confidently answer a query
Customer requests to speak with a manager
Customer expresses frustration
Query is outside the FAQ scope

Customization
Modify FAQs
Edit the FAQ_KNOWLEDGE variable in app.py:
pythonFAQ_KNOWLEDGE = """
Your custom FAQs here...
"""
Change AI Model
Update the model in app.py:
pythonmodel = genai.GenerativeModel('models/gemini-2.5-flash')  # or other model
Adjust Response Length
Modify max_tokens in the API call:
python"maxOutputTokens": 500  # longer responses
📁 Project Structure
ai-support-bot/
├── app.py              # Backend API
├── index.html          # Chat interface
├── .env               # API keys (not in repo)
├── .gitignore         # Git ignore rules
├── requirements.txt   # Python dependencies
└── README.md          # Documentation
🧪 Testing
Test Cases

Simple FAQ Query

Input: "What are your store hours?"
Expected: Returns store hours


Context Memory

Input 1: "What's your return policy?"
Input 2: "How long does that last?"
Expected: Remembers context from previous question


Escalation Trigger

Input: "I want to speak to a manager"
Expected: Escalates to human support



     Deployment
Option 1: Render

Create account at render.com
Connect GitHub repository
Add environment variables
Deploy!

Option 2: Railway

Create account at railway.app
Import project from GitHub
Add environment variables
Deploy!

     Security Notes

✅ API keys stored in .env (not committed to Git)

✅ .gitignore prevents secret leakage

✅ Input validation on all endpoints

✅ Error handling prevents information disclosure


    Performance

Response Time: < 2 seconds average
Rate Limit: 60 requests/minute (Gemini free tier)
Concurrent Sessions: Unlimited (in-memory storage)

    Troubleshooting
"Module not found" errors
bashpip3 install -r requirements.txt
"API key not found"
Ensure .env file exists
Check variable name is GOOGLE_API_KEY
Restart the server after creating .env

Frontend can't connect
Ensure backend is running (python3 app.py)
Check console for CORS errors
Verify Flask-CORS is installed




⭐ If you found this project helpful, please give it a star!
