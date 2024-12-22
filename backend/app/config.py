from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    blip_model : str = "Salesforce/blip-image-captioning-large"

settings = Settings()