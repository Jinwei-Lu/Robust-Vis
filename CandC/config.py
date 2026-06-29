"""Runtime configuration for CandC scripts.

Set API keys through environment variables before running the pipeline.
This file intentionally contains no secrets.
"""

import os


OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

QWEN_BASE_URL = os.getenv(
    "QWEN_BASE_URL",
    "https://dashscope.aliyuncs.com/compatible-mode/v1",
)
QWEN_API_KEY = os.getenv("QWEN_API_KEY", "")
