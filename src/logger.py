# logging is  important for tracking events that happen when application runs which helps in debugging and monitoring the application behaviour 
# os provide the functionality to read and write
import logging 
import os 
from datetime import datetime 

# how should the log file should look like
LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%s')}.log"
# creating the log path
logs_path=os.path.join(os.getcwd(),'logs',LOG_FILE)
# creating the directory 
os.makedirs(logs_path,exist_ok=True)
# Final Log path 
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# how should the inside logger should look like 
logging.basicConfig(
    filename=LOG_FILE_PATH,
    formate="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

