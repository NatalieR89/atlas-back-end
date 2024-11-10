#!/usr/bin/python3
'''Module'''

import requests
import sys
import json

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

    # Prepare data for JSON export
    json_data = {str(employee_id): []}

    # Add each task as a dictionary to the list for the employee
    for task in tasks_data:
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        }
        json_data[str(employee_id)].append(task_data)

    # Write the data to a JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, ensure_ascii=False, indent=4)

    print(f"Data has been exported to {json_filename}")

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
