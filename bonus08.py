from enum import Enum
import json
from json import JSONEncoder
import re
from uuid import UUID, uuid4


class Role(Enum):
    Trainee = 0
    Mentor = 1


class Score(Enum):
    A = (90, 100)
    B = (80, 89)
    C = (70, 79)
    D = (60, 69)
    F = (0, 59)


class NonUniqueException(Exception):
    def __init__(self, name):
        self.name = name
        self.message = f"User with name {self.name} already exists"

    def __str__(self):
        return self.message


class UserEncoder(JSONEncoder):
    def default(self, o):
        result = {}
        for key, item in o.__dict__.items():
            if key in ("username", "password"):
                result[key] = item
            elif key == "id":
                if isinstance(item, UUID):
                    result[key] = item.hex
                else:
                    result[key] = item
            elif key == "role":
                result[key] = item.value
        return result


class SubjectEncoder(JSONEncoder):
    def default(self, o):
        result = {}
        for key, item in o.__dict__.items():
            if key == "id":
                if isinstance(item, UUID):
                    result[key] = item.hex
                else:
                    result[key] = item
        return result


class GradeEncoder(JSONEncoder):
    def default(self, o):
        result = {}
        for key, item in o.__dict__.items():
            if key in ("subject_id", "user_id"):
                if isinstance(item, UUID):
                    result[key] = item.hex
                else:
                    result[key] = item
            # "score"
            else:
                result[key] = item
        return result


class PasswordValidationException(Exception):
     pass

class ForbiddenException(Exception):
     pass


def users_to_json(users, json_file):
    data = json.dumps(users, cls=UserEncoder)
    with open(json_file, "w") as f:
        f.write(data)


def subjects_to_json(subjects, json_file):
    data = json.dumps(subjects, cls=SubjectEncoder)
    with open(json_file, "w") as f:
        f.write(data)


def grades_to_json(users, subjects, json_file):
    list_grades = []
    titles = [subject.title for subject in subjects]
    for user in users:
        for grade in user.scores:
            list_grades.extend([item for key, item in grade.items() if key in titles])

    data = json.dumps(list_grades, cls=GradeEncoder)
    with open(json_file, "w") as f:
        f.write(data)


def check_if_user_present(username, password, users):
    users_attr = [(user_.username, user_.password) for user_ in users]
    return (username, password) in users_attr


def add_user(user, users):
    user_names = [user_.username for user_ in users]
    try:
        if user.username not in user_names:
            users.append(user)
        else:
            raise NonUniqueException(user.username)
    except NonUniqueException as e:
        print(e)


def add_subject(subject, subjects): #check title unique
    if subject not in subjects:
        subjects.append(subject)


def get_grades_for_user(username, user, users):
    try:
        if user.username != username and user.role != Role.Mentor:
            raise ForbiddenException("Forbidden")
        scores_ = [user_.scores for user_ in users if username == user_.username]
    except ForbiddenException as e:
        return e
    return scores_[0]


def get_subjects_from_json(subjects_json):
    with open(subjects_json, 'r') as f:
        data = json.load(f)

    if type(data) == dict:
        subjects = [Subject(**data)]
    else:
        subjects = [Subject(**subject) for subject in data]

    return subjects


def get_users_with_grades(users_json, subjects_json, grades_json):
    def get_list(json_data, cls):
        with open(json_data, 'r') as f:
            data = json.load(f)
            if type(data) == dict:
                list_data = [cls(**data)]
            else:
                list_data = [cls(**item) for item in data]
        return list_data

    users = get_list(users_json, User)
    subjects = get_subjects_from_json(subjects_json)
    grades = get_list(grades_json, Scores)

    for user in users:
        grades_of_user = {grade.subject_id: grade for grade in grades \
                          if grade.user_id == user.id}
        subjectes_of_user = {subject.id: subject for subject in subjects \
                             if subject.id in grades_of_user}
        for id_, grade in grades_of_user.items():
            user.add_score_for_subject(subjectes_of_user.get(id_), grade)

    return users


def get_uuid():
    return uuid4()


class Subject:
    def __init__(self, title, id=None):
        self.title = title
        self.id = id if id else get_uuid()

    def __repr__(self):
        return f"'{self.title}'"


class User:
    def __init__(self, username, password, role, id):
        self.username = username
        self.password = password
        self.role = Role(role) if isinstance(role, int) else role
        self.id = id
        self.scores = []

    def __str__(self):
        return f"{self.username} with role {self.role}: {self.scores}"

    def __repr__(self):
        return f"{self.username}"

    def add_score_for_subject(self, subject, score):
        if isinstance(score, Score):
            score = Scores(score.name, self.id, subject.id)
        self.scores.append({subject.title: score})

    @classmethod
    def create_user(cls, username, password, role):
        pattern_password = \
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*\[\]\"\';:_\-<>\., =\+\/\\]).{6,}$'
        if not re.match(pattern_password, password):
            raise PasswordValidationException # ("Invalid password")
        id_ = get_uuid()
        return cls(username, password, role, id_)


class Scores:
    def __init__(self, score, user_id, subject_id):
        self.score = score
        self.user_id = user_id
        self.subject_id = subject_id

    def __repr__(self):
        return f"'{self.score}'"