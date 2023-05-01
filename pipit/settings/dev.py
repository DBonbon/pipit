from .base import *

ALLOWED_HOSTS = ["*", "138.197.184.214",]
try:
    from .local import *
except ImportError:
    pass
