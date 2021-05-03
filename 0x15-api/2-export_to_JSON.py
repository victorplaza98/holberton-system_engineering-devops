#!/usr/bin/python3
"""
Python script that, using this REST API,
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    username = user.get('username')
    task = []
    for tasks in todo:
        task_dict = {}
        task_dict["task"] = tasks.get('title')
        task_dict["completed"] = tasks.get('completed')
        task_dict["username"] = username
        task.append(task_dict)
    tasks_json = {}
    tasks_json[userId] = task
    with open("{}.json".format(userId), 'w') as jsonfile:
        json.dump(tasks_json, jsonfile)
