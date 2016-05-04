"""This module contains an object that represents Tests for Coupon class"""

import sys
import unittest

sys.path.append('.')

from promoproducts.coupon import Coupon


class CouponTest(unittest.TestCase):
    """This object represents Tests for Coupon class"""

    def test_new_coupon(self):
        coupon = Coupon()

        self.assertTrue(isinstance(coupon.valid_coupons, list))
        self.assertTrue(isinstance(coupon.stores, list))

        self.assertTrue("ponto-frio" in coupon.stores)


if __name__ == '__main__':
    unittest.main()
