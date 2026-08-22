import os
from google import genai
from dotenv import load_dotenv 
load_dotenv()
client= genai.Client()
response= client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="привіт! напиши короткий скюл запит для вибору всіх користувачів з таблиці юзер."
)
print(response.text)
