from openai import OpenAI
import sys
import os
from dotenv import load_dotenv

from pdf_processor import process_pdf
from message_builder import build_user_message, build_system_message



def call_openai_client(images):
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
        model="Qwen/Qwen2-VL-7B-Instruct",
        messages=[system_message, user_message],
    )
    return chat_response.choices[0].message.content
    
def main():
    load_dotenv()
    if len(sys.argv) < 2:
        print("Usage: python main.py <pdf_file>. Using default file.")
        pdf_file_name = os.getenv("DEFAULT_FILE_NAME")
    else:
        pdf_file_name = sys.argv[1]
    
    file_path = os.getenv("PDF_DIR") + pdf_file_name
    if not os.path.isfile(file_path):
        print("Error: File not found.")
        sys.exit(1)
    
    # its necessary to convert pdf to png (or other image formats)
    # open api doesnt accept pdf files, only images
    images = process_pdf(file_path)
    response = call_openai_client(images)
    
    
    print("Chat completion output:", response)

    

if __name__ == "__main__":
    main()



