#!/bin/bash
vllm serve 'microsoft/Phi-4-multimodal-instruct' \
    --dtype half \
    --trust-remote-code \
    --host 192.168.1.220 \
    --port 8000 \
    --gpu_memory_utilization=1 \
    --max-num-seqs 2 \
    --max-model-len 50000 \
    --enable-lora \
    --max-lora-rank 320 \
    --lora-extra-vocab-size 0 \
    --limit-mm-per-prompt audio=0,image=5 \
    --chat_template ./phi4.jinja \
    --max-loras 1 \
    --lora-extra-vocab-size 512 \
    --lora-modules \
        vision=/home/barakisa/.cache/huggingface/hub/models--microsoft--Phi-4-multimodal-instruct/snapshots/0ae13bd0f508a906f8b8288fc5e36b01b903c132/vision-lora
