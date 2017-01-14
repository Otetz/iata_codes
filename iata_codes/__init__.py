import logging
from .cities import IATACodesClient, WrongIATAResultException

try:
    logging.getLogger(__name__).addHandler(logging.NullHandler())
# pragma: no cover
except AttributeError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass


    logging.getLogger(__name__).addHandler(NullHandler())
