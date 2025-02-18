from fastapi import FastAPI, Request
import time
import asyncio
from fastapi.responses import StreamingResponse
app = FastAPI()


async def stream_generator(model,contents):
    response_text = [{"id":"fakeLLM","object":"chat.completion.chunk","created":1145141919810,"model":f"{model}","choices":[{"index":0,"delta":{"content":"","reasoning_content":None,"role":"assistant"},"finish_reason":None,"content_filter_results":{"hate":{"filtered":False},"self_harm":{"filtered":False},"sexual":{"filtered":False},"violence":{"filtered":False}}}],"system_fingerprint":"","usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0}}]
    response_text += [{"id":"fakeLLM","object":"chat.completion.chunk","created":1145141919810,"model":f"{model}","choices":[{"index":0,"delta":{"content":f"{content}","reasoning_content":None},"finish_reason":None,"content_filter_results":{"hate":{"filtered":False},"self_harm":{"filtered":False},"sexual":{"filtered":False},"violence":{"filtered":False}}}],"system_fingerprint":"","usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0}} for content in contents]
    response_text.append({"id":"fakeLLM","object":"chat.completion.chunk","created":1145141919810,"model":f"{model}","choices":[{"index":0,"delta":{"content":"","reasoning_content":None},"finish_reason":"stop","content_filter_results":{"hate":{"filtered":False},"self_harm":{"filtered":False},"sexual":{"filtered":False},"violence":{"filtered":False}}}],"system_fingerprint":"","usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0}})
    response_text.append("[DONE]")
    for each in response_text:
        yield str(each) + '\n\n'
        await asyncio.sleep(0.2)


@app.post("/v1/chat/completions")
async def read_root(request: Request):
    data = await request.json()
    contents = "服务器繁忙，请稍后再试。"
    is_stream = data['stream']
    model = data['model']
    time.sleep(2)
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

