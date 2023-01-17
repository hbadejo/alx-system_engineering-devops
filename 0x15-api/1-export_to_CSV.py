#!/usr/bin/python3
import csv
import requests
import sys


def ex_emp_todo_csv():
    """
    Export to-do to CSV file

    Requirements:
        Records all tasks that are owned by this employee
        Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
        File name must be: USER_ID.csv
    """


    url = "https://jsonplaceholder.typicode.com/"
    emp = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user_id = sys.argv[1]


    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        pen = csv.writer(csvfile)
        [pen.writerow(
            [user_id, emp.get("username"), data.get("complete"), data.get("title")]
            ) for data in todo]


if __name__ == "__main__":
    ex_emp_todo_csv()
