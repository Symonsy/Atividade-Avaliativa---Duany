from uuid import uuid4
from datetime import datetime

db = {}

def generate_id():
    return str(uuid4())
