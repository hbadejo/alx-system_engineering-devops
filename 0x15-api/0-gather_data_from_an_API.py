#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", uid={"userId": sys.argv[1]}).json()

    completed = [data.get("title") for data in todo if data.get("comleted") is True]
    print(f"Employee {emp.get("name")} is done with tasks({len(completed)}/{len(todos)})")
    [print(f"\t {data}" for data in completed)]
