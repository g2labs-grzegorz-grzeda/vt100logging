import logging

VT100_LOGGER: logging.Logger


def vt100logging_initialize(name, is_verbose=False):
    global VT100_LOGGER

    class VT100Formatter(logging.Formatter):

        green = "\x1b[32;20m"
        yellow = "\x1b[33;20m"
        red = "\x1b[31;20m"
        reset = "\x1b[0m"
        format = "%(asctime)s -%(levelname)s- %(message)s"

        FORMATS = {
            logging.INFO: green + format + reset,
            logging.WARNING: yellow + format + reset,
            logging.ERROR: red + format + reset,
        }

        def format(self, record):
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = logging.Formatter(log_fmt)
            return formatter.format(record)
    VT100_LOGGER = logging.getLogger(name)
    VT100_LOGGER.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(VT100Formatter())
    VT100_LOGGER.addHandler(ch)


def I(text):
    VT100_LOGGER.info(text)


def W(text):
    VT100_LOGGER.warning(text)


def E(text):
    VT100_LOGGER.error(text)
