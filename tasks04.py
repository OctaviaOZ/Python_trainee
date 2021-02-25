class Employee:

    def __init__(self, firstname, lastname, salary):

        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def from_string(str):
        firstname, lastname, salary =  str.split("-")
        return Employee(firstname, lastname, salary)

class Employee:

    def __init__(self, _firstname, _lastname, _salary):

        self.firstname = _firstname
        self.lastname = _lastname
        self.salary = _salary

    @staticmethod
    def from_string(str):
        parsed_str = str.split("-")
        return Employee(*parsed_str)

# emp1 = Employee("Mary", "Sue", 60000)
# emp2 = Employee.from_string("John-Smith-55000")
# #
# print(emp1.firstname) # "Mary"
# print(emp1.salary) # 60000
# print(emp2.firstname) # "John"

class Pizza:
    order_number = 0

    def __init__(self, ingredients):
        Pizza.order_number += 1
        self.order_number = Pizza.order_number
        self._ingredients = ingredients

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def set_ingredients(self, x):
        self._ingredients = x

    @staticmethod
    def hawaiian():
        return Pizza(["ham", "pineapple"])

    @staticmethod
    def meat_festival():
        return Pizza(["beef", "meatball", "bacon"])

    @staticmethod
    def garden_feast():
        return Pizza(["spinach", "olives", "mushroom"])

# p1 = Pizza(["bacon", "parmesan", "ham"])
# p2 = Pizza.garden_feast()                  # order 2
# print(p1.ingredients) #➞ ["bacon", "parmesan", "ham"]
# print(p2.ingredients) #➞ ["spinach", "olives", "mushroom"]
# print(p1.order_number) #➞ 1
# print(p2.order_number) #➞ 2

class Employee:

    def __init__(self, fullname, **kwargs):

        self.name, self.lastname = fullname.split(" ")
        self.__dict__.update(kwargs)

class Employee:

    def __init__(self, _fullname, **kwargs):

        self.name, self.lastname = _fullname.split(" ")
        for key, val in kwargs.items():
            setattr(self, key, val)


class Testpaper:

    def __init__(self, subject = "", markscheme = "", pass_mark = ""):

        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:

    def __init__(self):

        self.tests_taken = "No tests taken"

    def take_test(self, csl, markscheme):
        q_questions = len(markscheme)

        pass_mark = round(sum(1 for i in range(q_questions) if markscheme[i] == csl.markscheme[i])\
                            / q_questions * 100)

        if pass_mark >= int(csl.pass_mark[:2]):

            test_taken = {csl.subject: "Passed! (" + str(pass_mark) + "%)"}

        else:

            test_taken = {csl.subject: "Failed! (" + str(pass_mark) + "%)"}

        if isinstance(self.tests_taken, dict):

            self.tests_taken.update(test_taken)

        else:

            self.tests_taken = test_taken


# paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
# paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
# paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
#
# student1 = Student()
# student2 = Student()
# student1.tests_taken ➞ "No tests taken"
# student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
# student1.tests_taken ➞ {"Maths" : "Passed! (80%)"}
#
# student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
# student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
# student2.tests_taken ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}


class Gallows:

    def __init__(self):

        # a list of words already said
        self.words = []
        self.game_over = False

    def play(self, word):

        if (not self.words or word[0] == self.words[-1][-1]) and \
                word not in self.words and not self.game_over:

            self.words.append(word)
            return self.words

        else:

            self.game_over = True
            return "game over"

    def restart(self):

        self.__init__()
        return "game restarted"


my_gallows = Gallows()
print(my_gallows.play('apple')) #➞ ['apple']
print(my_gallows.play('ear'))#➞ ['apple', 'ear']
print(my_gallows.play('rhino')) #➞ ['apple', 'ear', 'rhino']
# Corn does not start with an "o".
print(my_gallows.play('corn'))
print(my_gallows.words) #➞ ['apple', 'ear', 'rhino']
#
# Words should be accessible.
print(my_gallows.restart() )#➞ "game restarted"
# # Words list should be set back to empty.
# print(my_gallows.play('hostess')) #➞ ['hostess']
# print(my_gallows.play('stash')) #➞ ['hostess', 'stash']
# print(my_gallows.play('hostess')) #➞ "game over"
# # Words cannot have already been said.
# print(my_gallows.play('apple')) #➞ ['apple']
# print(my_gallows.play('rhino')) #➞ ['apple', 'ear', 'rhino']
# print(my_gallows.play('corn')) #➞ "game over"
# print(my_gallows.words) #➞  ['apple',  'ear', 'rhino']
# print(my_gallows.restart()) #➞ "game restarted"
# print(my_gallows.words) #➞ []