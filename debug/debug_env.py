import os
from dotenv import load_dotenv

print("--- Debugging Environment ---")
print(f"Current Working Directory: {os.getcwd()}")

env_path = os.path.join(os.getcwd(), ".env")
if os.path.exists(env_path):
    print(f".env file found at: {env_path}")
    with open(env_path, "r") as f:
        content = f.read()
        print(f"Content of .env:\n'{content}'")
else:
    print(".env file NOT found!")

print("\nLoading dotenv...")
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    print(f"GOOGLE_API_KEY found: {api_key[:5]}...{api_key[-5:]}")
else:
    print("GOOGLE_API_KEY NOT found in environment.")
