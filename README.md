## What TF is this

An alternative when you wanna experience busy-state Deepseek-R1. 

```bash
echo "服务器繁忙，请稍后再试。"
```

## 测试

### 流式输出测试

```bash
curl -X POST https://busy-deepseek-r1.vercel.app/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer Whatever-you-wanna-use" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "hello meow"}],
    "temperature": 0.7,
    "top_p": 1,
    "n": 1,
    "stream": true,
    "stop": null,
    "max_tokens": 2048,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "user": "user-123"
  }'
```

### 非流式输出测试

```bash

curl -X POST https://busy-deepseek-r1.vercel.app/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer Whatever-you-wanna-use" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "hello meow"}],
    "temperature": 0.7,
    "top_p": 1,
    "n": 1,
    "stream": false,
    "stop": null,
    "max_tokens": 2048,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "user": "user-123"
  }'
```

