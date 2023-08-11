from dotenv import load_dotenv
import os

load_dotenv()

# loading every .env file in the project
api_key = os.environ.get('MY_API_KEY')
sk = os.getenv('SECRET_KEY')
print(api_key)
print(sk)

