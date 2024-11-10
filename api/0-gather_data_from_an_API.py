#!/usr/bin/python3
'''Module'''

import requests
import sys


def get_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee's details (name, etc.)
    employee_url = f'{base_url}/users/{employee_id}'
    employee_response = requests.get(employee_url)

    # Check if the employee exists
    if employee_response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found.")
        return

    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch the employee's TODO tasks
    tasks_url = f'{base_url}/todos?userId={employee_id}'
    tasks_response = requests.get(tasks_url)

    if tasks_response.status_code != 200:
        print("Error: Unable to fetch tasks data.")
        return

    tasks_data = tasks_response.json()

    # Filter completed tasks
    completed_tasks = 
    [task['title'] for task in tasks_data if task['completed']]
    total_tasks = len(tasks_data)
    completed_tasks_count = len(completed_tasks)

    # Display the employee TODO list 
    # progress in the required format
    print(f'Employee {employee_name} is done with tasks({completed_tasks_count}/{total_tasks}):')
    for task in completed_tasks:
        print(f'\t {task}')

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
