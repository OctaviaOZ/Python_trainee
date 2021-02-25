import json
from json import JSONEncoder
from jsonschema import validate
import logging
import os
import csv


def find(file, key):

    def get_values(x):
        if x:
            if type(x) == list:
                values_extend(x)
            else:
                values_append(x)

    values = []
    values_extend = values.extend
    values_append = values.append

    with open(file, 'r') as f:
        json_data = json.load(f)

    if type(json_data) == dict:
        get_values(json_data.get(key))
    else:
        for dict_ in json_data:
            get_values(dict_.get(key))

    return list(set(values))

def find_all(data, key):
    result =[]

    return set(result)


def find(file, key):
    with open(file, 'r') as f:
        json_data = json.load(f)
    return find_all(json_data, key)



logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def parse_user(output_file, *input_files):

    def get_names(d):
        name = d.get('name')
        if name and name not in names:
            output_list_append(d)
            names.add(name)

    names = set()
    output_list = []
    output_list_append = output_list.append

    for file in input_files:

        try:
            with open(file, 'r') as f:
                json_data = json.load(f)

            if type(json_data) == dict:
                get_names(json_data)
            else:
                for items in json_data:
                    get_names(items)

        except FileNotFoundError as e:
            logging.error(f"File {e.filename} doesn't exists")

    with open(output_file, "w") as f:
        json.dump(output_list, f, indent=4)


class DepartmentName(Exception):

    def __init__(self, id):
        self.id = id
        self.message = f"Department with id {self.id} doesn't exists"
        print(self.message)

    def __str__(self):
        return self.message


class InvalidInstanceError(Exception):

    def __init__(self, name):
        self.name = name
        self.message = f"Error in {self.name} schema"
        print(self.message)

    def __str__(self):
        return self.message


def validate_json(data, schema):
    try:
        validate(data, schema)
        return False
    except:
        return True


def user_with_department(csv_file, user_json, department_json):
    def get_data(d):

        name_user = d.get('name')
        id_department = d.get('department_id')
        department = [items.get('name') for items in departments \
                      if items.get('id') == id_department]

        if not department:
            raise DepartmentName(id_department)
        else:
            return name_user, department[0]

    user_schema = {
        "type": "array",
        "items": {
            "properties": {
                "id": {"type": "number"},
                "name": {"type": "string"},
                "department_id": {"type": "number"},
            },
            "required": ["name", "department_id"]}
    }

    department_schema = {
        "type": "array",
        "items": {
            "properties": {
                "id": {"type": "number"},
                "name": {"type": "string"},
            },
            "required": ["id", "name"]}
    }

    try:

        with open(user_json, 'r') as f:
            users = json.load(f)

        with open(department_json, 'r') as f:
            departments = json.load(f)

        if validate_json(users, user_schema):
            raise InvalidInstanceError("user")
        elif validate_json(departments, department_schema):
            raise InvalidInstanceError("department")

        fields = ["name", "department"]
        dict_data = []
        dict_data_append = dict_data.append

        for items in users:
            name, department = get_data(items)
            dict_data_append({"name": name, "department": department})

        with open(csv_file, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(dict_data)

    except DepartmentName as e:
        return e

    except InvalidInstanceError as e:
        return e


class StudentEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Student:

    def __init__(self, full_name: str, avg_rank: float, courses: []):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __str__(self):
        return f'{self.full_name} ({self.avg_rank}): {self.courses}'

    def __repr__(self):
        return f'"{self.full_name} ({self.avg_rank}): {self.courses}"'

    @classmethod
    def from_json(cls, data):
        with open(data, 'r') as f:
            student = json.load(f)
        return Student(**student)


def get_filename(path):
    filename = os.path.basename(path)
    file_name = os.path.splitext(filename)[0]

    return file_name


class Group:

    def __init__(self, title: str, students: []):
        self.title = title
        self.students = students

    def __str__(self):
        return f'{self.title}: {self.students}'

    @staticmethod
    def serialize_to_json(list_of_groups, filename):
        data = json.dumps(list_of_groups, cls=StudentEncoder)
        with open(filename, "w") as f:
            f.write(data)

    @classmethod
    def create_group_from_file(cls, students_file):

        with open(students_file, 'r') as f:
            data = json.load(f)

        if type(data) == dict:
            students = [Student(**data)]
        else:
            students = [Student(**student) for student in data]

        return Group(get_filename(students_file), students)


from pickle import dump as pickle_dump
from json import dump as json_dump
from enum import Enum

#FileType = Enum("FileType", "JSON BYTE")

class FileType(Enum):
    JSON = 1
    BYTE = 2

class SerializeManager:

    def __init__(self, filename, type_):
        self.filename = filename
        self.type = type_
        self.file = None

    def __enter__(self):
        mode = "wb" if self.type == FileType.BYTE else "w"
        self.file = open(self.filename, mode)
        return self

    def __exit__(self, *exc):
        self.file.close()
        return False #?

    def serialize(self, object_):
        if self.type == FileType.BYTE:
            pickle_dump(object_, self.file)
        elif self.type == FileType.JSON:
            json_dump(object_, self.file, skipkeys=True)

def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)

#user_dict = {"name": "Hallo", "id" : 2}
#serialize(user_dict, "2", FileType.JSON)