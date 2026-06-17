from dotenv import load_dotenv
from pathlib import Path
from imagekitio import ImageKit
import os

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

imagekit = ImageKit(
    public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    url_endpoint=os.getenv("IMAGEKIT_URL")
)
