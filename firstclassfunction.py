
import logging

logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arugments {}'.format(func.__name__,args))
        print(func(*args))
    return log_func
