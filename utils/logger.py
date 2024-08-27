import logging
from logging.handlers import TimedRotatingFileHandler
import os
import functools
import time

def setup_logger(name, log_folder='logs'):
    # Create the log folder if it doesn't exist
    os.makedirs(log_folder, exist_ok=True)

    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create a timed rotating file handler
    log_file = os.path.join(log_folder, f'{name}.log')
    file_handler = TimedRotatingFileHandler(
        log_file,
        when='midnight',
        interval=1,
        backupCount=30,  # Keep logs for 30 days
        encoding='utf-8'
    )
    
    # Set the log format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(file_handler)

    return logger

# Instantiate the logger
logger = setup_logger('my_app')

def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            logger.info(f"Function '{func.__name__}' executed successfully in {execution_time:.4f} seconds.")
            return result
        except Exception as e:
            end_time = time.time()
            execution_time = end_time - start_time
            logger.exception(f"Error in '{func.__name__}' after {execution_time:.4f} seconds: {str(e)}")
            raise
    return wrapper
