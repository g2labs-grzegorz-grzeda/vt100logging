from .vt100logging import _initialize, _debug, _info, _warning, _error, _exception


def vt100logging_init(name, is_verbose=False, store_to_log_file=False):
    _initialize(name, is_verbose, store_to_log_file)


def D(text):
    _debug(text)


def I(text):
    _info(text)


def W(text):
    _warning(text)


def E(text):
    _error(text)


def EX(text):
    _exception(text)
