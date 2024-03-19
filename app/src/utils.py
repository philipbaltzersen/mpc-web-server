import os

def load_dotenv():
    with open("/.env") as file:
        for line in file:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=")
                os.environ[key] = value
