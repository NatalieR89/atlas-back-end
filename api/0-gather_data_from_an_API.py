#!/usr/bin/python3


import requests
import sys


def get_employee_todo_list(employee_id):
    try:
        # Retrieve employee information
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Retrieve employee TODO list
        todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        # Calculate the number of completed tasks and total tasks
        total_tasks = len(todo_list)
        done_tasks = [task for task in todo_list if task.get('completed')]
        number_of_done_tasks = len(done_tasks)

        # Print employee TODO list progress
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task.get('title')}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_list(employee_id)
