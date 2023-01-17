#!/usr/bin/python3
"""Exports to-do list information for a given employee to JSON format."""
import json
import requests
import sys


def ex_emp_todo_json():
    """ Export to-do to CSV file """

    url = "https://jsonplaceholder.typicode.com/"
    emp = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user_id = sys.argv[1]
    username = emp.get("username")

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump({user_id: [{
            "task": data.get("title"),
            "completed": data.get("completed"),
            "username": username
        } for data in todo]}, jsonfile)


if __name__ == "__main__":
    ex_emp_todo_json()
