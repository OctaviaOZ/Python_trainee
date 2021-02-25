import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import copy
import jsonschema


USERS_LIST = [
    {
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]

USERS_KEYS = ["id", "username", "firstName", "lastName", "email", "password"]

# I did't use the class in the code
# Written for a learning purpose
class User:
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "username": {"type": "string"},
            "firstName": {"type": "string"},
            "lastName": {"type": "string"},
            "password": {"type": "string"},
        },
        "required":["username", "firstName", "lastName", "password"]}

    def __init__(self, id, username, firstName, lastName, email, password):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password

    def serialize_to_json(self):
        return self.__dict__

    def from_json(csl, json_dict):
        return csl(**json_dict)

    def validate_json(self, data):
        try:
            jsonschema.validate(data, self.schema)
        except jsonschema.exeption.ValidationError:
            return False
        return True

# before put in the body to response user.serialize_to_json()
# self.user_list should contain users with type of User class


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    users_list_session = []

    def _set_response(self, status_code=200, body=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode('utf-8'))


    def _pars_body(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        return json.loads(self.rfile.read(content_length).decode('utf-8'))  # <--- Gets the data itself


    def check_id_user(self, user_id):
        if self.users_list:
            return [True if user['id'] == user_id else False for user in self.users_list][0]
        else:
            return False


    @staticmethod
    def check_keys_user(keys):
        for key in USERS_KEYS:
            if key not in keys:
                return True
        return False


    def check_user(self, body):
        if self.check_keys_user(body.keys()) or self.check_id_user(body.get("id")):
            status = 400
        else:
            status = 201
        return status


    def get_idx_user(self, user_id=None, username=None):
        if not self.users_list: return None
        if user_id:
            return [i if user['id'] == user_id else None for i, user in
                    enumerate(self.users_list)][0]
        elif username:
            return [i if user['username'] == username else None for i, user in
                    enumerate(self.users_list)][0]


    def do_GET(self):

        if self.path == "/users":
            self._set_response(200, self.users_list)

        elif self.path.startswith("/user/"):

            # find user in the self.users_list
            username = self.path.split("/")[-1]
            idx = self.get_idx_user(username=username)

            if idx is not None:
                self._set_response(200, self.users_list[idx])
            else:
                self._set_response(400, {"error": "User not found"})

        elif self.path == "/reset":
            SimpleHTTPRequestHandler.users_list = copy.deepcopy(USERS_LIST)
            self._set_response(204) # no content
        else:
            self._set_response(418)


    def do_POST(self):

        if self.path == "/user":
            body = self._pars_body()
            status = self.check_user(body)
            body = {} if status == 400 else body
            self._set_response(status, body)

        elif self.path == "/user/createWithList":
            body = self._pars_body()

            for user in body:
                status = self.check_user(user)
                if status == 400:
                    body = {}
                    break

            self._set_response(status, body)

        else:
            self._set_response(418)


    def do_PUT(self):

        if self.path.startswith("/user/"):
            body = self._pars_body()
            # find user in the self.users_list
            username = self.path.split("/")[-1]
            idx = self.get_idx_user(username=username)
            if idx is not None:
                keys_update = body.keys()

                # not valid only username is lack ???
                # assumed all of other field could be updated in case
                if "username" not in keys_update or "id" in keys_update:
                    self._set_response(400, {"error": "not valid request data"})
                else:
                    # getting dict of not updating fields
                    dict_save = {key: item for key, item in self.users_list[idx].items()
                                 if key not in keys_update}

                    updated_data = dict(**body, **dict_save)
                    self.users_list[idx].update(updated_data)
                    self._set_response(200, updated_data)

            else:
                self._set_response(404, {"error": "User not found"})
        else:
            self._set_response(418)


    def do_DELETE(self):

        if self.path.startswith("/user/"):
            id_ = self.path.split("/")[-1]
            try:
                id_ = int(id_)
                idx = self.get_idx_user(user_id=id_)
                if idx is not None:
                    self.users_list.pop(idx)
                    status = 200
                    body = {}
                else:
                    status = 404
                    body = {"error": "User not found"}
                self._set_response(status, body)

            except ValueError:
                self._set_response(404, {"error": "User not found"})
        else:
            self._set_response(418)


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='localhost', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
