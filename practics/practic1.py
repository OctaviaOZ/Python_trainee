def callback(s):
    print('set ',s)

class Listener:
    def __init__(self, cb = 0):
        self.cb = cb

    @property
    def cb(self):
        print("Getting value...")
        return self._cb


    @cb.setter
    def cb(self, value):
        callback(value)
        self._cb = value

import os

# Set environment variables
os.environ['API_USER'] = 'username'
os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')

print(USER)
print(PASSWORD)