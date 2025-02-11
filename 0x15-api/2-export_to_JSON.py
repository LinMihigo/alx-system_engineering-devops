#!/usr/bin/python3
"""
Extends a script to export data to csv format
"""
import json
import requests
import sys


if __name__ == "__main__":
    """
    Records all tasks that are owned by an employee and save em in a json
    file
    """
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{base_url}users/{employee_id}").json()
    todos = requests.get(f"{base_url}todos",
                         params={"userId": employee_id}).json()

    data = {str(employee_id): [{
        "task": t["title"],
        "completed": t["completed"],
        "username": user["username"]
        } for t in todos]}

    with open(f"{employee_id}.json", "w") as f:
        json.dump(data, f)
