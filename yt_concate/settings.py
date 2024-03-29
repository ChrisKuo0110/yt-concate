import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
API_KEY = os.getenv('API_KEY')

# Code of your application, which uses environment variables (e.g. from `os.environ` or `os.getenv`) as if they came
# from the actual environment.
