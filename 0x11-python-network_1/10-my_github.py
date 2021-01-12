#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id

    You must use Basic Authentication with a personal access token as
    password to access to your information (only read:user permission is needed)
    The first argument will be your username
    The second argument will be your password
    (in your case, a personal access token as password)
    You must use the package requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type)
"""
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    token = argv[2]
    URL = "https://api.github.com/user"

    req = requests.get(URL, auth={user, token}).text
    try:
        output = req[req.index("id") + 4: req.index("node") - 2]
    except ValueError:
        output = "None"
    print(output)
