from dotenv import load_dotenv
import os
import logging
from datetime import datetime

load_dotenv()

OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')
SLACK_WEBHOOK_ENDPOINT = os.getenv('SLACK_WEBHOOK_ENDPOINT')

LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_path = os.path.join(LOG_DIR, f'log_{timestamp}.log')

LOG_LEVEL = logging.INFO

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info(f"Logging initialized. Log file: {log_path}")