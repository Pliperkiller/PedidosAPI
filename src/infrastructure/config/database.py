import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables del archivo .env

DATABASE_URI = os.getenv("DATABASE_URI")
