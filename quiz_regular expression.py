import re

#3 Which of the following regular expression can be used to identify date(s) present in the text object:

x = "The next meetup on data science will be held on 2017-09-21, previously it happened on 31/03, 2016"
re.findall(r'\d{4}{-\\}\d{2}-\d{2}', x)


#5 Match any 2, 3, or 4 digits.

x = '5555 333 11 66666'
re.findall(r'\d{2,4}', x)

#6 How would you find a 4-letter word that ends a string and is preceded by at least one zero?
#Write regular expression.
x = 'pppp 0rdgd 0jjjj'
re.findall(r'0\w{4}$', x)

#10
#Return a copy of the string with its first character capitalized and the rest lowercased.
print("hhhJJJJ".capitalize())
#Return the number of non-overlapping occurrences of substring sub in the range [start, end].
print("hhhJJJJ".count('h'))
#Return a list of the words in the string, using sep as the delimiter string.
print("hhh JJJ J".split(' '))
# Return a copy of the string with the leading and trailing characters removed.
print(" hhh JJJ J ".strip())

#11 If brackets are used to define a group, what would match the regular expression

re_ = "r'(,\s[0-9]{1,4}){4},\s[0-9]{1,3}\.[0-9]"

#, 135, 1155, 915, 513, 18.8

#12 Please select correct explanation for the regular expression pattern below.

#[^AEIOU] Match anything other than a uppercase vowel.