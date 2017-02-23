import logging


class Logger():

    def __init__(self, mod_name):
        self.log_level = "INFO"
        self.mod_name = mod_name
        self.logger = logging.getLogger(mod_name)
        self.logger.setLevel(self.log_level)
        self.logger.addHandler(self._GetConsoleHandler())

    def _GetConsoleHandler(self):
        formatter = logging.Formatter("%(asctime)s %(name)s: %(message)s")
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        return ch

    def debug(self, buf):
        self.logger.debug(buf)

    def info(self, buf):
        self.logger.info(buf)

    def warn(self, buf):
        self.logger.warn(buf)

    def error(self, buf):
        self.logger.error(buf)

    def critical(self, buf):
        self.logger.critical(buf)
