#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
    You must use the package urllib
    You are not allowed to import any packages other than urllib
    The body of the response must be displayed like the following
    example (tabulation before -)
    You must use a with statement
"""
from urllib import request

if __name__ == "__main__":
    URL = "https://intranet.hbtn.io/status"

    with request.urlopen(URL) as route:
        info = route.read()

    print("Body response:")
    print("\t- type:", type(info))
    print("\t- content:", info)
    print("\t- utf8 content:", info.decode("utf-8"))
