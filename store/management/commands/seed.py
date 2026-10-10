import random
from django.core.management.base import BaseCommand
from store.models import Product
DATA = {
 "Electronics": [("Wireless Headphones",2499),("Smart Watch",3999),("Bluetooth Speaker",1799),("Power Bank 20000mAh",1299),("Gaming Mouse",899)],
 "Fashion": [("Denim Jacket",1999),("Cotton T-Shirt",499),("Running Shoes",2799),("Pullover Hoodie",1499),("Formal Shirt",999)],
 "Home": [("Table Lamp",799),("Wall Clock",649),("Cushion Cover Set",599),("Cotton Bedsheet",1099),("Curtain Pair",1299)],
 "Beauty": [("Face Wash",249),("Moisturizer",399),("Matte Lipstick",349),("Eau de Perfume",899),("Hair Dryer",1199)],
 "Sports": [("Yoga Mat",599),("Dumbbell Set",1999),("Football",699),("Cricket Bat",1499),("Skipping Rope",199)],
 "Books": [("Python Crash Course",599),("Clean Code",749),("Atomic Habits",399),("The Alchemist",299),("Django for Beginners",499)],
 "Toys": [("Building Blocks",899),("RC Car",1299),("1000-Piece Puzzle",499),("Teddy Bear",599),("Family Board Game",799)],
 "Kitchen": [("Air Fryer",4499),("Mixer Grinder",2999),("Non-stick Pan",899),("Chef Knife Set",1099),("Steel Water Bottle",349)],
 "Grocery": [("Almonds 1kg",899),("Green Tea Box",299),("Basmati Rice 5kg",749),("Olive Oil 1L",599),("Dark Chocolate Pack",249)],
 "Accessories": [("Travel Backpack",1299),("Sunglasses",699),("Leather Wallet",549),("Analog Wrist Watch",1799),("Laptop Sleeve",499)]}
class Command(BaseCommand):
    def handle(self, *a, **k):
        random.seed(7); n = 0
        for cat, items in DATA.items():
            for name, price in items:
                n += 1
                Product.objects.update_or_create(name=name, defaults=dict(category=cat, price=price,
                    old_price=round(price * 1.3, -1) if n % 2 else None, rating=round(random.uniform(3.8, 4.9), 1),
                    stock=random.randint(5, 60), image_url=f"https://picsum.photos/seed/shopalpha{n}/600/450",
                    description=f"{name} from our {cat} collection. Premium quality, great value and fast delivery. Easy 7-day returns."))
        self.stdout.write(f"Seeded {n} products")
