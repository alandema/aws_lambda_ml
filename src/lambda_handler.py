import google.auth
import os
import json
import vertexai
import google.generativeai as genai
import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv('config.env')


GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)


def lambda_handler(event, context):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Give me python code to sort a list")
    print(response.text)

    print(response.text)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == "__main__":
    with open('test/events/test_event.json', 'r') as file:
        event = json.load(file)
    r = lambda_handler(event, None)
    print(r)
