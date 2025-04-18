from core.llm import call_llm

system = "You are a helpful assistant."
user = "Explain the difference between inductive and deductive reasoning."

response = call_llm([
    {"role": "system", "content": system},
    {"role": "user", "content": user}
])

print("Response:\n", response)