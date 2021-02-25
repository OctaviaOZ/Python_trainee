import math
import unittest
from unittest.mock import mock_open, patch

class Product:

    def __init__(self, name, price, count=0):
        self.name = name
        self.price = price
        self.count = count
        self.discount = 0

    def __str__(self):
        return f"name: '{self.name}' price: {self.price} count: {self.count} discount: {self.discount}"


class Cart:

    def __init__(self):
        self.products = []

    def add(self, product):
        if product in self.products:
            idx = self.products.index(product)
            self.products[idx].count += 1
            self.products[idx].discount = self.discount(self.products[idx].count)
        else:
            if not product.count:
                product.count = 1
            else:
                product.discount = self.discount(product.count)
            self.products.append(product)

    def discount(self, count):
        if count < 5:
            return 0
        elif count < 7:
            return 5
        elif count < 10:
            return 10
        elif count < 20:
            return 20
        elif count == 20:
            return 30
        else:
            return 50

    def get_product(self, product):
        if product in self.products:
            idx = self.products.index(product)
            return f"{self.products[idx]}"
        else:
            return f"Din't find!"

class CartTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # creating products with different quantities
        cls.product0 = Product("product0", 1)
        cls.product1 = Product("product1", 1, 5)
        cls.product2 = Product("product2", 1, 7)
        cls.product3 = Product("product3", 1, 10)
        cls.product4 = Product("product4", 1, 20)
        cls.product5 = Product("product5", 1, 21)
        cls.product6 = Product("product5", 1, 50)
        # adding to a cart all product exclude product6
        cls.card1 = Cart()
        cls.card1.add(cls.product1)
        cls.card1.add(cls.product2)
        cls.card1.add(cls.product3)
        cls.card1.add(cls.product4)
        cls.card1.add(cls.product5)
        # adding one more - in this case +1 count 0+1
        cls.card1.add(cls.product0)
        cls.card1.add(cls.product0)

    @classmethod
    def tearDownClass(cls):
        cls.product0 = None
        cls.product1 = None
        cls.product2 = None
        cls.product3 = None
        cls.product4 = None
        cls.product5 = None
        cls.product6 = None
        cls.card1 = None

    def test_get_product(self):
        list_cases = [(self.card1.get_product(self.product0), "name: 'product0' price: 1 count: 2 discount: 0"),
                  (self.card1.get_product(self.product1), "name: 'product1' price: 1 count: 5 discount: 5"),
                  (self.card1.get_product(self.product2), "name: 'product2' price: 1 count: 7 discount: 10"),
                  (self.card1.get_product(self.product3), "name: 'product3' price: 1 count: 10 discount: 20"),
                  (self.card1.get_product(self.product4), "name: 'product4' price: 1 count: 20 discount: 30"),
                  (self.card1.get_product(self.product5), "name: 'product5' price: 1 count: 21 discount: 50"),
                  (self.card1.get_product(self.product6), "Din't find!")]


        for p1, p2 in list_cases:
            with self.subTest():
                self.assertEqual(p1, p2)

#===============================================================================================================
def divide(num_1, num_2):
    return float(num_1) / num_2


class DivideTest(unittest.TestCase):

    def test_divine(self):
        list_cases = [(divide(5, 2), 2.5),
                      (divide(20, 3), 6.67),
                      (divide(3, 3), 1)]

        for p1, p2 in list_cases:
            with self.subTest():
                self.assertAlmostEqual(p1, p2, 2)

    def test_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 1, 0)

    def test_type(self):
        self.assertRaises(TypeError, divide, "1", "2")

    def test_value(self):
        self.assertRaises(ValueError, divide, "gg", 2)

#===============================================================================================================
# take math - without complex solutions
def quadratic_equation(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        # calculate the discriminant
        d = (b ** 2) - (4 * a * c)

        if d < 0:
            return None
        elif d == 0:
            # find one solutions
            solution_1 = (-b - math.sqrt(d)) / (2 * a)
            return solution_1
        else:
            # find two solutions
            solution_2 = (-b - math.sqrt(d)) / (2 * a)
            solution_1 = (-b + math.sqrt(d)) / (2 * a)
            return (solution_1, solution_2)
    except ZeroDivisionError as e:
        return e


class QuadraticEquationTest(unittest.TestCase):
    # discriminant > 0
    positive_case1 = quadratic_equation(1, 5, 6)
    # discriminant = 0
    positive_case2 = quadratic_equation(1, -4, 4)
    # discriminant < 0
    nagative_case = quadratic_equation(2, -4, 3)

    def test_positive_1(self):
        self.assertEqual(self.positive_case1, (-2.0, -3.0))

    def test_positive_2(self):
        self.assertEqual(self.positive_case2, 2.0)

    def test_no_solutions(self):
        self.assertEqual(self.nagative_case, None)

    # given not number
    def test_value(self):
        self.assertRaises(ValueError, quadratic_equation, 1, "abc", 5)


#===============================================================================================================
class TriangleNotValidArgumentException(Exception):
    pass

class TriangleNotExistException(Exception):
    pass

class Triangle:

    def __init__(self, args):
        Triangle.validate_create(args)
        self.a, self.b, self.c = args

    @staticmethod
    def _get_val_to_sqrt(a, b, c):
        p = (a + b + c) * 0.5
        val = p * (p - a) * (p - b) * (p - c)
        return val

    # Heron’s formula
    def get_area(self):
        val = self._get_val_to_sqrt(self.a, self.b, self.c)
        area = math.sqrt(self.val)
        return area

    @staticmethod
    def validate_create(args):
        if not isinstance(args, tuple) or len(args) != 3 or\
        False in (isinstance(each, int) or isinstance(each, float) for each in args):
            raise TriangleNotValidArgumentException("Not valid arguments")

        a, b, c = args

        if a < 0 or b < 0 or c < 0 or a + b < c or b + c < a or a + c < b:
            msg = "Can`t create triangle with this arguments"
            raise TriangleNotExistException(msg)

        val = Triangle._get_val_to_sqrt(a, b, c)
        if not val or val < 0:
            msg = "Can`t create triangle with this arguments"
            raise TriangleNotExistException(msg)


#t = Triangle(('a', 2, 3))

class TriangleTest(unittest.TestCase):

    valid_test_data = [
        ((3, 4, 5), 6.0),
        ((10, 10, 10), 43.30),
        ((6, 7, 8), 20.33),
        ((7, 7, 7), 21.21),
        ((50, 50, 75), 1240.19),
        ((37, 43, 22), 406.99),
        ((26, 25, 3), 36.0),
        ((30, 29, 5), 72.0),
        ((87, 55, 34), 396.0),
        ((120, 109, 13), 396.0),
        ((123, 122, 5), 300.0)
    ]
    not_valid_triangle = [
        (1, 2, 3),
        (1, 1, 2),
        (7, 7, 15),
        (100, 7, 90),
        (17, 18, 35),
        (127, 17, 33),
        (145, 166, 700),
        (1000, 2000, 1),
        (717, 17, 7),
        (0, 7, 7),
        (-7, 7, 7)
    ]
    not_valid_arguments = [
        ('3', 4, 5),
        ('a', 2, 3),
        (7, "str", 7),
        ('1', '1', '1'),
        'string',
        (7, 2),
        (7, 7, 7, 7),
        'str',
        10,
        ('a', 'str', 7)
    ]

    def test_valid_data(self):
        for p1, p2 in self.valid_test_data:
            with self.subTest():
                p = round(Triangle(p1).get_area(), 2)
                assert abs(p - p2) < 0.01

    def test_not_valid_data(self):
        for p in self.not_valid_triangle:
            with self.subTest():
                try:
                    Triangle(p)
                    return False
                except TriangleNotExistException:
                    return True

    def test_not_valid_arguments(self):
        for p in self.not_valid_arguments:
            with self.subTest():
                try:
                    Triangle(p)
                    return False
                except TriangleNotValidArgumentException:
                    return True




# not_valid_triangle = [
#         (-7, 7, 7)
# ]
# for data in not_valid_triangle:
#     try:
#         Triangle(data)
#         print(data)
#     except TriangleNotExistException as e:
#         print(e)

#===============================================================================================================
class Worker:
    def __init__(self, name, salary=0):
        if salary < 0:
            raise ValueError
        self.name = name
        self.salary = salary

    def get_tax_value(self, salary=0):
        if salary:
            self.salary = salary
        rates = [0, .1, .15, .21, .30, .40, .47]  # %
        brackets = [0, 1000, 3000, 5000, 10000, 20000, 50000]
        income = self.salary

        bt = zip(brackets, brackets[1:] + [income])
        income_in_b = (t - b if income > t else income - b for b, t in bt \
        if income - b > 0)
        tax = sum(p * s for p, s in zip(rates, income_in_b))
        if not tax:
            return 0.0
        else:
            return round(tax, 2)


class WorkerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # creating products with different quantities
        cls.worker = Worker("Worker")

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.worker

    def test_worker_success(self):
        list_cases = [(self.worker.get_tax_value(100), 0.0),
                      (self.worker.get_tax_value(1001), 0.1),
                      (self.worker.get_tax_value(5000), 500.0),
                      (self.worker.get_tax_value(10000), 1550.0),
                      (self.worker.get_tax_value(20000), 4550.0),
                      (self.worker.get_tax_value(50000), 16550.0),
                      (self.worker.get_tax_value(100000), 40050.0)]

        for p1, p2 in list_cases:
            with self.subTest():
                self.assertEqual(p1, p2)

    @unittest.expectedFailure
    def test_worker_failed(self):
        Worker("Worker 5", -100)


#===============================================================================================================
import unittest
from unittest.mock import mock_open, patch
def file_parser(path_to_file, find_string, replace_string=None):
    mode = "w" if replace_string else "r"
    with open(path_to_file, mode) as f:
        lines = f.readlines()
        count_ = sum(line.count(find_string) for line in lines)
        if not replace_string:
            return f"Found {count_} strings"
        elif count_:
            lines = [line.replace(find_string, replace_string) for line in lines]
            # Open file in write mode
            for line in lines:
                f.write(line)

        return f"Replaced {count_} strings"


class ParserTest(unittest.TestCase):
    data = "a,b,a\nx,y,z"

    @patch('builtins.open')
    def test_file_parser1(self, moke_file):
        moke_file.side_effect = [
            mock_open(read_data=self.data).return_value
        ]
        self.assertEqual(file_parser(moke_file, 'a'), "Found 2 strings")

    @patch('builtins.open')
    def test_file_parser2(self, moke_file):
        moke_file.side_effect = [
            mock_open(read_data=self.data).return_value
        ]
        self.assertEqual(file_parser(moke_file, 'a', 'b'), "Replaced 2 strings")

    @patch('builtins.open')
    def test_file_parser3(self, moke_file):
        mock_file = mock_open(read_data=self.data)
        with patch('builtins.open', mock_file):
            result = file_parser(mock_file, 'a', 'b')
            mock_file.assert_called_with(mock_file, "w")

unittest.main()

