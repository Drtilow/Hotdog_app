import unittest
from models.hotdog import HotDog
from models.order import Order
from services.discount_strategy import DefaultDiscount

class TestOrderTotalPrice(unittest.TestCase):

    def create_order_with_n_hotdogs(self, n, price_per_hotdog=50.0):
        order = Order()
        for _ in range(n):
            order.add_hotdog(HotDog("TestDog", ["bun", "sausage"], price_per_hotdog))
        return order

    def test_total_price_no_discount(self):
        order = self.create_order_with_n_hotdogs(2)
        total = order.get_total_price(DefaultDiscount())
        expected = 2 * 50.0
        self.assertAlmostEqual(total, expected)

    def test_total_price_with_10_percent_discount(self):
        order = self.create_order_with_n_hotdogs(4)
        subtotal = 4 * 50.0
        expected = subtotal - 0.10 * subtotal
        total = order.get_total_price(DefaultDiscount())
        self.assertAlmostEqual(total, expected)

    def test_total_price_with_25_percent_discount(self):
        order = self.create_order_with_n_hotdogs(8)
        subtotal = 8 * 50.0
        expected = subtotal - 0.25 * subtotal
        total = order.get_total_price(DefaultDiscount())
        self.assertAlmostEqual(total, expected)

if __name__ == '__main__':
    unittest.main()
