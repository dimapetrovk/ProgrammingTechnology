import os
from dotenv import load_dotenv

def load_from_dot_env():
    """Load environmental variables from .env file"""
    dot_env_default_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

    load_dotenv(dotenv_path=dot_env_default_path)