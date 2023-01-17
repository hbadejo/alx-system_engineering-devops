#!/usr/bin/python3
# Returns to-do list information for a given employee ID.
import requests
import sys


def emp_todo():
    """
    Python script that, using this REST API, 
    for a given employee ID, 
    returns information about his/her TODO list progress.

    Requirements:
        You must use urllib or requests module
        The script must accept an integer as a parameter, 
        which is the employee ID
    """
    url = "https://jsonplaceholder.typicode.com/"
    emp = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [data.get("title")
                 for data in todo if data.get("completed") is True]
    print("Employee {} is done with tasks({}/{})".format(emp.get("name"),
          len(completed), len(todo)))
    [print("\t {}".format(com_title)) for com_title in completed]


if __name__ == "__main__":
    emp_todo()

