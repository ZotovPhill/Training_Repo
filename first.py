import sys
import requests

request = requests.get("https://dev.by")
print(request.status_code)
print(sys.version)
print(sys.executable)


def greetings(name):
    greeting = "Hello, {} !".format(name)
    return greeting


print(greetings("Pat"))
