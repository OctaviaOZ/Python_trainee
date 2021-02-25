double_string = lambda x: sum(1 for s in x if x.count(s*2))

#data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
#print(double_string(data))

def morse_number(num):

    morse_code = []
    morse_code_append = morse_code.append

    for each in num:

        int_each = int(each)
        if int_each < 6:
            morse_code_append("." * int_each + "-" * (5 - int_each))
        else:
            morse_code_append("-" * (int_each - 5) + "." * (10 - int_each))

    return " ".join(morse_code)

#print(morse_number("295"))
#print(morse_number("005"))
#print(morse_number("513"))
#print(morse_number("784"))


import re
import math


def figure_perimetr(s):
    y = re.findall(r'([0-9]):', s)
    x = re.findall(r':([0-9])', s)
    
    perimeter = sum(math.sqrt((int(x[i]) - int(x[j])) ** 2 + \
                              (int(y[i]) - int(y[j])) ** 2) \
                    for i, j in [[0, 1], [1, 3], [3, 2], [2, 0]])

    return perimeter

#test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
#print(figure_perimetr(test2))

def max_population(data):

    population_max = max(int(re.findall(r',([0-9]+)',each)[0]) for each in data[1:])
    name_max =  ["".join(each).split(',')[1] for each in data[1:] if str(population_max) in each]

    return (name_max[0], population_max)


# data = ["id,name,poppulation,is_capital",
#             "3024,eu_kyiv,24834,y",
#             "3025,eu_volynia,20231,n",
#             "3026,eu_galych,23745,n",
#             "4892,me_medina,18038,n",
#             "4401,af_cairo,18946,y",
#             "4700,me_tabriz,13421,n",
#             "4899,me_bagdad,22723,y",
#             "6600,af_zulu,09720,n"]

#print(max_population(data))

def pretty_message(s):

    mather = re.compile(r"(.+?)\1+")
    replace_list = [(match.group(0), match.group(1)) \
                    for match in mather.finditer(s)]
    for in_, out_ in replace_list:
        s = s.replace(in_, out_)

    return s
	
def pretty_message(data):
    return re.sub(r'(.+?)\1+\b', r'\1', data)
	
#s = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"	
	