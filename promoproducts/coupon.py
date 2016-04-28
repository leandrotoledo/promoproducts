import urllib
import pdb
import time
from bs4 import BeautifulSoup
from promoproducts import Promoproducts

class Coupon(object):
    def __init__(self):
        self.valid_coupons = []
        self.stores = Promoproducts().get_stores()

    def coupon_url(self, store):
        # Base of URL of coupons page
        base_url = 'http://blog.thiagorodrigo.com.br/cupom-desconto-'
        url = base_url + store

        return url

    def get_coupons(self):
        for store in self.stores:
            url = self.coupon_url(store)

            # HTML of coupons page
            html = urllib.urlopen(url).read()

            # making a soup
            soup = BeautifulSoup(html)

            # get coupons
            coupons = soup.select('ul.vt-skin-green li.vt-line div.vt-content')

            for coupon in coupons:
                # coupon's code
                cod = coupon.find_all('a', attrs={'data-cupom': True})

                if cod:
                    val = {
                            "cod": cod[0]['data-cupom'],
                            "store": store,
                            "time": time.strftime("%x")
                          }
                    self.valid_coupons.append(dict(val))

        return self.valid_coupons

    def all_coupons(self):
        if self.valid_coupons:
            for item in self.valid_coupons:
                print item
        else:
            return "There's no coupon"
