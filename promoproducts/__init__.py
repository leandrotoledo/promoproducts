# -*- coding: utf-8 -*-

__version__ = '0.1'
__author__ = 'Leandro Muto'
__email__ = 'leandro.muto@gmail.com'

class Promoproducts(object):
    def __init__(self):
        self.stores = ["ponto-frio", "walmart", "ricardo-eletro", "extra"]

    def get_stores(self):
        return self.stores
