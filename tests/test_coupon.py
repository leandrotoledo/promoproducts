"""This module contains an object that represents Tests for Coupon class"""

import sys
import unittest

sys.path.append('.')

from promoproducts.coupon import Coupon
from promoproducts.store import Store, Extra


class CouponTest(unittest.TestCase):
    """This object represents Tests for Coupon class"""

    def test_new_coupon(self):
        coupon = Coupon()

        self.assertTrue(isinstance(coupon.valid_coupons, list))
        self.assertTrue(isinstance(coupon.stores, list))

        self.assertTrue("ponto-frio" in coupon.stores)

class StoreTest(unittest.TestCase):

    def test_get_departments(self):
        store = Store('http://www.extra.com.br')
        departments = store.get_departments([])

        self.assertEqual(departments[0]['department_name'],
                         'Beleza e Sa\xc3\xbade')
        self.assertEqual(departments[0]['department_href'],
                         'http://www.extra.com.br/BelezaSaude/?Filtro=C102&nid=200669')

    def test_get_categories(self):
        store = Store('http://www.extra.com.br')
        departments = store.get_departments([])
        category = store.get_categories(departments[0]['department_href'])

        self.assertEqual(category[0]['category_href'],
                         'http://www.extra.com.br/BelezaSaude/cuidadosfemininos/?Filtro=C102_C105')

        self.assertEqual(category[0]['category_name'],
                         'Cuidados Femininos')


class ExtraTest(unittest.TestCase):

    def test_get_departments(self):
        extra = Extra('http://www.extra.com.br')
        departments = extra.get_departments([])

        self.assertEqual(departments[0]['department_name'],
                         'Beleza e Sa\xc3\xbade')

    def test_get_categories(self):
        store = Store('http://www.extra.com.br')
        departments = store.get_departments([])
        category = store.get_categories(departments[0]['department_href'])

        self.assertEqual(category[0]['category_href'],
                         'http://www.extra.com.br/BelezaSaude/cuidadosfemininos/?Filtro=C102_C105')

        self.assertEqual(category[0]['category_name'],
                         'Cuidados Femininos')

if __name__ == '__main__':
    unittest.main()
