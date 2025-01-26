import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = 'logs'

# Ensure path is correct relative to root or desired directory
logs_path = os.path.join(os.getcwd(), log_dir, LOG_FILE)

# Create the log directory if it doesn't exist
os.makedirs(os.path.join(os.getcwd(), log_dir), exist_ok=True)

# Basic logging configuration
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)