from euriai import EuriaiClient

def get_chat_model(api_key: str = "euri-bedc20059d7c760ff40a2ed4706ac66cb2c2664b5006d8efaedd198298fd005f", model: str = "gpt-4.1-nano"):
    client = EuriaiClient(
        api_key=api_key,
        model=model
    )
    return client

def ask_chat_model(client: EuriaiClient, prompt: str, temperature: float = 0.7, max_tokens: int = 300):
    response = client.generate_completion(
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response
