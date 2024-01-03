#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def get_todo_list(employee_id):
    """Retrieve TODO list for the given employee ID."""
    api_url = "https://jsonplaceholder.typicode.com/"
    
    # Retrieve user information
    user_response = requests.get(api_url + "users/{}".format(employee_id))
    if user_response.status_code != 200:
        print("Failed to retrieve user data. Status code:", user_response.status_code)
        sys.exit(1)
    
    user = user_response.json()

    # Retrieve TODO list for the given employee ID
    todos_response = requests.get(api_url + "todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Failed to retrieve TODO data. Status code:", todos_response.status_code)
        sys.exit(1)

    todos = todos_response.json()
    return user, todos

def display_todo_progress(user, todos):
    """Display TODO list progress for the given employee ID."""
    completed = [t.get("title") for t in todos if t.get("completed")]

    # Display output
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Display titles of completed tasks
    [print("\t {}".format(c)) for c in completed]

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("USAGE: python3 script_name.py <employee_id>")
        sys.exit(1)

    # Convert the second command-line argument into an integer (employee ID)
    employee_id = int(sys.argv[1])

    # Get user and TODO list data
    user, todos = get_todo_list(employee_id)

    # Display TODO list progress
    display_todo_progress(user, todos)
