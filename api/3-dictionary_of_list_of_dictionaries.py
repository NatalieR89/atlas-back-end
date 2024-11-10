#!/usr/bin/python3
'''Module'''

import requests
import sys
import json

def get_all_employees_todo():
    # Base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch all employees
    users_url = f'{base_url}/users'
    users_response = requests.get(users_url)

    if users_response.status_code != 200:
        print("Error: Unable to fetch users data.")
        return

    users_data = users_response.json()

    # Prepare the data for all employees' TODO lists
    all_tasks_data = {}

    for user in users_data:
        user_id = user['id']
        username = user['name']

        # Fetch the user's TODO tasks
        tasks_url = f'{base_url}/todos?userId={user_id}'
        tasks_response = requests.get(tasks_url)

        if tasks_response.status_code != 200:
            print(f"Error: Unable to fetch tasks data for user {username} (ID: {user_id}).")
            continue

        tasks_data = tasks_response.json()

        # Store tasks for this user
        user_tasks = []
        for task in tasks_data:
            user_tasks.append({
                'username': username,
                'task': task['title'],
                'completed': task['completed']
            })

        all_tasks_data[str(user_id)] = user_tasks

    # Write the data to a JSON file
    json_filename = 'todo_all_employees.json'
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(all_tasks_data, jsonfile, ensure_ascii=False, indent=4)

    print(f"Data has been exported to {json_filename}")

if __name__ == '__main__':
    # Call the function to fetch and export all employees' TODO lists
    get_all_employees_todo()
