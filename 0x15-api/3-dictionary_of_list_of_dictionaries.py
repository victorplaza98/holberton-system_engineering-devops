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
        user_id = user.get("id")
        user_dict[user_id] = []
        username_dict[user_id] = user.get("username")
    todo = requests.get("https://jsonplaceholder.typicode.com/todos",
                        verify=False).json()
    for task in todo:
        tasks_json = {}
        user_id = task.get("userId")
        tasks_json["task"] = task.get('title')
        tasks_json["completed"] = task.get('completed')
        tasks_json["username"] = username_dict.get(user_id)
        user_dict.get(user_id).append(tasks_json)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
