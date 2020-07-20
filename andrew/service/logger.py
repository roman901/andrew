import os
import logging
from logging import Logger

from andrew.service import Service


class LoggerService(Service):
    logger: Logger = logging.getLogger()

    def __init__(self):
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        self.logger.addHandler(sh)

        if bool(int(os.environ.get('DEBUG', '0'))):
            self.logger.setLevel(logging.DEBUG)
