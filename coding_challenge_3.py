# part 1
def student_price(current_price):
    return current_price - current_price * .10


def regular_buyer(price):
    student = student_price(price)
    final = student - student * .05
    return final


student = student_price(100)
print(student)
regular = regular_buyer(100)
print(regular)

# part 2
print((lambda x: x*(x+5)**2)(5))

# part 3
prices = [200, 30, 150, 3000, 10]


def reduce_price(price):
    return price - price * .10


x = map(reduce_price, prices)
print(list(x))

# part 4
class Computer:
    name = ''
    year = 0

    def get_computer_specs(self):
        self.name = input('What is the name: ')
        self.year = input('What is the year: ')

    def display_computer_specs(self):
        print(self.name)
        print(self.year)


class Desktop(Computer):
    size = ''

    def get_desktop_specs(self):
        self.size = input('What is the size: ')

    def display_desktop_specs(self):
        print(self.size)


class Laptop(Computer):
    weight = 0

    def get_laptop_specs(self):
        self.weight = input('What is the weight: ')

    def display_laptop_specs(self):
        print(self.weight)


laptop1 = Laptop()
laptop1.get_computer_specs()
laptop1.get_laptop_specs()
laptop1.display_computer_specs()
laptop1.display_laptop_specs()

desktop1 = Desktop()
desktop1.get_computer_specs()
desktop1.get_desktop_specs()
desktop1.display_computer_specs()
desktop1.display_desktop_specs()


# part 5
class Pounds:
    def __init__(self, weight):
        self.weight = weight

    def __mul__(self, other):
        adding = self.weight + other.weight
        return Pounds(adding)

    def __str__(self):
        return "({0})".format(self.weight)

my_weight = Pounds(100)
your_weight = Pounds(200)
print(my_weight * your_weight)