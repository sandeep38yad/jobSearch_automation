import logging
import os

class Logger:
    @staticmethod
    def get_logger(logger_name='automation', log_file=r'logs\jobSearch.log', log_level=logging.DEBUG):

        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)

        # Create a file handler
        file_handler = logging.FileHandler(log_file, encoding = 'utf-8')  # Ensure it appends to the file
        file_handler.setLevel(log_level)

        # Create a formatter and set it for the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)


        return logger

