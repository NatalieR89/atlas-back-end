#!/usr/bin/python3
'''Module'''

import urllib.request
import urllib.error
import sys
import json


def get_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee's details (name, etc.)
    employee_url = f'{base_url}/users/{employee_id}'

    try:
        with urllib.request.urlopen(employee_url) as response:
            employee_data = json.load(response)
    except urllib.error.HTTPError as e:
        print(f"Error: Unable to fetch employee data for ID 
              {employee_id}. HTTP Error {e.code}.")
        return
    except urllib.error.URLError as e:
        print(f"Error: Unable to fetch employee data. URL Error {e.reason}.")
        return

    employee_name = employee_data.get('name')

    # Fetch the employee's TODO tasks
    tasks_url = f'{base_url}/todos?userId={employee_id}'

    try:
        with urllib.request.urlopen(tasks_url) as response:
            tasks_data = json.load(response)
    except urllib.error.HTTPError as e:
        print(f"Error: Unable to fetch tasks data for employee 
              {employee_name} (ID: {employee_id}). HTTP Error {e.code}.")
        return
    except urllib.error.URLError as e:
        print(f"Error: Unable to fetch tasks data. URL Error {e.reason}.")
        return

    # Filter completed tasks
    completed_tasks = [task['title'] 
                       for task in tasks_data if task['completed']]
    total_tasks = len(tasks_data)
    completed_tasks_count = len(completed_tasks)

    # Display the employee TODO list progress in the required format
    print(f"Employee {employee_name} is done with tasks({completed_tasks_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == '__main__':
    # Ensure that the script has been called with an employee ID
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])  # Parse the employee ID
    except ValueError:
        print("Error: Employee ID should be an integer.")
        sys.exit(1)

    # Call the function to fetch and display employee TODO progress
    get_employee_todo_progress(employee_id)
