class Item:
    # Constructor accepts three parameters: item name, quantity (default value 1), price (default value 10).
    def __init__(self, item_name, quantity=1, price=10):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    # Method which returns item quantity * item price.
    def get_total_price(self):
        return self.quantity * self.price

    # Method which returns text consisting of item name + item price + item quantity + get_total_price().
    def full_info(self):
        return "{} {} {} {} \n".format(self.item_name, self.price, self.quantity, self.get_total_price())

    # Method which returns data in the dictionary.
    def to_dict(self):
        item_dict = {'name': self.item_name,
                     'price': self.price,
                     'total_price': self.get_total_price()}
        return "{} \n".format(item_dict)


class Food(Item):
    # Constructor accepts three parameters: item name, quantity (default value 1), price (default value 10).
    def __init__(self, item_name, quantity=1, price=10):
        super().__init__(item_name, quantity, price)

    def full_info(self):
        return "{} {} {} {} {}".format("Food", self.item_name, self.price, self.quantity, self.get_total_price())


class Drink(Item):
    # Constructor accepts three parameters: item name, quantity (default value 1), price (default value 10).
    def __init__(self, item_name, quantity=1, price=10):
        super().__init__(item_name, quantity, price)

    def full_info(self):
        return "{} {} {} {} {}".format("Drink", self.item_name, self.price, self.quantity, self.get_total_price())
