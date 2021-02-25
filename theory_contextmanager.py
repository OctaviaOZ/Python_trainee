class MyContentManadger:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'{self.name} entered')
        return  self.name

    def __exit__(self, *args):
        print(f'{self.name} exited')


# pcm1 = MyContentManadger('context manager 1')
# pcm2 = MyContentManadger('context manager 2')
#
# with pcm1 as name:
#     print(f'in with block for {name}')
#
# try:
#     with pcm2 as name:
#         raise Exception
#         print(f'in with block for {name}')
# except:
#     print('Error occured.')

from contextlib import contextmanager

@contextmanager
def some_generatore(*args):
    value = 0
    try:
        yield value
    finally:
        del value

@contextmanager
def managed_file(name, method):
    f = open(name, method)
    try:
        yield f
    except:
        f.close()

# with managed_file('hello.txt','w') as f:
#     f.write('hello, word')
#     f.write('bye now')

import json

class Student:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def from_json(data):
        return Student(**data)


class Team:

    def __init__(self, students: []):
        self.students = students

    @staticmethod
    def from_json(data):
        students = list(map(Student.from_json, data['students']))
        return Team(students)


# student1 = Student(first_name='Jake', last_name='Foo')
# student2 = Student(first_name='Jason', last_name='Bar')
# team = Team([student1, student2])
#
# # Serializing
# data = json.dumps(team, default=lambda o:o.__dict__, sort_keys=True, indent=4)
# print(data)
#
# # Deserializing
# decoded_team = Team.from_json(json.loads(data))
# print(decoded_team)
# print(decoded_team.students)

from jsonschema import validate

schema= {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
    },
    "required": ["age", "name"]
}

# valid_json = {"name": "Jason", "age": 10}
# invalid_json1 = {"name": "Jason", "age": "10"}
# invalid_json2 = {"name": "Jason"}
# validate(valid_json, schema)
# validate(invalid_json1, schema)
# validate(invalid_json2, schema)
import csv

mydict=[{"name": "Jason", "age": "10"},
        {"name": "Jason1", "age": "11"}]

fields = ["name", "age"]
file_name = "output.txt"

with open(file_name, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(mydict)
