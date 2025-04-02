from huggingface_hub import snapshot_download
model_path = snapshot_download(repo_id="microsoft/Phi-4-multimodal-instruct")
speech_lora_path = model_path+"/speech-lora"
vision_lora_path = model_path+"/vision-lora"
print(f"speech lora path: {speech_lora_path}")
print(f"vision lora path: {vision_lora_path}")