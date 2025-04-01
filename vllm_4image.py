from openai import OpenAI
import sys
import cv2
import base64
import os


def build_message_content(image_urls, user_prompt):
    # NOTE: The prompt formatting with the image token `<image>` is not needed
    # since the prompt will be processed automatically by the API server.        
    message_content = [{"type": "text", "text": user_prompt}]
    for image_url in image_urls:
        message_content.append({"type": "image_url", "image_url": {"url": image_url}})
    return message_content

def build_base64_urls(images):
    urls = []
    for image in images:
        img = cv2.imread(image)
        jpg_img = cv2.imencode('.png', img)
        b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
        urls.append(f"data:image/png;base64,{b64_string}")
    return urls

def get_png_files(folder_path):
    return [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.png')]

openai_api_key = "EMPTY"
openai_api_base = "http://192.168.1.220:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

user_prompt = "Whats in image 1? Wjhats in image 2? Whats in image 3? Whats in image 4?"
folder_path = ".\\png"
images = get_png_files(folder_path)

urls = build_base64_urls(images)
user_message_content = build_message_content(urls, user_prompt)

chat_response = client.chat.completions.create(
    model="Qwen/Qwen2-VL-7B-Instruct",
    messages=[{
        "role": "user",
        "content": user_message_content,
    }],
)
print("Chat completion output:", chat_response.choices[0].message.content)

