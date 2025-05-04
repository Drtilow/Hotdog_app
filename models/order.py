class Order:
    def __init__(self):
        self.hotdogs = []

    def add_hotdog(self, hotdog):
        self.hotdogs.append(hotdog)

    def get_total_price(self, discount_strategy):
        total = sum(h.base_price for h in self.hotdogs)
        return total - discount_strategy.calculate_discount(self)
