import os 
from dotenv import load_dotenv 
load_dotenv()

class Settings:
    DATABASE_URL=os.getenv("DATABASE_URL","postgresql://postgres:anis1234@db.ihiinpbzsjuotmqiygdd.supabase.co:5432/fastapi_db")
    
settings = Settings()