import unittest
from models.hotdog import HotDog
from models.order import Order
from services.discount_strategy import DefaultDiscount

class TestDefaultDiscount(unittest.TestCase):

    def create_order_with_n_hotdogs(self, n, price_per_hotdog=50.0):
        order = Order()
        for _ in range(n):
            order.add_hotdog(HotDog("TestDog", ["bun", "sausage"], price_per_hotdog))
        return order

    def test_no_discount_for_1_or_2_hotdogs(self):
        for count in [1, 2]:
            order = self.create_order_with_n_hotdogs(count)
            discount = DefaultDiscount().calculate_discount(order)
            self.assertEqual(discount, 0.0, f"Expected no discount for {count} hotdog(s)")

    def test_10_percent_discount_for_3_to_5_hotdogs(self):
        for count in [3, 4, 5]:
            order = self.create_order_with_n_hotdogs(count)
            expected = 0.10 * count * 50.0
            discount = DefaultDiscount().calculate_discount(order)
            self.assertAlmostEqual(discount, expected, msg=f"Expected 10% discount for {count} hotdogs")

    def test_25_percent_discount_for_6_or_more_hotdogs(self):
        for count in [6, 8, 10]:
            order = self.create_order_with_n_hotdogs(count)
            expected = 0.25 * count * 50.0
            discount = DefaultDiscount().calculate_discount(order)
            self.assertAlmostEqual(discount, expected, msg=f"Expected 25% discount for {count} hotdogs")

if __name__ == '__main__':
    unittest.main()
