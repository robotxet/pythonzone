"""
Create an application which manages an inventory of products.
Create a product class which has a price, id and quantity on hand.
Then create an inventory class which keeps track of various products and
can sum up the inventory value
"""


class Product(object):
    """
    class for storing product info
    """
    def __init__(self, name=None, id=0, price=0, quantity=0):
        self.name = name
        self.id = id
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return "%s, %s, %s, %s" % (self.name,
                                   self.id, self.price, self.quantity)


class Inventory(object):
    def __init__(self):
        self.product_list = []

    def addProduct(self, product):
        self.product_list.append(product)

    def removeProduct(self, pId):
        for product in self.product_list:
            if product.id == pId:
                self.product_list.remove(product)

    def __str__(self):
        return ' '.join(str(p) for p in self.product_list)

if __name__ == '__main__':
    product1 = Product('Tea', 1, 10, 5)
    inventory = Inventory()
    inventory.addProduct(product1)
    print inventory
    inventory.removeProduct(1)
    print inventory
