# Environment Variables
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SHOPIFY_API_KEY: str
    SHOPIFY_API_SECRET: str
    LLM_API_KEY: str  # Or whichever AI provider you use
    
    class Config:
        env_file = ".env"

settings = Settings()