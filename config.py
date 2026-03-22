import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ.get("SUBSTACK_EMAIL", "")
PASSWORD = os.environ.get("SUBSTACK_PASSWORD", "")
