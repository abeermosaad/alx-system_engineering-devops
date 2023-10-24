#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
import requests

if __name__ == "__main__":

    url = f"https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url)
    employees = response.json()

    users = len(employees)
    dictionary = {}

    for i in range(1, users):
        li = []
        url = f"https://jsonplaceholder.typicode.com/users/{i}"
        response = requests.get(url)
        employee = response.json()

        url2 = f"https://jsonplaceholder.typicode.com/todos?userId={i}"
        response2 = requests.get(url2)
        todos = response2.json()

        total = len(todos)
        for j in range(total):
            dic = {}
            dic['username'] = employee.get("username")
            dic['task'] = todos[j].get("title")
            dic['completed'] = todos[j].get('completed')
            li.append(dic)
        dictionary[str(i)] = li

    with open("todo_all_employees.json", "w") as file:
        json.dump(dictionary, file)
