import os
from dotenv import load_dotenv,find_dotenv
import google.generativeai as genai





def chatbot(k,prompt):
     genai.configure(api_key=k)
     model=genai.GenerativeModel(model_name='gemini-1.5-flash-latest')
     response=model.generate_content(prompt)
     return response.text
    
     


