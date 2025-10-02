from google import genai
from config import API_KEY


client = genai.Client(
    api_key=API_KEY
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)

client.close()