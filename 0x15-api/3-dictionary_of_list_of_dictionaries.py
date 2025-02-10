#!/usr/bin/python3
"""
Extends a script to export data to csv format
"""
import sys
import requests
import json


if __name__ == "__main__":
    """
    Records all tasks that are owned by an employee and save em in a json
    file
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{base_url}users/").json()
    all_data = {}

    for user in users:
        todos = requests.get(
            f"{base_url}todos",
            params={"userId": user["id"]}
            ).json()

        all_data[user["id"]] = [{
            "username": user["username"],
            "task": t["title"],
            "completed": t["completed"]
        } for t in todos]

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_data, f)
