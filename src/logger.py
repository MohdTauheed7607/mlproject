import logging
import os
from datetime import datetime


LOG_DIR="logs"
os.makedirs(LOG_DIR,exist_ok=True)

log_file=f"{datetime.now().strftime('%h_%m_%Y_%H_%M_%S')}.log"

log_file_path=os.path.join(LOG_DIR,log_file)

logging.basicConfig(filename=log_file_path,
                    level=logging.INFO,
format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")

