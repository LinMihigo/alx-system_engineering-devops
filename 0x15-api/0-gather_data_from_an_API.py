#!/usr/bin/python3
"""
Returns information about an employee's TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    i = 0
    num = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos/1"
    while i < int(num):
        req = requests.request('GET', url)

        if req.ok:
            data = req.json()
            print(data)
        else:
            print("Error code: ", req.status_code)

        i++
