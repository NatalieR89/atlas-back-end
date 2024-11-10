#!/usr/bin/python3
'''Module'''
import json
import urllib.error
import urllib.request


def fetch_all_employees_todo_progress():
    # Base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch all employees' details
    employees_url = f'{base_url}/users'
    try:
        with urllib.request.urlopen(employees_url) as response:
            employees_data = json.load(response)
    except urllib.error.HTTPError as e:
        print(f"Error: Unable to fetch employees data. HTTP Error {e.code}.")
        return
    except urllib.error.URLError as e:
        print(f"Error: Unable to fetch employees data. URL Error {e.reason}.")
        return

    # Fetch all TODO tasks for all users
    tasks_url = f'{base_url}/todos'
    try:
        with urllib.request.urlopen(tasks_url) as response:
            tasks_data = json.load(response)
    except urllib.error.HTTPError as e:
        print(f"Error: Unable to fetch tasks data. HTTP Error {e.code}.")
        return
    except urllib.error.URLError as e:
        print(f"Error: Unable to fetch tasks data. URL Error {e.reason}.")
        return

    # Organize tasks by user ID
    all_employees_tasks = {}
    for employee in employees_data:
        user_id = employee['id']
        username = employee['username']
        # Filter tasks for the current user and format them
        user_tasks = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in tasks_data if task['userId'] == user_id
        ]
        all_employees_tasks[str(user_id)] = user_tasks

    # Write the JSON data to a file
    json_filename = "todo_all_employees.json"
    try:
        with open(json_filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(all_employees_tasks, jsonfile, indent=4)
        print(f"Data successfully written to {json_filename}")
    except IOError as e:
        print(f"Error: Unable to write to file {json_filename}. I/O Error: {e}")


if __name__ == '__main__':
    # Call the function to fetch and export all employees' TODO progress
    fetch_all_employees_todo_progress()
