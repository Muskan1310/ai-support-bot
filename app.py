from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from datetime import datetime
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure Gemini (FREE!)
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash')

# Store conversations in memory
conversations = {}

# Your FAQ knowledge base
FAQ_KNOWLEDGE = """
You are a customer support assistant for TechShop, an electronics store.

Common FAQs:
1. Shipping: We offer free shipping on orders over $50. Standard delivery takes 3-5 business days.
2. Returns: 30-day return policy. Items must be unopened and in original packaging.
3. Warranty: All products come with 1-year manufacturer warranty.
4. Payment: We accept credit cards, debit cards, and PayPal.
5. Track Order: Customers can track orders using the tracking number sent via email.
6. Store Hours: Monday-Saturday 9AM-8PM, Sunday 10AM-6PM.
7. Contact: Email support@techshop.com or call 1-800-TECH-SHOP

Keep responses brief and helpful. If you cannot answer a question confidently, 
respond with: "ESCALATE: I'll connect you with a human agent who can better assist you."
"""

@app.route('/')
def home():
    return jsonify({
        "message": "AI Customer Support Bot API is running! (Google Gemini - FREE)",
        "endpoints": {
            "/chat": "POST - Send a message",
            "/history": "GET - Get conversation history"
        }
    })

@app.route('/chat', methods=['POST'])
def chat():
    """
    Main chat endpoint
    Expects JSON: {"session_id": "user123", "message": "What are your store hours?"}
    """
    try:
        # Get data from the request
        data = request.json
        session_id = data.get('session_id', 'default')
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({"error": "Message is required"}), 400
        
        # Initialize conversation history if new session
        if session_id not in conversations:
            conversations[session_id] = []
        
        # Add user message to history
        conversations[session_id].append({
            "role": "user",
            "content": user_message,
            "timestamp": datetime.now().isoformat()
        })
        
        # Build prompt with context
        prompt = FAQ_KNOWLEDGE + "\n\nConversation history:\n"
        
        # Add last 5 messages for context
        for msg in conversations[session_id][-5:]:
            role = "Customer" if msg['role'] == 'user' else "Assistant"
            prompt += f"{role}: {msg['content']}\n"
        
        prompt += f"\nCustomer: {user_message}\nAssistant:"
        
        # Call Gemini API (FREE!)
        response = model.generate_content(prompt)
        ai_message = response.text
        
        # Check if escalation is needed
        needs_escalation = "ESCALATE:" in ai_message
        if needs_escalation:
            ai_message = ai_message.replace("ESCALATE:", "").strip()
        
        # Add AI response to history
        conversations[session_id].append({
            "role": "assistant",
            "content": ai_message,
            "timestamp": datetime.now().isoformat()
        })
        
        # Return response
        return jsonify({
            "response": ai_message,
            "escalate": needs_escalation,
            "session_id": session_id
        })
    
    except Exception as e:
        print("\n" + "="*50)
        print("🚨 ERROR OCCURRED!")
        print("="*50)
        print(f"Error message: {str(e)}")
        print("="*50 + "\n")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/history/<session_id>', methods=['GET'])
def get_history(session_id):
    """Get conversation history for a session"""
    if session_id in conversations:
        return jsonify({
            "session_id": session_id,
            "history": conversations[session_id]
        })
    else:
        return jsonify({"error": "Session not found"}), 404

@app.route('/clear/<session_id>', methods=['DELETE'])
def clear_session(session_id):
    """Clear a conversation session"""
    if session_id in conversations:
        del conversations[session_id]
        return jsonify({"message": f"Session {session_id} cleared"})
    else:
        return jsonify({"error": "Session not found"}), 404

if __name__ == '__main__':
    print("🚀 Starting AI Support Bot (Google Gemini - FREE)")
    print("📝 Make sure GOOGLE_API_KEY is in your .env file")
    app.run(debug=True, port=5000)