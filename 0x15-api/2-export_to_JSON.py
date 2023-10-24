#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    arg1 = int(sys.argv[1])
    url = f"https://jsonplaceholder.typicode.com/users/{arg1}/"
    response = requests.get(url)

    url2 = f"https://jsonplaceholder.typicode.com/todos?userId={arg1}"
    response2 = requests.get(url2)

    employee = response.json()
    todos = response2.json()

    total = len(todos)
    dictionary = {}
    li = []

    for i in range(total):
        dic = {}
        dic['task'] = todos[i].get("title")
        dic['completed'] = todos[i].get('completed')
        dic['username'] = employee.get("username")
        li.append(dic)

    dictionary[str(arg1)] = li
    with open(f"{arg1}.json", "w") as file:
        json.dump(dictionary, file)
