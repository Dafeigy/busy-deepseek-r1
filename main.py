from fastapi import FastAPI, Request
import time
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost:3000",  # 允许的来源
    "http://127.0.0.1:3000",
    "http://localhost:8080",  # 如果你的NextChat运行在8080端口
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/v1/chat/completions")
async def read_root(request: Request):
    data = await request.json()
    print(data)
    return {
        "id": f"{int(time.time())}",
        "choices": [
            {
            "message": {
                "role": "assistant",
                "content": "<string>",
                "reasoning_content": "<string>"
            },
            "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 123,
            "completion_tokens": 123,
            "total_tokens": 123
        },
        "created": 123,
        "model": f"{data['model']}",
        "object": "chat.completion"
    }

