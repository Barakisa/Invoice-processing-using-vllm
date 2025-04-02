#!/bin/bash
 HF_TOKEN=$HF_TOKEN vllm serve google/gemma-3-12b-it \
  --task generate \
  --trust_remote_code \
  --host 192.168.1.220 \
  --port 8000 \
  --dtype=half \
  --gpu_memory_utilization=1 \
  --max-num-seqs 2 \
  --max-model-len 32768 \
  --limit-mm-per-prompt image=4,video=0 \
  --chat_template ./template_qwen.jinja \
  --no-enable-prefix-caching

