import urllib
import pdb
import time
from bs4 import BeautifulSoup

class Coupon(object):
    def __init__(self):
        self.valid_coupons = {}
        self.stores = {
            1: "ponto-frio",
            2: "walmart",
            3: "ricardo-eletro",
            4: "extra"
        }

    def couponurl(self, store):
        # Base of URL of coupons page
        base_url = 'http://blog.thiagorodrigo.com.br/cupom-desconto-'
        url = base_url + store

        return url

    def getcoupons(self):
        for i in self.stores:
            store = self.stores[i]
            url = self.couponurl(store)

            # HTML of coupons page
            html = urllib.urlopen(url).read()

            # making a soup
            soup = BeautifulSoup(html)

            # get coupons
            coupons = soup.select('ul.vt-skin-green li.vt-line div.vt-content')

            key = 0
            for coupon in coupons:
                # coupon's code
                cod = coupon.find_all('a', attrs={'data-cupom': True})

                if cod:
                    self.valid_coupons[key] = {
                                                "cod": cod[0]['data-cupom'],
                                                "store": store,
                                                "time": time.strftime("%x")
                                              }
                    key = key + 1

        return self.valid_coupons

    def allstores(self):
        for store in self.stores:
            print self.stores[store]

    def allcoupons(self):
        if self.valid_coupons:
            for i in self.valid_coupons:
                print self.valid_coupons[i]
        else:
            return "There's no coupon"
