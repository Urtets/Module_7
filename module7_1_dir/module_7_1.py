class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            file = open(self.__file_name, 'r')
            string_of_products = file.read()
            file.close()
            return string_of_products
        except FileNotFoundError:
            return ''


    def add(self, *products):
        string_of_products = self.get_products()
        exception = []
        for i in products:
            if i.name not in string_of_products:
                exception.append(i)
            else:
                print(f'Продукт {i.name} уже есть в магазине')

        for i in exception:
            string_of_products = string_of_products + i.__str__() + '\n'
        file = open(self.__file_name, 'w')
        file.write(string_of_products)
        file.close()

if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())