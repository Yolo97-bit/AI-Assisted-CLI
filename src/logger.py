import logging
import sys
import os

def setup_logger(name: str = "AI_Wizard_App") -> logging.Logger:
    """
    Configures and returns a standard enterprise logger.
    Logs to both console (stdout) and a file (app.log).
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent adding multiple handlers if logger is already configured
    if logger.hasHandlers():
        return logger

    # Formatter: Standard enterprise format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Handler 1: Console (StreamHandler)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Handler 2: File (FileHandler)
    try:
        file_handler = logging.FileHandler("app.log", mode='a', encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except IOError as e:
        print(f"Warning: Could not create log file. Logging to console only. Error: {e}")

    return logger

# Create a singleton logger instance
logger = setup_logger()
