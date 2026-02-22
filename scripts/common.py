import logging

# Configurazione base log file
LOG_FILE = '../logs/LOG.txt'

logging.basicConfig(
    filename=LOG_FILE,
    filemode='a',           # append
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def log(msg, level="info"):
    if level == "info":
        logging.info(msg)
    elif level == "warning":
        logging.warning(msg)
    elif level == "error":
        logging.error(msg)
    else:
        logging.debug(msg)