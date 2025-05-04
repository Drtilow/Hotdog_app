class HotDog:
    def __init__(self, name: str, ingredients: list[str], base_price: float):
        self.name = name
        self.ingredients = ingredients
        self.base_price = base_price

    def __str__(self):
        return f"{self.name}: {', '.join(self.ingredients)} – {self.base_price:.2f} Kč"
