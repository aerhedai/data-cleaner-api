import logging
import sys

def setup_logger(name: str = "app") -> logging.Logger:
    """
    Returns a logger instance with a consistent format and level.
    """
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Change to logging.INFO in production
    logger.addHandler(handler)
    logger.propagate = False  # Avoid duplicate logs

    return logger
