#!/usr/bin/python3
"""
Extends a script to export data to csv format
"""
import sys
import requests
import csv


if __name__ == "__main__":
    """
    Records all tasks that are owned by an employee and save em in a csv
    file
    """
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{base_url}users/{employee_id}").json()
    todos = requests.get(f"{base_url}todos",
                         params={"userId": employee_id}).json()

    with open(f"{employee_id}.csv", "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow([employee_id, user["username"], t["completed"],
                          t["title"]]) for t in todos]
