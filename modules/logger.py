import logging

logging.basicConfig(filename='data/app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

def debug(message):
    logging.debug(message)

def info(message):
    logging.info(message)

def warning(message):
    logging.warning(message)

def error(message):
    logging.error(message)

def critical(message):
    logging.critical(message)