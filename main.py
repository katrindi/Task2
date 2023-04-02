from shop.shop_items import *
from shop.shop_customers import *

c1 = Customer("Jonas Jonaitis", [Food("Bread", 2, 1.3), Drink("CocaCola", 3, 1.7)])
c2 = Customer("Petras Petraitis", [Food("Butter", 1, 1.3), Drink("Sprite", 2, 1.7)])

print(c1.get_items())
print(c2.get_items())
c1.add_item(Drink("Fanta", 10, 1.7))
print(c1.get_items())
