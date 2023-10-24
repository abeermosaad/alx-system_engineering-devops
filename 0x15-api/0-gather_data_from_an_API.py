#!/usr/bin/python3
"""Python script that returns information about TODOS list progress"""
import requests
import sys

url = f"https://jsonplaceholder.typicode.com/users/{int(sys.argv[1])}/"
response = requests.get(url)

url2 = f"https://jsonplaceholder.typicode.com/todos?userId={int(sys.argv[1])}"
response2 = requests.get(url2)

employee = response.json()
todos = response2.json()

complete = 0
total = len(todos)

for i in range(total):
    if todos[i].get('completed'):
        complete += 1

print(
    f'Employee {employee.get("name")} is done with tasks({complete}/{total}):')

for i in range(total):
    if todos[i].get('completed'):
        print(f'\t {todos[i].get("title")}')
