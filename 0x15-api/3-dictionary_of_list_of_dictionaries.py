#!/usr/bin/python3
"""
a
"""

import json
import requests

if __name__ == '__main__':
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         verify=False).json()
    user_dict = {}
    username_dict = {}
    for user in users:
        uid = user.get("id")
        userdict[uid] = []
        usernamedict[uid] = user.get("username")
    todo = requests.get("https://jsonplaceholder.typicode.com/todos",
                        verify=False).json()
    for task in todo:
        tasks_json = {}
        uid = task.get("userId")
        tasks_json["task"] = task.get('title')
        tasks_json["completed"] = task.get('completed')
        tasks_json["username"] = username_dict.get(uid)
        user_dict.get(uid).append(tasks_json)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
