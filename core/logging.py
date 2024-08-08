"""pass."""
import logging
import sys

log_format = (
        '%(asctime)s [%(levelname)s]'
        '(%(filename)s).%(funcName)s:%(lineno)d '
        '- %(message)s'
    )
logging.basicConfig(
    format=log_format,
    datefmt='%m-%d %H:%M:%S',
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)],
)
