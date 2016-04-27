import urllib
from bs4 import BeautifulSoup

class Coupon:

    def __init__(self):
        pass

    def couponurl(self, store):
        # Base of URL of coupons page
        base_url = 'http://blog.thiagorodrigo.com.br/cupom-desconto-'
        url = base_url + store

        return url

    def getcoupons(self, store):
        url = self.couponurl(store)

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
                print cod[0]['data-cupom']
