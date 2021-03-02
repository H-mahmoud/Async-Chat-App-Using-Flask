from dotenv import load_dotenv
from pathlib import Path  
import os


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config:

    DEBUG = os.getenv('DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')
    MYSQL_HOST = "127.0.0.1"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "chat_users"