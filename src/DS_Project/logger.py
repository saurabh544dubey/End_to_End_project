import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%M_%H_%S')}.log"

# A .log file will be created
# It'll store the current datetime in the specifies format 

log_path = os.path.join(os.getcwd() , 'logs' , LOG_FILE)

# creating a folder
os.makedirs(log_path , exist_ok=True)  
# exist_ok is used if the folder is already present then use it

# writing complete path by combining both
LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)