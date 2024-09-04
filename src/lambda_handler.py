import json
import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv
load_dotenv('config.env')

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

SAFETY_SETTINGS = {
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE
}


def lambda_handler(event, context):
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"You're a story teller creating a short story for a person named {event['name']}, who is {event['age']} years old. This person likes stories ambiented on a {event['scenario']} setting, and they love the style of {event['style']}. Please tell a story about them with maximum 1000 words."

    response = model.generate_content(prompt, safety_settings=SAFETY_SETTINGS)
    return {
        'statusCode': 200,
        'body': json.dumps(response.text)
    }


if __name__ == "__main__":
    with open('test/events/test_event.json', 'r') as file:
        event = json.load(file)
    r = lambda_handler(event, None)
    print(r['body'])
