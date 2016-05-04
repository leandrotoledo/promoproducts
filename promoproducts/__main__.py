from coupon import Coupon
from store import Store

import urllib
from bs4 import BeautifulSoup

c = Coupon()

c.get_coupons()
print c.all_coupons()

s = Store()

print s.call_me()
