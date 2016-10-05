import logging

try:
    logging.getLogger(__name__).addHandler(logging.NullHandler())
except AttributeError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
    logging.getLogger(__name__).addHandler(NullHandler())
