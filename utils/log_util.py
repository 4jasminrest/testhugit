import  logging
import os.path
from logging.handlers import *

logger = logging.getLogger(__name__)

log_path = os.path.dirname(os.path.abspath(__file__))