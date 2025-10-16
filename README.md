# AI Customer Support Bot

An intelligent customer support chatbot powered by Google Gemini AI that handles FAQs, remembers conversation context, and escalates complex queries to human agents.



---

##  Features

-  **Natural Language Processing** - Understands customer queries in natural language
-  **Contextual Memory** - Remembers previous messages in the conversation
-  **Smart Escalation** - Automatically detects when to transfer to human support
-  **Fast Responses** - Powered by Google Gemini 2.0 Flash (FREE)
-  **Modern UI** - Beautiful, responsive chat interface
-  **Session Management** - Tracks multiple user conversations simultaneously
-  **Secure** - API keys protected with environment variables

---

##  Tech Stack

**Backend:**
- Python 3.8+
- Flask 3.0.0
- Google Generative AI SDK

**Frontend:**
- HTML5
- CSS3
- Vanilla JavaScript

**AI Model:**
- Google Gemini 2.0 Flash

---

##  Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher installed
- pip (Python package manager)
- Google Gemini API key (FREE - get it [here](https://aistudio.google.com/app/apikey))

---

##  Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Muskan1310/ai-support-bot.git
cd ai-support-bot
```

### 2. Install dependencies
```bash
pip3 install -r requirements.txt
```

### 3. Get Google Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click **"Create API Key"**
3. Copy your API key

### 4. Create environment file

Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY=your-api-key-here
```

**Important:** Never commit your `.env` file to Git!

### 5. Run the application
```bash
python3 app.py
```

The backend will start on `http://127.0.0.1:5000`

### 6. Open the chat interface

Simply open `index.html` in your web browser.

---

##  Usage

### Chat Interface

1. Open `index.html` in your browser
2. Type your message in the input box
3. Press Enter or click Send
4. The bot will respond with helpful information!

### Example Queries

Try asking:
- "What are your store hours?"
- "What's your return policy?"
- "Do you offer free shipping?"
- "How can I track my order?"

---

## API Endpoints

### POST `/chat`
Send a message to the chatbot

**Request:**
```json
{
  "session_id": "user123",
  "message": "What are your store hours?"
}
```

**Response:**
```json
{
  "response": "Our store hours are Monday-Saturday 9AM-8PM, Sunday 10AM-6PM.",
  "escalate": false,
  "session_id": "user123"
}
```

### GET `/history/<session_id>`
Retrieve conversation history for a session

**Response:**
```json
{
  "session_id": "user123",
  "history": [
    {
      "role": "user",
      "content": "What are your store hours?",
      "timestamp": "2025-10-11T05:30:00"
    },
    {
      "role": "assistant",
      "content": "Our store hours are...",
      "timestamp": "2025-10-11T05:30:02"
    }
  ]
}
```

### DELETE `/clear/<session_id>`
Clear a conversation session

**Response:**
```json
{
  "message": "Session user123 cleared"
}
```

---

##  How It Works

### Architecture
```
User Interface (HTML/CSS/JS)
         ↓
    REST API (Flask)
         ↓
  Google Gemini AI
         ↓
    Response Generation
         ↓
  Session Storage (Memory)
```

### LLM Integration

- **Model:** Google Gemini 2.0 Flash
- **Temperature:** 0.7 (balanced creativity and accuracy)
- **Max Tokens:** 200 (concise responses)
- **Context Window:** Last 5 messages for conversation memory

### System Prompt

The bot is trained with a comprehensive FAQ knowledge base covering:
- Shipping policies (free shipping over $50, 3-5 day delivery)
- Return procedures (30-day policy, unopened items)
- Warranty information (1-year manufacturer warranty)
- Payment methods (credit cards, debit cards, PayPal)
- Order tracking process
- Store hours and contact information

### Escalation Logic

The bot automatically escalates to human support when:
- It cannot confidently answer a query
- Customer requests to speak with a manager/supervisor
- Customer expresses frustration or anger
- Query is outside the FAQ knowledge base scope

---

##  Customization

### Modify FAQs

Edit the `FAQ_KNOWLEDGE` variable in `app.py` (lines 20-35):
```python
FAQ_KNOWLEDGE = """
You are a customer support assistant for [YOUR COMPANY].

Common FAQs:
1. [Your FAQ 1]
2. [Your FAQ 2]
...
"""
```

### Change AI Model

Update the model in `app.py` (line 16):
```python
model = genai.GenerativeModel('models/gemini-2.5-flash')  # or other model
```

Available models:
- `models/gemini-2.0-flash` (Fast, recommended)
- `models/gemini-2.5-flash` (Newer)
- `models/gemini-pro-latest` (Best quality)

### Adjust Response Length

Modify in the `call_gemini` function:
```python
"maxOutputTokens": 500  # for longer responses
```

### Customize UI Colors

Edit `index.html` CSS section (lines 10-200) to change:
- Chat background gradient
- Message bubble colors
- Button colors
- Typography

---

## 📁 Project Structure
```
ai-support-bot/
├── app.py              # Backend Flask API
├── index.html          # Frontend chat interface
├── .env               # API keys (not in repo)
├── .gitignore         # Git ignore rules
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

---

##  Testing

### Manual Testing

1. **Simple FAQ Test:**
   - Input: "What are your store hours?"
   - Expected: Returns correct store hours

2. **Context Memory Test:**
   - Input 1: "What's your return policy?"
   - Input 2: "How long does that last?"
   - Expected: Bot remembers context from previous question

3. **Escalation Test:**
   - Input: "I want to speak to a manager"
   - Expected: Red escalation message appears

### API Testing with cURL
```bash
# Test chat endpoint
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id":"test123","message":"What are your hours?"}'

# Test history endpoint
curl http://localhost:5000/history/test123
```

---

##  Deployment

### Deploy to Render (Free)

1. Create account at [render.com](https://render.com)
2. Connect your GitHub repository
3. Add environment variable: `GOOGLE_API_KEY`
4. Deploy!

### Deploy to Railway (Free)

1. Create account at [railway.app](https://railway.app)
2. Import project from GitHub
3. Add environment variable: `GOOGLE_API_KEY`
4. Deploy!

---

##  Security

- ✅ API keys stored in `.env` file (not committed to Git)
- ✅ `.gitignore` prevents accidental secret exposure
- ✅ Input validation on all API endpoints
- ✅ Error handling prevents information leakage
- ✅ CORS configured for secure cross-origin requests

---

##  Performance

- **Response Time:** < 2 seconds average
- **Rate Limit:** 60 requests/minute (Gemini free tier)
- **Concurrent Sessions:** Unlimited (in-memory storage)
- **Cost:** $0 (using free Gemini API)

---

##  Troubleshooting

### "Module not found" errors
```bash
pip3 install -r requirements.txt
```

### "API key not found"
- Ensure `.env` file exists in project root
- Check variable name is exactly `GOOGLE_API_KEY`
- Restart server after creating/editing `.env`

### Frontend can't connect to backend
- Ensure backend is running: `python3 app.py`
- Check browser console for CORS errors
- Verify Flask-CORS is installed: `pip3 install flask-cors`

### "Model not found" error
- Update model name in `app.py` to `models/gemini-2.0-flash`
- Check available models: Run model check script

---

##  What I Learned

Building this project taught me:
- ✅ REST API development with Flask
- ✅ Large Language Model (LLM) integration
- ✅ Asynchronous frontend-backend communication
- ✅ Session management and state handling
- ✅ Error handling and debugging
- ✅ Environment variable security
- ✅ Git version control and collaboration
- ✅ API design patterns and best practices

---

##  Future Enhancements

Potential improvements for v2.0:
- [ ] Database integration (PostgreSQL/MongoDB) for persistent storage
- [ ] User authentication and authorization
- [ ] Multi-language support
- [ ] Voice input/output capabilities
- [ ] Analytics dashboard for conversation insights
- [ ] Email notifications for escalations
- [ ] Sentiment analysis for customer satisfaction
- [ ] File upload support (images, documents)
- [ ] Live chat handoff to human agents
- [ ] Mobile app version (React Native)


---

##  Author

**Muskan**
- GitHub: [@Muskan1310](https://github.com/Muskan1310)
- Project: [ai-support-bot](https://github.com/Muskan1310/ai-support-bot)

---

##  Acknowledgments

- [Google Gemini](https://ai.google.dev/) for providing free AI API
- [Flask](https://flask.palletsprojects.com/) for the excellent web framework
- The open-source community for inspiration and resources

---

##  Support

If you have any questions or run into issues:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Open an issue on [GitHub](https://github.com/Muskan1310/ai-support-bot/issues)
3. Review the code comments for inline documentation

---

**Built with ❤️ using Python, Flask, and Google Gemini AI**
