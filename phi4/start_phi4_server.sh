#!/bin/bash
vllm serve \
    --model 'microsoft/Phi-4-multimodal-instruct' \
    --dtype auto \
    --trust-remote-code \
    --max-model-len 131072 \
    --enable-lora \
    --max-lora-rank 320 \
    --lora-extra-vocab-size 0 \
    --limit-mm-per-prompt audio=3,image=3 \
    --max-loras 2 \
    --lora-modules speech=<path to speech lora folder> vision=<path to vision lora folder>
