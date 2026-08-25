# Coding Agent Harness CLI

A bare-bones experimental AI agent loop written in Python. It sends a prompt to an LLM via OpenRouter, lets the model read local files using tool calls if needed, and prints the final answer.

This is a starter project built to learn how agent loops and function calling work under the hood, with the goal of expanding it into a full CLI coding assistant.

## Part 1: Agent Loop

### Agent loop:
- Call model
- Execute requested tool
- Return tool result
- Repeat until final answer


## Part 2: Coding Agent Harness CLI

### Coding Agent Harness CLI:
- Wraps that loop in a reusable CLI runtime for coding tasks
- Provides coding tools (read/write/search/list/run tests)
- Enforces guardrails (workspace scope, max steps, error handling)

## Setup

### 1. Install Dependencies
```bash
pip install openai
pip install openrouter
```

### 2. Set Environment Variables
```bash
export OPENROUTER_API_KEY="your_openrouter_api_key"
```

### 3. Usage
```bash
python coding_agent_harness.py -p "Your prompt here"
```
