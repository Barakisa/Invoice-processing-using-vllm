import sys
import os
from pdf_processor import process_pdf
from utils import save_response, parse_arguments, remove_markdown_json_tags, log_response_raw
from api_client import call_api_client

    
def main():
    [pdf_file_name, model_name] = parse_arguments(sys.argv)
    file_path = os.getenv("PDF_DIR") + pdf_file_name
    if not os.path.isfile(file_path):
        print("Error: File not found.")
        sys.exit(1)
    
    # its necessary to convert pdf to png (or other image formats)
    # open api doesnt accept pdf files, only images
    images = process_pdf(file_path)
    response_raw = call_api_client(images, model_name)
    response_json = remove_markdown_json_tags(response_raw)
    # save response in .txt dir
    # and then (inside described how) log the resopnse in one big log
    save_response(response_json, pdf_file_name)
    log_response_raw(response_raw, model_name)
    
    print("Chat completion output: \n", response_json)

    

if __name__ == "__main__":
    main()



