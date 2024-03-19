import os

def load_dotenv(path: str = "/.env"):
    with open(path) as file:
        for line in file:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=")
                os.environ[key] = value
