import ntpath
import sys
import os
from dotenv import load_dotenv

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def log_response_raw(response):
    # Log the response to a file
    with open("./logs/responses.log", "a", encoding="utf-8") as log_file:
        log_file.write(response + "\n")
        
def save_response(response_json, file_name):
    # Save the response to a text file
    with open("./txt/" + file_name + ".txt", "w", encoding="utf-8") as output_file:
        output_file.write(response_json)
    
def parse_arguments(args):
    load_dotenv()
    if len(args) == 1:
        print("No arguments provided. Usage: python script.py <pdf_file_name> ?<model_name>")
        sys.exit(1)
    elif len(args) == 2:
        pdf_file_name = args[1]
        model_name = os.getenv("MODEL_NAME")
        print(f"Document provided. Using default model: {model_name}")
    elif len(args) >= 3:
        pdf_file_name = args[1]
        model_name = args[2]
    return [pdf_file_name, model_name]


def remove_markdown_json_tags(text):
    return text.replace("```json", "").replace("```", "")