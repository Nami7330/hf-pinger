from gradio_client import Client
import os

token = os.environ.get("HF_TOKEN")
if not token:
    raise ValueError("HF_TOKEN missing!")

client = Client("Zarwa7/calculator-backend", hf_token=token)
result = client.predict(user_input="2+2", api_name="/chatbot_calculator_logic")
print("Ping result:", result)
