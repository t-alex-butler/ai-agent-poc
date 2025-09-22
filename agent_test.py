from openai import OpenAI

# Create client (make sure you set your API key first!)
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",   # lightweight but capable model
    messages=[
        {"role": "system", "content": "You are a helpful AI agent."},
        {"role": "user", "content": "Hello, what can you do?"}
    ]
)

print(response.choices[0].message.content)

