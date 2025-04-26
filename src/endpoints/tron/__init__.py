import os

from tronpy import Tron
from tronpy.providers import HTTPProvider

tron = Tron(HTTPProvider(api_key=os.environ.get("TRON_GRID_API_KEY")))
