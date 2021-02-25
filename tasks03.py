import re


def outer(name):
    def inner():
        print(f"Hello, {name}!")

    return inner


# tom = outer("tom")
# tom()


def create(arg):
    return lambda arg1: arg == arg1


# tom = create("pass_for_Tom")

# print(tom("pass_for_Tom"))
# print(tom("pass_for_tom"))


def create_account(user_name, password, secret_words):
    """
        param: user_name: string, password: string, secret_words: list
        return: inner function check

        Password should contain at least 6 symbols including one uppercase letter,
                            one lowercase letter,  special character and one number.
        Otherwise function create_account raises ValueError.
    """

    pattern_password = re.compile(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*\[\]\"\';:_\-<>., =+/\\]).{6,}$')

    if not pattern_password.match(password):
        raise ValueError("Password should contain at least 6 symbols including one uppercase letter, "
                         "one lowercase letter, special character and one number")

    def check(password_check, secret_words_check):

        if password != password_check or len(secret_words) != len(secret_words_check) or len(secret_words) == 0:
            return False

        len_misspelled_1 = 0
        len_misspelled_2 = 0
        for i in range(len(secret_words)):

            if secret_words[i] not in secret_words_check:
                len_misspelled_1 += 1

            if secret_words_check[i] not in secret_words:
                len_misspelled_2 += 1

            if len_misspelled_1 > 1:
                return False

            if len_misspelled_2 > 1:
                return False

        return True

    return check


def create_account1(user_name, password, secret_words):
    """
        param: user_name: string, password: string, secret_words: list
        return: inner function check

        Password should contain at least 6 symbols including one uppercase letter,
                            one lowercase letter,  special character and one number.
        Otherwise function create_account raises ValueError.
    """

    pattern_password = \
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*\[\]\"\';:_\-<>\., =\+\/\\]).{6,}$'

    try:
        if not re.match(pattern_password, password):
            raise ValueError("Password should contain at least 6 symbols including one uppercase letter, " +
                             "one lowercase letter, special character and one number.")
    except ValueError as e:
        print(e)
        return False

    # ("Password should contain at least 6 symbols including one uppercase letter, "
    #                     "one lowercase letter, special character and one number")

    def check(password_check, secret_words_check):

        if password != password_check or len(secret_words) != len(secret_words_check):
            return False

        return sum(1 for i in range(len(secret_words)) if secret_words[i] not in secret_words_check) < 2 and \
               sum(1 for i in range(len(secret_words)) if secret_words_check[i] not in secret_words) < 2

    return check


#tom = create_account1("Tom", "Qwerty1_", ["1", "word"])
#check1 = tom("Qwerty1_",  ["1", "word"]) #return True
#print(check1)
#
# check2 = tom("Qwerty1_",  ["word"]) #return False due to different length of   ["1", "word"] and  ["word"]
#
# check3 = tom("Qwerty1_",  ["word", "12"]) #return True
#
# check4 = tom("Qwerty1!",  ["word", "1"]) #return False because "Qwerty1!" not equals to "Qwerty1_"
#
# print(check1, check2, check3, check4)
#
# user2 = create_account1("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
# print(user2("yu6r*Tt5",["abc3", "word1", "list"]))
#
#val1 = create_account1("123", "qQ1345", [1, 1])

#val1 = create_account1("123", "qQ1!45", [1, 2, 1])
#print(val1("qQ1!45", [1, 3, 4]))


def divisor(n):
    for i in range(1, n + 1):
        if not n % i:
            yield i

    while True:
        yield None


# three = divisor(3)
# print(next(three))
# print(next(three))
# print(next(three))
# print(next(three))


def logger(func):
    def wrapper(*args, **kwargs):
        a = ', '.join(map(str, args))
        if a and kwargs:
            a += ', '
        a += ', '.join(map(str, kwargs.values()))

        result = func(*args, **kwargs)

        print(f"Executing of function {func.__name__} with arguments {a}...")

        return result

    return wrapper


@logger
def concat(*args, **kwargs):
    s_ = ''
    for s in args:
        s_ += str(s)

    for s in kwargs.values():
        s_ += str(s)

    return s_


print(concat(2, 3))
print(concat('hello', 2))
print(concat (first = 'one', second = 'two'))

# print(concat(1))
# print(concat('first string', second = 2, third = 'second string'))

# Executing of function concat with arguments first string, 2, second string...
# first string2second string

from random import choice


def randomWord(words):
    w = words[:]
    while True and w:

        for i in range(len(w)):
            choiced = choice(w)
            yield choiced
            w.remove(choiced)

        w = words[:]

    yield None

# import collections
#
# double_list = ["word1", "Biggg word", "last word"]
# actual_list = []
# random_element = randomWord(double_list)
# for _ in range(len(double_list) * 2):
#     actual_list.append(next(random_element))
# print(collections.Counter(set(actual_list)) == collections.Counter(set(double_list * 2)))
