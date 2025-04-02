from openai import OpenAI
import os
from message_builder import build_user_message, build_system_message

def call_openai_client(images, model_name):
    client = OpenAI(
        api_key=os.getenv("API_KEY"),
        base_url=os.getenv("API_BASE"),
    )

    # there is a specific message format
    # jinja is applied on the message format
    system_message = build_system_message()
    user_message = build_user_message(images)
    
    # TODO implement user message
    # system_message = build_system_message()
    chat_response = client.chat.completions.create(
        model=model_name,
        messages=[system_message, user_message],
    )
    return chat_response.choices[0].message.content

def call_api_client(images, model_name):
    # Call the OpenAI API client with the provided images
    response = call_openai_client(images, model_name)
    return response