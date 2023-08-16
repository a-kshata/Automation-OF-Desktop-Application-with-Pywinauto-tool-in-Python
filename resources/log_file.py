import logging
import sys
import datetime





# filemode='w')
# current_timestamp = datetime.datetime.now()
# log_file_name = 'log_'+str(current_timestamp)+'.log'

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y%m%d%H%M%S")
log_file_name = str(formatted_time)+'log_file.log'
# # Open the log file in append mode and write the timestamp
# with open("log_file.log", "a") as log_file:
#     # log_file='log_'+str(current_time)+'.log'
#  log_file.write(f"[{formatted_time}] Your log message here\n")

logging.basicConfig(filename=log_file_name,

# format='%(asctime)s %(message)s',
encoding='utf_8',

filemode='w')


console_handler = logging.StreamHandler()  # Sends logs to console
formatter = logging.Formatter('%(levelname)s - %(message)s' )
console_handler.setFormatter(formatter)

# Attach handler to the root logger

file_handler = logging.FileHandler(log_file_name)  # Logs to a file named "logfile.log"
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Attach handler to the root logger
logger = logging.getLogger()
logger.addHandler(file_handler)
logger.propagate = False



# #Now we are going to Set the threshold of logger to DEBUG

logger.setLevel(logging.DEBUG)

def log_info(description):
    logger.info(description)
    print(description)