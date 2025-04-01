from openai import OpenAI
import sys
import cv2
import base64
from dotenv import load_dotenv

if len(sys.argv) < 2:
    print("Usage: python vllm_1image.py <1-4>")
    sys.exit(1)

x = int(sys.argv[1])
match x:
    case 1:
        image_url = "https://upload.wikimedia.org/wikipedia/commons/d/da/2015_Kaczka_krzy%C5%BCowka_w_wodzie_%28samiec%29.jpg"
    case 2:
        #break for some reason. Too high resolution?
        image_url = "https://upload.wikimedia.org/wikipedia/commons/7/77/002_The_lion_king_Snyggve_in_the_Serengeti_National_Park_Photo_by_Giles_Laurent.jpg"
    case 3:
        image_url = "file:///home/barakisa/Programming/ai/vllm/Invoice-5411EDE4-0005.png"
    case 4:
        img = cv2.imread('Invoice-5411EDE4-0005.png')
        jpg_img = cv2.imencode('.png', img)
        b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
        image_url = f"data:image/png;base64,{b64_string}"
    case _:
        image_url = "file:///home/barakisa/Programming/ai/vllm/invoice-1319568.png"


openai_api_key = os.getenv("API_KEY")
openai_api_base = os.getenv("API_BASE")

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

chat_response = client.chat.completions.create(
    model="Qwen/Qwen2-VL-7B-Instruct",
    messages=[{
        "role": "user",
        "content": [
            # NOTE: The prompt formatting with the image token `<image>` is not needed
            # since the prompt will be processed automatically by the API server.
            {"type": "text", "text": "Whats in this image?"},
            {"type": "image_url", "image_url": {"url": image_url}},
        ],
    }],
)
print("Chat completion output:", chat_response.choices[0].message.content)