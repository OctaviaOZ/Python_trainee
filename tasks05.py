def divide(numerator, denominator):
    # enter your code
    try:
        result = numerator / denominator
        return f"Result is {result}"

    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"

    except TypeError:
        return "Value Error! You did not enter a number!"


# import complex math module
import cmath

def solve_quadric_equation(a, b, c):

    try:

        a, b, c = float(a), float(b), float(c)
        # calculate the discriminant
        d = (b ** 2) - (4 * a * c)

        # find two solutions
        solution_1 = (-b - cmath.sqrt(d)) / (2 * a)
        solution_2 = (-b + cmath.sqrt(d)) / (2 * a)

        return f"The solution are x1={solution_1} and x2={solution_2}"

    except ZeroDivisionError:
        return "Zero Division Error"

    except ValueError:
        return "Could not convert string to float"

# s1 = solve_quadric_equation(1, 5, 6)            #output:   " The solution are x1=(-2-0j) and x2=(-3+0j)"
# s2 = solve_quadric_equation(0, 8, 1)            #output:   "Zero Division Error"
# s3 = solve_quadric_equation(1,"abc", 5)       #output:   "Could not convert string to float"
#
# print(s1, s2, s3)


class MyError(Exception):
    # enter your code
    pass


def check_positive(number):
    # enter your code
    try:
        number = float(number)
        if number < 0:
            raise MyError

        else:
            return f"You input positive number: {number}"

    except ValueError:
        return "Error type: ValueError!"

    except MyError:
        return f"You input negative number: {number}. Try again."


class MyError(Exception):
    # enter your code
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

    def __repr__(self):
        return self.message


class MyError(Exception):
    # enter your code
    def __init__(self, text):
        self.txt = text


class MyError(Exception):
    #Exception.    # enter your code
    pass

def check_positive(number):
    # enter your code
    try:
        number = float(number)
        if number < 0:
            raise MyError(f"You input negative number: {number}. Try again.")

        else:
            return f"You input positive number: {number}"

    except ValueError:
        return "Error type: ValueError!"

    except MyError as e:
        return e

#c1 = check_positive (24)      #output:    "You input positive number: 24"
#c1 = check_positive (-19)     #output:     "You input negative number: -19. Try again."
#c1 = check_positive ("38")    #output:    "You input positive number: 38"
#c1 = check_positive ("abc")  #output:     "Error type: ValueError!"
#print(c1)
#print(c1) #, c2, c3, c4

import re

def valid_email(email):
    #enter your code

    #[chr(i) for i in range(0x0021, 0x02FF)]
    #An email is a string (a subset of ASCII characters) separated into two parts by @ symbol,
    # a “user_info” and a domain_info, that is personal_info@domain_info:
    pattern_email = "^[a-z]+@([a-z]+\.){1,2}([a-z]{3})$"
    try:
        if not re.match(pattern_email, email):
            raise ValueError
        else:
            return "Email is valid"
    except ValueError:
        return "Email is not valid"


def valid_email1(email):
    #enter your code

    #An email is a string (a subset of ASCII characters) separated into two parts by @ symbol,
    # a “user_info” and a domain_info, that is personal_info@domain_info:
    pattern_email = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$'
    try:
        if not re.match(pattern_email, email):
            raise ValueError("Email is not valid")
        return "Email is valid"

    except ValueError as e:
        return e

# print(valid_email("trafik@ukr.tel.com"))          #output:   "Email is valid"
# print(valid_email("trafik@ukr_tel.com"))        #output:   "Email is not valid"
# print(valid_email("tra@fik@ukr.com"))           #output:   "Email is not valid"
# print(valid_email("ownsite@our.c0m"))         #output:   "Email is not valid"




def day_of_week(day):
    week_days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    try:

        if type(day) != int and not day.isdigit():
            raise TypeError

        name_of_day = week_days[day]

        return name_of_day

    except KeyError:
        return "There is no such day of the week! Please try again."

    except TypeError:
        return "You did not enter a number! Please try again."



class ToSmallNumberGroupError(Exception):
    """Raised when the input value is too small"""
    pass


def check_number_group(number):
    try:

        if type(number) == str and number.isdigit():
            number = int(number)

        if number <= 10:
            raise ToSmallNumberGroupError

        return f"Number of your group {number} is valid"

    except ToSmallNumberGroupError:
        return "We obtain error:Number of your group can't be less than 10"

    except TypeError:
        return "You entered incorrect data. Please try again."


def check_number_group(number):
    try:

        number = int(number)

        if number <= 10:
            raise ToSmallNumberGroupError

        return f"Number of your group {number} is valid"

    except ToSmallNumberGroupError:
        return "We obtain error:Number of your group can't be less than 10"

    except ValueError:
        return "You entered incorrect data. Please try again."

#print(check_number_group(75))


def check_odd_even(number):
    try:
        if number % 2:
            is_number = "odd"

        else:
            is_number = "even"

        return f"Entered number is {is_number}"

    except TypeError:
        return "You entered not a number."