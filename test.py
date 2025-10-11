# test.py - Quick verification
import sys
print(f"✅ Python version: {sys.version}")
print(f"✅ Python location: {sys.executable}")

try:
    import flask
    print("✅ Flask installed")
except:
    print("❌ Flask not installed - Run: pip3 install flask")

try:
    import openai
    print("✅ OpenAI installed")
except:
    print("❌ OpenAI not installed - Run: pip3 install openai")

try:
    from dotenv import load_dotenv
    print("✅ python-dotenv installed")
except:
    print("❌ python-dotenv not installed - Run: pip3 install python-dotenv")

print("\n🎉 All set! You're ready to build your chatbot!")