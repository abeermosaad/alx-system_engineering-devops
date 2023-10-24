#!/usr/bin/python3
"""Python script that returns information about TODOS list progress"""
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

    complete = 0
    total = len(todos)

    for i in range(total):
        if todos[i].get('completed'):
            complete += 1

    name = employee.get("name")
    print(f'Employee {name} is done with tasks({complete}/{total}):')

    for i in range(total):
        if todos[i].get('completed'):
            print(f'\t {todos[i].get("title")}')
