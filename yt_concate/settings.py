import os
from dotenv import load_dotenv

load_dotenv()
API_KEY: str | None = os.getenv('YOUTUBE_API_KEY')
print("API_KEY in settings.py:", API_KEY)

# Print all environment variables
print("All environment variables:", os.environ)

