# Create a class Inventory. The __init__ method should accept only the capacity of the inventory. The capacity should be a private attribute (__capacity). You can read more about private attributes here. Each inventory should also have an attribute called items, where all the items will be stored. The class should also have 3 methods:
# •	add_item(item) - adds the item in the inventory if there is space for it. Otherwise, returns
# "not enough room in the inventory"
# •	get_capacity() - returns the value of __capacity
# •	__repr__() - returns "Items: {items}.\nCapacity left: {left_capacity}". The items should be separated by ", "


class Inventory:
    items = []

    def __init__(self, __capacity):
        self.capacity = __capacity

    def add_item(self, item):
        if self.capacity > 0:
            self.items.append(item)
            self.capacity -= 1
        elif self.capacity == 0:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.get_capacity()}"


# Testing
inventory = Inventory(2)
print(inventory.get_capacity())
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory)
