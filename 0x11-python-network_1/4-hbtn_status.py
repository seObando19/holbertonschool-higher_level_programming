#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following
example (tabulation before -)
"""
from urllib import request

if __name__ == "__main__":
    URL = "https://intranet.hbtn.io/status"

    with request.urlopen(URL) as response:
        res = response.read().decode("utf-8")

    print("Body response:")
    print("\t- type:", type(res))
    print("\t- content:", res)
