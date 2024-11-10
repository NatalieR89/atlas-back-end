import requests
import sys

def fetch_employee_todo_data(employee_id):
    # Define the base URL for the API
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    # Make a GET request to fetch the TODO data for the given employee ID
    response = requests.get(url)
    
    # If the request is successful (status code 200), return the JSON data
    if response.status_code == 200:
        return response.json()
    else:
        # Handle failure, for example, employee not found
        print(f"Error: Could not retrieve data for employee ID {employee_id}")
        sys.exit(1)

def display_employee_progress(employee_id):
    # Fetch the TODO data for the employee
    todos = fetch_employee_todo_data(employee_id)
    
    # Extract the employee's name from the user API endpoint
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code == 200:
        employee_name = user_response.json().get("name")
    else:
        print(f"Error: Could not retrieve employee data for ID {employee_id}")
        sys.exit(1)

    # Filter completed tasks
    completed_tasks = [task['title'] for task in todos if task['completed']]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)
    
    # Output the progress in the requested format
    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    
    # Output each completed task title with proper formatting
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    # Ensure that an employee ID is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command line argument
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    # Display the employee's TODO list progress
    display_employee_progress(employee_id)
