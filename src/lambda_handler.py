import google.auth
import os
import json
import vertexai
from google.oauth2 import service_account
from vertexai.generative_models import GenerativeModel
import base64

from dotenv import load_dotenv
load_dotenv('config.env')


def decode_creds():
    credentials = json.loads(base64.b64decode(os.environ["GOOGLE_APPLICATION_CREDENTIALS"]).decode("utf-8"))
    return credentials


def lambda_handler(event, context):
    credentials = service_account.Credentials.from_service_account_info(decode_creds(),
                                                                        scopes=["https://www.googleapis.com/auth/cloud-platform"])

    project_id = os.environ["PROJECT_ID"]

    vertexai.init(project=project_id, location="us-central1", credentials=credentials)

    model = GenerativeModel("gemini-1.5-flash-001")

    response = model.generate_content(
        "What's a good name for a flower shop that specializes in selling bouquets of dried flowers?"
    )

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
