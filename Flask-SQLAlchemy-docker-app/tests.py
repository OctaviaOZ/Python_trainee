import requests

body = dict(id='1')
attrs = ['id', 'name', 'gender', 'date_of_birth'].sort()

response = requests.delete('http://127.0.0.1:8000/api/actor-relations', data=body)
if response.status_code != 200 or list(response.json().keys()).sort() != attrs:
            print("Route '/api/actor_relations' method DELETE failed processing correct request")
print(response.json())


body = dict(name='')
attrs = ['id', 'name', 'gender', 'date_of_birth'].sort()

response = requests.delete('http://127.0.0.1:8000/api/actor-relations', data=body)
if response.status_code != 400:
            print("Route '/api/actor_relations' method DELETE failed handling request with no 'id'")
print(response.json())