import os
from dotenv import load_dotenv,find_dotenv
import google.generativeai as genai



def get_my_key():
    load_dotenv(find_dotenv(),override=True)
    return os.environ.get('GOOGLE_API_KEY')

def show_models():
    genai.configure(api_key=get_my_key())
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
                print(m.name)


def chatbot(prompt):
     genai.configure(api_key=get_my_key())
     model=genai.GenerativeModel(model_name='gemini-1.5-flash-latest')
     response=model.generate_content(prompt)
     return response.text
    
     

show_models()
print(chatbot(input('Please enter your question\n')))

