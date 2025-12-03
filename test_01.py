import openai

openai.api_key = "api key here"
def generate_text(prompt, model="gpt-4.1-mini"):
        response = openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
        return response.choices[0].message.content

prompt = "Write a short paragraph about the benefits of AI in healthcare."
print(generate_text(prompt))