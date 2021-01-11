#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following
example (tabulation before -)
"""
import requests

if __name__ == "__main__":
    URL = "https://intranet.hbtn.io/status"
    req = requests.get(URL)

    print("Body response:")
    print("\t- type:", type(req.content.decode("utf-8")))
    print("\t- content:", req.content.decode("utf-8"))
