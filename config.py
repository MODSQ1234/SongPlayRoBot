import os
API_ID = int(os.getenv("27940595"))
API_HASH = os.getenv("89a1fa73f8cc1e1002044e1e4e2b7b65")
BOT_TOKEN = os.getenv("6336222828:AAHKY7m9H9VMaD7GKNzg0YBw2dhuQ3OqB1E")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("1098027220", "").split()})
