#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header

You must use the packages requests and sys
You are not allow to import other packages than requests and sys
The value of this variable is different for each request
You don’t need to check script arguments (number and type)
"""
import requests
from sys import argv

if __name__ == "__main__":
    URL = argv[1]
    req = requests.get(URL)
    if req.status_code == 200:
        print(req.headers["X-Request-Id"])
