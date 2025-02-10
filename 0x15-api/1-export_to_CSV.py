#!/usr/bin/python3
"""
Extends a script to export data to csv format
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{base_url}users/{employee_id}").json()
    todos = requests.get(f"{base_url}todos",
                         params={"userId": employee_id}).json()

    with open(f"{employee_id}.csv", "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow(
                [t["userId"], user["name"], t["completed"], t["title"]]
            )
