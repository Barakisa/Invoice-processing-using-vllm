import os
from dotenv import load_dotenv
from pdf2image import convert_from_path

def generate_images_from_pdf(pdf_file_name):
    load_dotenv()
    img_dir = os.getenv("IMG_DIR")
    os.makedirs(img_dir, exist_ok=True)
    
    image_content = convert_from_path(pdf_file_name)
    images = []
    
    for i, image in enumerate(image_content):
        image_path = os.path.join(img_dir, f"{pdf_file_name}_page_{i+1}.png")
        if image.save(image_path, "PNG"):
            images.append(image_path)
            print(f"Saved: {image_path}")
        else:
            # TODO add error correction, exception handling, graceful process abortion
            print(f"Failed to save image{image_path}")
        

def process_pdf(pdf_file_name):
    images = generate_images_from_pdf(pdf_file_name)
    return images
