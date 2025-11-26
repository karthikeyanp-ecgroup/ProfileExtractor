from openai import OpenAI
client = OpenAI(api_key="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")

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(resp.choices[0].message.content)
