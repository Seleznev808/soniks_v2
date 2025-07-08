from src.app import create_app
from src.core.config import settings

app = create_app(settings)
