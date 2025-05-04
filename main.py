from models.order import Order
from services.recipe_factory import RecipeFactory
from services.discount_strategy import DefaultDiscount

def display_menu():
    print("\n--- HOT DOG MENU ---")
    print("1. Classic (bun, sausage, mustard, ketchup)")
    print("2. Spicy (bun, sausage, jalapenos, chili)")
    print("3. Sweet (bun, sausage, sweet onion, relish)")
    print("4. Vlastní recept")
    print("5. Konec objednávky\n")

def get_custom_ingredients():
    print("Zadej ingredience pro vlastní hot dog (odděluj čárkami):")
    input_str = input("Např. bun, sausage, mustard, pickles: ")
    return [i.strip() for i in input_str.split(",")]

def main():
    order = Order()
    discount = DefaultDiscount()

    while True:
        display_menu()
        choice = input("Vyber číslo z menu: ")

        if choice == "1":
            hotdog = RecipeFactory.create_standard("classic")
        elif choice == "2":
            hotdog = RecipeFactory.create_standard("spicy")
        elif choice == "3":
            hotdog = RecipeFactory.create_standard("sweet")
        elif choice == "4":
            ingredients = get_custom_ingredients()
            hotdog = RecipeFactory.create_custom(ingredients)
        elif choice == "5":
            break
        else:
            print("Neplatná volba.")
            continue

        order.add_hotdog(hotdog)
        print(f"Přidán: {hotdog}")

    if not order.hotdogs:
        print("Nebyla vytvořena žádná objednávka.")
        return

    total = order.get_total_price(discount)
    print(f"\nPočet hot dogů: {len(order.hotdogs)}")
    print(f"Celková cena se slevou: {total:.2f} Kč")

    # Volitelně: výběr způsobu platby
    payment_method = input("Chceš platit kartou (K) nebo hotově (H)? ").strip().lower()
    if payment_method == "k":
        print("Probíhá platba kartou...")
    elif payment_method == "h":
        print("Probíhá platba v hotovosti...")
    else:
        print("Neznámý způsob platby.")

    print("\nDěkujeme za nákup!")

if __name__ == "__main__":
    main()
