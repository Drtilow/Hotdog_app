# services/discount_strategy.py

class DiscountStrategy:
    def calculate_discount(self, order):
        raise NotImplementedError("Tato metoda musí být implementována")

class DefaultDiscount(DiscountStrategy):
    def calculate_discount(self, order):
        count = len(order.hotdogs)
        if count >= 6:
            return 0.25 * sum(h.base_price for h in order.hotdogs)  # 25 % sleva
        elif count >= 3:
            return 0.10 * sum(h.base_price for h in order.hotdogs)  # 10 % sleva
        else:
            return 0.0
