#!/bin/bash
vllm serve "unsloth/gemma-3-27b-it-unsloth-bnb-4bit" \
  --host 192.168.1.220 \
  --port 8000 \
  --load-format bitsandbytes \
  --dtype=half \
  --gpu_memory_utilization=1 \
  --max-model-len 2048 \
  --task generate \
  --trust_remote_code \
  --max-num-seqs 1 \
  --limit-mm-per-prompt image=1,video=0 \
  --no-enable-prefix-caching
