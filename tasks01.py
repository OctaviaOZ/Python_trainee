#For the given integer n, consider an increasing sequence consisting of all positive integers that are either powers
# of n, or sums of distinct powers of n.
#Your task is to find the kth (1-based) number in this sequence.

def kthTerm(n, k):

    # Constraints
    if n < 2 or n > 30 or k < 1 or k > 100:
        return 0

    seq_integers = []

    for p in range(k):

        number_power = n ** p
        seq_integers.append(number_power)

        len_list = len(seq_integers)
        if len_list == k:
            break

        last_item = min(k - len_list, len_list - 1)

        seq_integers += [item + number_power for item in seq_integers[:last_item]]

        if len(seq_integers) >= k:
            break

    return seq_integers[k - 1]


def kthTerm1(n, k):

    seq_integers = []
    seq_append = seq_integers.append

    for p in range(k):
        seq_append(n ** p)

        last_item = len(k) - 1
        for i in range(last_item):
            seq_integers[i]+seq_integers[last_item]

    return seq_integers[k - 1]


def filterBible(scripture, book, chapter):

    filteredVerses = [item for item in scripture if item[:2] == book and item[2:5] == chapter]

    return filteredVerses


def filterBible1(scripture, book, chapter):

    filteredVerses = [item for item in scripture if +item.startwith(book+chapter)]

    return filteredVerses

filterBible2 = lambda s, b, c: [i for i in s if s[:5] == b+c]

def isPalindrome(str):

    # in palindrom each litera have to be even and some case one in the middle
    str = str.replace(' ', '').upper()

    onlyonecase = 0
    for l in set(str):
        if not str.count(l) % 2:
            onlyonecase += 1

        if onlyonecase > 1:
            return False

    return True

def isPalindrome1(str):
    return lambda s: sum(s.count(c) % 2 for c in set(s)) < 2


def findPermutation(n, p, q):

    r = [0 for i in range(n)]

    for i in range(n):

        #q[i-1] = p[r[i-1]]
        idx = p.index(q[i])
        r[i] = idx+1

    return r



findPermutation1 = lambda n, p, q: [p.index(i)+1 for i in q]

# p = [2,3,1]
# q = [3,1,2]
# # #
# print(findPermutation1(3, p, q))

def order(a):

    # Constraints
    length_a = len(a)
    if length_a >= 100 or length_a < 1:
        return ''
    #elif length_a != len(set(a)):
    #    return ''

    if sorted(a) == a:
        return "ascending"
    elif sorted(a, reverse=True) == a:
        return "descending"
    else:
        return "not sorted"

def order1(a):
    return "ascending" if sorted(a) == a else "descending" if sorted(a) == a[::-1] else "not sorted"

#print(order1([1,2,3]))

def Cipher_Zeroes(N):

    # Constraints
    #if (int(N) < 1) or (int(N) > 1e1000):
    #   return 0

    visible_zeros_1 = '069'
    visible_zeros_2 = '8'

    number_points = 0
    for number in N:
        if number in visible_zeros_1:
            number_points += 1
        elif number in visible_zeros_2:
            number_points += 2

    if number_points:
        if number_points % 2:
            number_points -= 1
        else:
            number_points += 1

    return int(bin(number_points)[2:])


def Cipher_Zeroes(N):
    t = N.count
    t = t("8")*2 + t("0") + t("6") + t("9")
    t += [-1, 1][t % 2]
    return int(bin([0, t][t > 0])[2:])


def studying_hours(a):

    start = 0
    increase_days = 0
    increase_days_list = []

    for hours in a:
        if hours >= start:
            increase_days += 1
            start = hours
        else:
            if increase_days > 1:
                increase_days_list.append(increase_days)

            increase_days = 1
            start = 0

    if increase_days > 1:
        increase_days_list.append(increase_days)

    if increase_days_list:
        return max(increase_days_list)
    else:
        return 0

# це рішення підійде, якщо потрібно виводити не 0, а 1 якщо немає підвищення чи рівності
def studying_hours(a):

    start = 0
    increase_days = 0
    increase_days_list = []

    for hours in a:
        increase_days = [1, increase_days + 1][start <= hours]
        increase_days_list += [increase_days]
        start = hours

    return max(increase_days_list)
'''
Algorithm 
1. Scan the infix expression from left to right. 
2. If the scanned character is an operand, output it. 
3. Else, 
      1 If the precedence of the scanned operator is greater than the precedence of the operator 
        in the stack(or the stack is empty or the stack contains a ‘(‘ ), push it. 
      2 Else, Pop all the operators from the stack which are greater than or equal to in precedence than 
        hat of the scanned operator. After doing that Push the scanned operator to the stack. 
        (If you encounter parenthesis while popping then stop there and push the scanned operator in the stack.) 
4. If the scanned character is an ‘(‘, push it to the stack. 
5. If the scanned character is an ‘)’, pop the stack and and output it until a ‘(‘ is encountered, and discard both the parenthesis. 
6. Repeat steps 2-6 until infix expression is scanned. 
7. Print the output 
8. Pop and output from the stack until it is not empty. '''

def toPostFixExpression(e):

    #for return precedence to sort stack
    def getKey(op):
        return precedence[op]

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 3}

    outputs = []
    stack = []

    for item in e:

        if item[0] in '1234567890':
            outputs.append(item)

        elif item in '-+*/%':
            if stack:
                if stack[-1] == '(' or precedence[item] > precedence.get(stack[-1],0):
                    stack.append(item)
                else:
                    precedence_item = precedence[item]
                    while stack:
                        op = stack[-1]
                        if op == '(':
                            outputs.append(item)
                            break
                        elif precedence[op] >= precedence_item:
                            stack.pop()

                    stack.append(item)

            else:
                stack.append(item)

        elif item in '(':
            stack.append(item)

        elif item in ')':
            while stack:
                op = stack[-1]
                if op in '(':
                    stack.pop()
                    break
                else:
                    outputs.append(op)
                    stack.pop()

    if stack:
        stack.sort(key=getKey, reverse=True)
        outputs.extend(stack)

    return outputs


def toPostFixExpression1(e):

    #for return precedence to sort stack
    def getKey(op):
        return precedence[op]

    precedence = {'+': 2, '-': 2, '*': 3, '/': 3, '%': 3, '(': 1, ')': 1}

    outputs = []
    stack = []

    for item in e:

        if item in precedence and precedence[item] > 1:

            while stack and precedence[item] <= precedence[stack[-1]]:
                outputs += [stack.pop()]

            stack += [item]

        elif item == '(':

            stack += [item]

        elif item == ')':

            while stack[-1] != '(':

               outputs += [stack.pop()]

            stack.pop()

        else:
            outputs += [item]

    for item in stack[::-1]:
        outputs += [item]

    return outputs


#print(toPostFixExpression1(["2","+","3","*","4","(","5","*","6",")"]))