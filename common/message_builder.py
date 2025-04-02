import base64
import cv2


# dynamically build content entries for open ai api
# its called urls, even though its actually file content with tags
# just how open ai api works 
def build_base64_urls(images):
    urls = []
    for image in images:
        img = cv2.imread(image)
        jpg_img = cv2.imencode('.png', img)
        b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
        urls.append(f"data:image/png;base64,{b64_string}")
    return urls

# build full user message content for the first prompt
def build_user_image_content(images):
    # to use on lan offline, you need to pass file itself rather than (deep)link somewhere
    # TODO investigate url on lan 
    image_urls = build_base64_urls(images)
    
    image_content = []
    for image_url in image_urls:
        image_content.append({"type": "image_url", "image_url": {"url": image_url}})
    return image_content

# user prompt is based on the size of the pdf file
def build_user_text_content(images):
    # TODO analize, which is better:
    # Analize image {i} or Whats in image {i}
    text = ""
    for i, _ in enumerate(images):
        text+=f"Whats in image {i+1}? "

    # NOTE: The prompt formatting with the image token `<image>` is not needed
    # since the prompt will be processed automatically by the API server.        
    text_content = [{"type": "text", "text": text}]
    return text_content

def build_user_message(images):
    user_text_content = build_user_text_content(images)
    user_image_content = build_user_image_content(images)
    
    user_message_content = user_text_content + user_image_content
    
    message = {"role": "user", "content": user_message_content}
    return message

def build_system_message():
    return {"role": "system", "content": [{"type": "text", "text": "You are a master accountant, and your job is to parse images to determine invoice id, invoice date, invoice sub-total, invoice total tax, invoice total (subtotal + tax), invoice items (item description, item qty, item unit price, item tax (if applicable), item price). You love json format, and you hate explaining things, which means, that you return only the data in json format, completely bare from anything else."}]}
