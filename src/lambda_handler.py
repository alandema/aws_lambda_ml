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
    prompt_parts = [
        " Your role is to give people data science themed nicknames. Someone will tell you their first name, or you can ask them their first name, and then you should respond with a really clever data science themed nickname, where you take their first name, and then append to it some sort of data science term, ideally using alliteration. ",
        "input: Paul",
        "output: Precision-Recall Paul",
        "input: Robert",
        "output: Random-Forest Robert",
        "input: Will",
        "output: Whisker-Plot Will",
        "input: Ned",
        "output: Neural-Network Ned",
        "input: Tommy",
        "output: Transformer Tommy",
        "input: Greg",
        "output: Gradient-Descent Greg",
        "input: Earl",
        "output: Eigen-Vector Earl",
        "input: Ricardo",
        "output: ResNet Ricardo",
        "input: Larry",
        "output: LightGBM Larry",
        "input: Pat",
        "output: Permutation-Importance Pat",
        "input: Carlos",
        "output: ",
    ]
    response = model.generate_content(prompt_parts)
    return {
        'statusCode': 200,
        'body': json.dumps(response.text)
    }


if __name__ == "__main__":
    with open('test/events/test_event.json', 'r') as file:
        event = json.load(file)
    r = lambda_handler(event, None)
    print(r)
