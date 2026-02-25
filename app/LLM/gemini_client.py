import google.generativeai as genai 
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

async def chat_with_gemini(prompt):
    response = await model.generate_content_async(prompt)
    return response.text