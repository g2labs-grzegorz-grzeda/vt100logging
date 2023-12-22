import logging

VT100_LOGGER: logging.Logger


def _initialize(name, is_verbose):
    global VT100_LOGGER

    class VT100Formatter(logging.Formatter):

        green = "\x1b[32;20m"
        yellow = "\x1b[33;20m"
        red = "\x1b[31;20m"
        reset = "\x1b[0m"
        format = "%(asctime)s -%(levelname).1s- %(message)s"

        FORMATS = {
            logging.DEBUG: green + format + reset,
            logging.INFO: green + format + reset,
            logging.WARNING: yellow + format + reset,
            logging.ERROR: red + format + reset,
        }

        def format(self, record):
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = logging.Formatter(log_fmt)
            return formatter.format(record)
    VT100_LOGGER = logging.getLogger(name)
    VT100_LOGGER.setLevel(logging.DEBUG if is_verbose else logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(VT100Formatter())
    VT100_LOGGER.addHandler(ch)


def _debug(text):
    VT100_LOGGER.debug(text)


def _info(text):
    VT100_LOGGER.info(text)


def _warning(text):
    VT100_LOGGER.warning(text)


def _error(text):
    VT100_LOGGER.error(text)
