from openai import OpenAI
import requests
import json
import logging
import random
from config import *

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'
]

random_letter = random.choice(letters)

def flippy_slack():
    try:
        client = OpenAI(api_key=OPEN_AI_KEY)
        slack_webhook_endpoint = SLACK_WEBHOOK_ENDPOINT

        # prompt gpt
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {'role':'system',
                'content': 'you are a lexicographer who knows every word in the english dictionary'
                },
                {
                    'role':'user',
                    'content':f'pick a word that starts with the letter: {random_letter} and give me the part of speech, definition, example sentence using the word, and the etymology'
                }
            ], max_tokens=800
        )

        slack_message = completion.choices[0].message.content 
        payload = {
            "text": slack_message #payload for slack message
        }

        response = requests.post(slack_webhook_endpoint, data=json.dumps(payload)) #post message to slack hook
        response.raise_for_status()
        logger.info(f'Successfully posted message to channel: {payload}')

    except requests.exceptions.RequestException as e:
        logging.exception(f"Request to Slack failed: {e}")
    except openai.error.OpenAIError as e:
        logging.exception(f"OpenAI error occurred: {e}")
    except Exception as e:
        logging.exception(f"An error occurred: {e}")

if __name__ == "__main__":
    flippy_slack()