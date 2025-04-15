import ntpath
import sys
import os
from dotenv import load_dotenv
import json


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def log_response_raw(response, model_name):
    # Log the response to a file
    with open(os.getenv("LOG_DIR") + model_name + "_responses.log", "a", encoding="utf-8") as log_file:
        log_file.write(response + "\n")
        
def save_response(response_json, file_name):
    # Save the response to a text file
    with open(os.getenv("TXT_DIR") + file_name + ".txt", "w", encoding="utf-8") as output_file:
        output_file.write(response_json)
    
def parse_arguments(args):
    
    load_dotenv()
    pdf_file_name = os.getenv("DEFAULT_FILE_NAME")
    model_name = os.getenv("DEFAULT_MODEL_NAME")
    if len(args) == 1:
        print(f"No arguments provided. Usage: python script.py <pdf_file_name> ?<model_name>. Using default values: file: {pdf_file_name} model:{model_name}")
    elif len(args) == 2:
        pdf_file_name = args[1]
        print(f"Document provided. Using default model: {model_name}")
    elif len(args) >= 3:
        pdf_file_name = args[1]
        model_name = args[2]
    return [pdf_file_name, model_name]


def remove_markdown_json_tags(text):
    return text.replace("```json", "").replace("```", "")


def combine_prompt_and_template(system_prompt_file, json_template_file):
    try:
        with open(system_prompt_file, 'r') as f:
            system_prompt = f.read()
        
        with open(json_template_file, 'r') as f:
            template = json.load(f)  # Load JSON directly

        combined_string = (
            system_prompt + 
            "\noutput format:\n ```json" + 
            json.dumps(template, indent=4) + # Use dumps to convert dict to string
            "\n```"
        )
        return combined_string

    except FileNotFoundError:
        print("Error: One or both files not found.")
        return ""
    except json.JSONDecodeError:
        print("Error: Invalid JSON in template file.")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""

def get_system_prompt():
    system_prompt_path = "../prompts/system_prompt.txt"
    template_path = "../prompts/output_template.json"

    if not all([system_prompt_path, template_path]):
        raise ValueError("Missing required environment variables")

    return combine_prompt_and_template(system_prompt_path, template_path)