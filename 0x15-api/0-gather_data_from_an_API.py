#!/usr/bin/python3
"""
Returns information about an employee's TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    """
    Main entry point for the script. Accepts an employee ID as a command-line
    argument.

    Args:
        None

    Returns:
        None: Executes the function `get_employee_todo_progress` for the given
        employee ID.
    """
    employee_id = int(sys.argv[1])
    base_url = f"https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + f"users/{employee_id}").json()
    todos = requests.get(base_url + "todos",
                         params={"userId": sys.argv[1]}).json()

    completed = [t["title"] for t in todos if t["completed"]]
    print(f"Employee {user['name']} is done with "
          f"tasks({len(completed)}/{len(todos)}):")
    for c in completed:
        print(f"\t {c}")
