@echo off
for /L %%i in (1,1,10) do (
    echo Running command iteration %%i
    python ./vllm_1image.py 4
)