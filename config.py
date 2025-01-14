import os
import logging

from dotenv import load_dotenv


load_dotenv()  # parse environment variables from .env file

DEBUG = os.getenv('DEBUG', False)
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    logging.error("BOT_TOKEN is not defined neither in .env file nor in environment variables")
    quit()

SQLALCHEMY_URL = os.getenv('SQLALCHEMY_URL')
