import ollama

def merchant_chat(model, messages):
    try:
        response = ollama.chat(model=model, messages=messages)
        return response
    except Exception as e:
        return f"Error connecting to Ollama: {e}"