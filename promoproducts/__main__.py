from coupon import Coupon
from store import *

import urllib
from bs4 import BeautifulSoup

c = Coupon()

c.get_coupons()
print c.all_coupons()

e = Extra()

print e.call_me()
