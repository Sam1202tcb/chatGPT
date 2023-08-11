from dotenv import load_dotenv
from appp import BOSS_S_K
import os

load_dotenv()

# loading every .env file in the project
api_key = os.environ.get('MY_API_KEY')
sk = os.getenv('SECRET_KEY')
B_S_K = BOSS_S_K
print(api_key)
print(B_S_K)
print(sk)

