# social_book/utils/db_connector.py
from django.conf import settings
from sqlalchemy import create_engine, text

def get_engine():
    db = settings.DATABASES['default']
    DATABASE_URL = f"postgresql://{db['USER']}:{db['PASSWORD']}@{db['HOST']}:{db['PORT']}/{db['NAME']}"
    return create_engine(DATABASE_URL)