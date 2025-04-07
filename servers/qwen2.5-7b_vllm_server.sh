#!/bin/bash
vllm serve Qwen/Qwen2-VL-7B-Instruct \
  --task generate \
  --trust_remote_code \
  --host 192.168.1.220 \
  --port 8000 \
  --dtype=half \
  --gpu_memory_utilization=1 \
  --max-num-seqs 2 \
  --max-model-len 32768 \
  --limit-mm-per-prompt image=4,video=0 \
  --chat_template ./qwen.jinja \
  --no-enable-prefix-caching

