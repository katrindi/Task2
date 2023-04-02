from shop.shop_items import *


class Customer:
    # Class variable to track the number of customers
    identifier = 0

    def __init__(self, customer_name, item_list):
        # .__ makes the customer name private
        self.__customer_name = customer_name
        Customer.identifier += 1
        self.customer_identifier = Customer.identifier
        self.item_list = item_list

    # Method which returns the customer identifier.
    def get_identifier(self):
        return "\n{}".format(self.customer_identifier)

    # Method which returns text consisting of customer identifier + customer name.
    def full_info(self):
        return "\n{} {}".format(self.customer_identifier, self.__customer_name)

    #  ---- Task 4 ----

    # Method which accepts a food or drink object and saves it to the customer.
    def add_item(self, item):
        # First, it checks if the parameter is one of the types of item (should be Food\Drink)
        if isinstance(item, Food) or isinstance(item, Drink):
            # If it is, Food\Drink,
            self.item_list.append(item)
        else:
            TypeError("Invalid item type")

    # Method which accepts an item index and removes that item from the customer's shopping cart.
    # def remove_item():

    # Method which returns a list of all items where each item is represented by its "full_info" method results.
    def get_items(self):
        # Create new list where the items will be defined
        item_list_for_print = []
        # For each item in 'item_list' list
        for item in self.item_list:
            # Each item will be represented by its "full_info" method
            item_list_for_print.append((item.full_info()))
        return item_list_for_print
