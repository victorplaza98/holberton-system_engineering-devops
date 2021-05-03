#!/usr/bin/python3
"""
Python script that, using this REST API,
"""

import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    number_of_tasks = []
    for task in todo:
        if task.get('completed') is True:
            number_of_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(number_of_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in number_of_tasks))
