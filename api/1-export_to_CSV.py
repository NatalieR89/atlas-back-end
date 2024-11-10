#!/usr/bin/python3
'''Module'''
import csv
import json
import sys
import urllib.error
import urllib.request


def get_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee's details (name, etc.)
    employee_url = f'{base_url}/users/{employee_id}'

    try:
        with urllib.request.urlopen(employee_url) as response:
            employee_data = json.load(response)
    except urllib.error.HTTPError as e:
        print(f"Error: Unable to fetch employee data for ID {employee_id}. HTTP Error {e.code}.")
        return
    except urllib.error.URLError as e:
        print(f"Error: Unable to fetch employee data. URL Error {e.reason}.")
        return

    employee_name = employee_data.get('username')

    # Fetch the employee's TODO tasks
    tasks_url = f'{base_url}/todos?userId={employee_id}'

    try:
        with urllib.request.urlopen(tasks_url) as response:
            tasks_data = json.load(response)
    except urllib.error.HTTPError as e:
        print(f"Error: Unable to fetch tasks data for employee {employee_name} (ID: {employee_id}). HTTP Error {e.code}.")
        return
    except urllib.error.URLError as e:
        print(f"Error: Unable to fetch tasks data. URL Error {e.reason}.")
        return

    # Prepare data for CSV output
    csv_filename = f"{employee_id}.csv"
    try:
        with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in tasks_data:
                csvwriter.writerow([employee_id, employee_name, task['completed'], task['title']])
        print(f"Data successfully written to {csv_filename}")
    except IOError as e:
        print(f"Error: Unable to write to file {csv_filename}. I/O Error: {e}")

    # Display the employee TODO list progress in the required format
    completed_tasks = [task['title'] for task in tasks_data if task['completed']]
    total_tasks = len(tasks_data)
    completed_tasks_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({completed_tasks_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == '__main__':
    # Ensure that the script has been called with an employee ID
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])  # Parse the employee ID
    except ValueError:
        print("Error: Employee ID should be an integer.")
        sys.exit(1)

    # Call the function to fetch and display employee TODO progress
    get_employee_todo_progress(employee_id)
