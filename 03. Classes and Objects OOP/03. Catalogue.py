# Create a class Catalogue. The __init__ method should accept the name of the catalogue.
# Each catalogue should also have an attribute called products and it should be a list.
# The class should also have three more methods:
#   •	add_product(product) - add the product to the product list
#   •	get_by_letter(first_letter) - returns a list containing only the products that start with the given letter
#   •	__repr__ - returns the catalogue info in the following format:
#       "Items in the {name} catalogue:
#       {item1}
#       {item2}
#       …"
# The items should be sorted alphabetically (default sorting)


class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        new_products = []
        for each_item in self.products:
            if each_item.startswith(first_letter) == True:
                new_products.append(each_item)
        return new_products

    def __repr__(self):
        self.products.sort()
        result_str = "\n".join(self.products)
        return f"Items in the {self.name} catalogue: \n{result_str}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
