import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("ENDPOINT")
    KEY = os.getenv("SUBSCRIPTION_KEY")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")



print(f"ENDPOINT: {Config.ENDPOINT}")
print(f"SUBSCRIPTION_KEY: {Config.KEY}")
print(f"AZURE_STORAGE_CONNECTION_STRING: {Config.AZURE_STORAGE_CONNECTION_STRING}")
print(f"CONTAINER_NAME: {Config.CONTAINER_NAME}")
