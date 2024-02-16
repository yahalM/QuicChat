import argparse
import logging
from logging.handlers import RotatingFileHandler
import sys


def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Set up logging configuration for stdout
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.INFO)

    # Set up logging configuration for file with rollover
    log_file = 'example.log'
    file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)
    file_handler.setLevel(logging.INFO)

    # Create a formatter with timestamp and log level
    formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Set the formatter for both handlers
    stdout_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add the new handlers
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)


def main(args):
    message = args.message
    # Log the received message
    logging.info(f'Received message: {message}')
    return 0


if __name__ == "__main__":
    # Set up argument parser with default value for 'message'
    parser = argparse.ArgumentParser(
        description='A program that receives arguments and prints them using the logging library.')
    parser.add_argument('-m', '--message', type=str, nargs='?', default='Hello, World!',
                        help='The message to be printed (default: Hello, World!)')
    arguments = parser.parse_args()

    # Set up logging configuration
    setup_logging()

    # Run the main function with the provided or default message
    sys.exit(main(arguments))
