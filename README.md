## What TF is this

An alternative when you wanna experience busy-state Deepseek-R1. 

```bash
echo "服务器繁忙，请稍后再试。"
```

## 流失传输

```bash
data: {"id":"019516ecd5791194e7ce760dcc227413","object":"chat.completion.chunk","created":1739846374,"model":"Qwen/Qwen2.5-Coder-7B-Instruct","choices":[{"index":0,"delta":{"content":"","reasoning_content":null,"role":"assistant"},"finish_reason":null,"content_filter_results":{"hate":{"filtered":false},"self_harm":{"filtered":false},"sexual":{"filtered":false},"violence":{"filtered":false}}}],"system_fingerprint":"","usage":{"prompt_tokens":35,"completion_tokens":0,"total_tokens":35}}

data: {"id":"019516ecd5791194e7ce760dcc227413","object":"chat.completion.chunk","created":1739846374,"model":"Qwen/Qwen2.5-Coder-7B-Instruct","choices":[{"index":0,"delta":{"content":" 当","reasoning_content":null},"finish_reason":null,"content_filter_results":{"hate":{"filtered":false},"self_harm":{"filtered":false},"sexual":{"filtered":false},"violence":{"filtered":false}}}],"system_fingerprint":"","usage":{"prompt_tokens":35,"completion_tokens":1,"total_tokens":36}}

data: {"id":"019516ecd5791194e7ce760dcc227413","object":"chat.completion.chunk","created":1739846374,"model":"Qwen/Qwen2.5-Coder-7B-Instruct","choices":[{"index":0,"delta":{"content":"然","reasoning_content":null},"finish_reason":null,"content_filter_results":{"hate":{"filtered":false},"self_harm":{"filtered":false},"sexual":{"filtered":false},"violence":{"filtered":false}}}],"system_fingerprint":"","usage":{"prompt_tokens":35,"completion_tokens":2,"total_tokens":37}}

data: {"id":"019516ecd5791194e7ce760dcc227413","object":"chat.completion.chunk","created":1739846374,"model":"Qwen/Qwen2.5-Coder-7B-Instruct","choices":[{"index":0,"delta":{"content":"！","reasoning_content":null},"finish_reason":null,"content_filter_results":{"hate":{"filtered":false},"self_harm":{"filtered":false},"sexual":{"filtered":false},"violence":{"filtered":false}}}],"system_fingerprint":"","usage":{"prompt_tokens":35,"completion_tokens":3,"total_tokens":38}}

...

data: {"id":"019516ecd5791194e7ce760dcc227413","object":"chat.completion.chunk","created":1739846374,"model":"Qwen/Qwen2.5-Coder-7B-Instruct","choices":[{"index":0,"delta":{"content":"帮助","reasoning_content":null},"finish_reason":null,"content_filter_results":{"hate":{"filtered":false},"self_harm":{"filtered":false},"sexual":{"filtered":false},"violence":{"filtered":false}}}],"system_fingerprint":"","usage":{"prompt_tokens":35,"completion_tokens":255,"total_tokens":290}}

data: {"id":"019516ecd5791194e7ce760dcc227413","object":"chat.completion.chunk","created":1739846374,"model":"Qwen/Qwen2.5-Coder-7B-Instruct","choices":[{"index":0,"delta":{"content":"！","reasoning_content":null},"finish_reason":null,"content_filter_results":{"hate":{"filtered":false},"self_harm":{"filtered":false},"sexual":{"filtered":false},"violence":{"filtered":false}}}],"system_fingerprint":"","usage":{"prompt_tokens":35,"completion_tokens":256,"total_tokens":291}}

data: {"id":"019516ecd5791194e7ce760dcc227413","object":"chat.completion.chunk","created":1739846374,"model":"Qwen/Qwen2.5-Coder-7B-Instruct","choices":[{"index":0,"delta":{"content":"","reasoning_content":null},"finish_reason":"stop","content_filter_results":{"hate":{"filtered":false},"self_harm":{"filtered":false},"sexual":{"filtered":false},"violence":{"filtered":false}}}],"system_fingerprint":"","usage":{"prompt_tokens":35,"completion_tokens":256,"total_tokens":291}}

data: [DONE]
```