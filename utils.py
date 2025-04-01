import ntpath

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def log_response(response):
    # Log the response to a file
    with open("responses.log", "a", encoding="utf-8") as log_file:
        log_file.write(response + "\n")
        
def save_response(response, file_name):
    # Save the response to a text file
    with open(file_name + ".txt", "w", encoding="utf-8") as output_file:
        output_file.write(response)
    
    log_response(response)