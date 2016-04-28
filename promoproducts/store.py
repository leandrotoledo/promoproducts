import urllib
import pdb
import time
import promoproducts
from bs4 import BeautifulSoup

class Store:
    def __init__(self):
        self.stores = promoproducts.get_stores()