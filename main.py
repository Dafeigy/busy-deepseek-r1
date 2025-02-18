from fastapi import FastAPI, Request
import encodings.utf_8 as utf_8
import time
import asyncio
import json
from fastapi.responses import StreamingResponse
app = FastAPI()


async def stream_generator(model,contents):
    role_message = {
        "id": "fakeLLM",
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": model,
        "choices": [{
            "index": 0,
            "delta": {
                "role": "assistant",
            },
            "finish_reason": None
        }]
    }
    
    yield f"data: {json.dumps(role_message)}\n\n"
    
    for char in contents:
        content_message = {
            "id": "fakeLLM",
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": model,
            "choices": [{
                "index": 0,
                "delta": {
                    "content": char
                },
                "finish_reason": None
            }]
        }
        yield f"data: {json.dumps(content_message,ensure_ascii=False)}\n\n"
        await asyncio.sleep(0.1)  # 添加一个小延迟使输出更自然
    
    done_message = {
        "id": "fakeLLM",
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": model,
        "choices": [{
            "index": 0,
            "delta": {},
            "finish_reason": "stop"
        }]
    }
    yield f"data: {json.dumps(done_message)}\n\n"
    yield 'data: [DONE]\n\n'



@app.post("/v1/chat/completions")
async def read_root(request: Request):
    data = await request.json()
    contents = "服务器繁忙，请稍后再试。"
    is_stream = data['stream']
    model = data['model']
    headers = {'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive'}

    if is_stream:
        print("Streaming")
        return StreamingResponse(stream_generator(model,contents), 
                                 media_type="text/event-stream",
                                 headers=headers)
    else:
        return  {
        "id": f"{int(time.time())}",
        "choices": [
            {
            "message": {
                "role": "assistant",
                "content": f"{contents}",
            },
            "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        },
        "created": 0,
        "model": f"{data['model']}",
        "object": "chat.completion"
    }

