import openai
import os

# Set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Replace with your fine-tuned model ID after fine-tuning completes
fine_tuned_model = "ft:gpt-3.5-turbo:your-org:your-model-id"

prompts = [
    "Mujhe ek chai pilao.",
    "Weekend ka kya plan hai?",
    "Koi funny video suggest kar."
]

for prompt in prompts:
    response = openai.chat.completions.create(
        model=fine_tuned_model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=50
    )
    print(f"Prompt: {prompt}")
    print(f"Response: {response.choices[0].message.content}\n")