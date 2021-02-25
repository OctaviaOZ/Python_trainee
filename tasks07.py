from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def cook(self):
        pass

class FettuccineAlfredo(Product):

    name = "Fettuccine Alfredo"

    def cook(self):
        print(f"Italian main course prepared: {FettuccineAlfredo.name}")


class Tiramisu(Product):

     name = "Tiramisu"

     def cook(self):
         print(f"Italian dessert prepared: {Tiramisu.name}")

class DuckALOrange(Product):

    name = "Duck À L'Orange"

    def cook(self):
        print(f"French main course prepared: {DuckALOrange.name}")

class CremeBrulee(Product):

    name = "Crème brûlée"

    def cook(self):
        print(f"French dessert prepared: {CremeBrulee.name}")

class Factory(ABC):

    @abstractmethod
    def get_dish(self, type_of_meal):
        pass


class ItalianDishesFactory(Factory):

    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return FettuccineAlfredo()
        else:
            return Tiramisu()

class FrenchDishesFactory(Factory):

    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return DuckALOrange()
        else:
            return CremeBrulee()


class FactoryProducer:

    def get_factory(self, type_of_factory):

        if type_of_factory == "italian":
            return ItalianDishesFactory()
        else:
            return FrenchDishesFactory()

#behavioral/strategy
class Goods:

    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    @property
    def discount_strategy(self):
        return self._discount_strategy

    @discount_strategy.setter
    def discount_strategy(self, discount_strategy):
        self._discount_strategy = discount_strategy

    def __str__(self):
        return f"Price: {self.price}, price after discount: {self.price_after_discount()}"

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        return self.price - discount

def on_sale_discount(order):
    return order.price * 0.5


def twenty_percent_discount(order):
    return order.price * 0.2

#adapter
class MotorCycle:
    """Class for MotorCycle"""

    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"


class Truck:

    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"


class Car:

    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"


class Adapter:
    """
        Adapts an object by replacing methods.
        Usage:
        motorCycle = MotorCycle()
        motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
        """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        #self.__dict__.update(adapted_methods)
        for key, val in adapted_methods.items():
            setattr(self, key, val)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__

#facade
class Washing:

    def __init__(self):
        print(self)

    def processing(self):
        print(self)

    def __str__(self):
        return "Washing..."


class Rinsing:

    def __init__(self):
        print(self)

    def processing(self):
        print(self)

    def __str__(self):
        return "Rinsing..."


class Spinning:

    def __init__(self):
        print(self)

    def processing(self):
        print(self)

    def __str__(self):
        return "Spinning..."


class WashingMachine:

    def __init__(self):
        self.wash = Washing()
        self.rinse = Rinsing()
        self.spin = Spinning()

    def startWashing(self):
        self.wash.processing()
        self.rinse.processing()
        self.spin.processing()

#washingMachine = WashingMachine()
#washingMachine.startWashing()

#composite
class LeafElement:

    def __init__(self, *args):
        ''''Takes the first positional argument and assigns to member variable "position".'''
        self.position = args[0]

    def showDetails(self):
        '''Prints the position of the child element.'''
        return f"\t\t{self.position}"


class CompositeElement:

    def __init__(self, *args):
        '''Takes the first positional argument and assigns to member
         variable "position". Initializes a list of children elements.'''
        self.position = args[0]
        self._children = []
        self.parent = None

    def add(self, child):
        '''Adds the supplied child element to the list of children
         elements "children".'''
        self._children.append(child)
        child.parent = self

    def remove(self, child):
        '''Removes the supplied child element from the list of
        children elements "children".'''
        self._children.remove(child)
        child.parent = None

    def showDetails(self):
        '''Prints the details of the component element first. Then,
        iterates over each of its children, prints their details by
        calling their showDetails() method.'''
        if self.parent:
            print("\t" + self.position)
        else:
            print(self.position)
        for child in self._children:
            sd = child.showDetails()
            if sd:
                print(child.showDetails())

# topLevelMenu = CompositeElement("GeneralManager")
# print(topLevelMenu)

#composite
class LeafElement:

    def __init__(self, *args):
        ''''Takes the first positional argument and assigns to member variable "position".'''
        self.position = args[0]

    def showDetails(self, level=0):
        '''Prints the position of the child element.'''
        print("\t", end="")
        print(self.position)


class CompositeElement:

    def __init__(self, *args):
        '''Takes the first positional argument and assigns to member
         variable "position". Initializes a list of children elements.'''
        self.position = args[0]
        self._children = []

    def add(self, child):
        '''Adds the supplied child element to the list of children
         elements "children".'''
        self._children.append(child)

    def remove(self, child):
        '''Removes the supplied child element from the list of
        children elements "children".'''
        self._children.remove(child)

    def showDetails(self, level=0):
        '''Prints the details of the component element first. Then,
        iterates over each of its children, prints their details by
        calling their showDetails() method.'''
        print(self.position)
        for child in self._children:
            print("\t"*level, end="")
            child.showDetails(level+1)

# topLevelMenu = CompositeElement("GeneralManager")
# subMenuItem1 = CompositeElement("Manager1")
# subMenuItem2 = CompositeElement("Manager2")
# subMenuItem11 = LeafElement("Developer11")
# subMenuItem12 = LeafElement("Developer12")
# subMenuItem21 = LeafElement("Developer21")
# subMenuItem22 = LeafElement("Developer22")
# subMenuItem1.add(subMenuItem11)
# subMenuItem1.add(subMenuItem12)
# subMenuItem2.add(subMenuItem22)
# subMenuItem2.add(subMenuItem22)
# topLevelMenu.add(subMenuItem1)
# topLevelMenu.add(subMenuItem2)
# topLevelMenu.showDetails()

