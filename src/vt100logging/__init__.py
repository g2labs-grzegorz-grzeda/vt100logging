from .vt100logging import _initialize, _debug, _info, _warning, _error


def vt100logging_init(name, is_verbose=False):
    _initialize(name, is_verbose)


def D(text):
    _debug(text)


def I(text):
    _info(text)


def W(text):
    _warning(text)


def E(text):
    _error(text)
