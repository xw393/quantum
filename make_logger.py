import sys
from logbook import FileHandler, StreamHandler

def make_logger(name, file_name, path):
    log_file_addr = path + '/' + file_name
    new_logger = Logger(name)
    new_logger.handlers.append(StreamHandler(sys.stdout, bubble=True))
    new_logger.handlers.append(FileHandler(log_file_addr, bubble=True, mode='w'))

    return new_logger