from models.hotdog import HotDog

class RecipeFactory:
    @staticmethod
    def create_standard(recipe_type: str) -> HotDog:
        recipes = {
            "classic": ["bun", "sausage", "mustard", "ketchup"],
            "spicy": ["bun", "sausage", "jalapenos", "chili"],
            "sweet": ["bun", "sausage", "sweet onion", "relish"]
        }
        if recipe_type not in recipes:
            raise ValueError("Neznámý recept")
        return HotDog(recipe_type.capitalize(), recipes[recipe_type], 50.0)

    @staticmethod
    def create_custom(ingredients: list[str]) -> HotDog:
        return HotDog("Custom", ingredients, 50.0 + len(ingredients) * 5.0)
