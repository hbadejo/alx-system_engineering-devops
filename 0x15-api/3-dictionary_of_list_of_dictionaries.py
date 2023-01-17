#!/usr/bin/python3
"""Exports to-do list information for a all employees to JSON format."""
import json
import requests


def ex_allemp_todo_json():
    """ Export to-do to CSV file """

    url = "https://jsonplaceholder.typicode.com/"
    allemp = requests.get(url + "users").json()
    todo = requests.get(url + "todos").json()

    with open(f"todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": data.get("title"),
                "completed": data.get("completed"),
                "username": user.get("username")
            } for data in todo] for user in allemp}, jsonfile)


if __name__ == "__main__":
    ex_allemp_todo_json()
