#!/usr/bin/python3
"""Python script to export data in the CSV format"""
import csv
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

    with open(f'{arg1}.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)

        for i in range(total):
            row = []
            row.append(str(arg1))
            row.append(employee.get("username"))
            row.append(str(todos[i].get('completed')))
            row.append(todos[i].get("title"))

            writer.writerow(row)
