# Project Requirements

# User Interface (UI):
# Create a command-line interface (CLI) for the To-Do List Application.
# Display a welcoming message and a menu with the following options:
#         Welcome to the To-Do List App!

#         Menu:
#         1. Add a task
#         2. View tasks
#         3. Mark a task as complete
#         4. Delete a task
#         5. Quit

def display_menu():
    print("Welcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5.Quit")
# make sure you start building your CLI first it helps with your future plans of input

def get_choice():
    number_choices = ["1","2","3","4","5"]
    while True:
        choice = input("Enter your choice (1-5): ")
        if choice in number_choices:
            return choice
        else: 
            print("Invalid choice. Please try again.")
# This will help us select what option we would like to use

tasks = []

def add_task():
    title = input("Enter what task needs to get done: ")
    tasks.append({"title": title, "status": "Incomplete"})
    print(f'Task "{title}" added.')

def view_tasks():
    if not tasks:
        print("No tasks.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f'{index + 1}. {task["title"]} - {task["status"]}')

def mark_task_complete():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the tasks number to mark as complete: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num -1]["status"] = "Complete"
                print(f"Tasks '{tasks[task_num -1]['title']}' marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a number.")

def delete_task():
    view_tasks()
    if tasks:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f'Task "{deleted_task["title"]}" deleted.')
        else:
            print("Invalid task number.")
    else:
        print("No tasks to delete.")

def main():
    while True:
        display_menu()
        choice = get_choice()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

if __name__=="__main__":
    main()

# To-Do List Features:
# Implement the following features for the To-Do List:
# Adding a task with a title (by default “Incomplete”).
# Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
# Marking a task as complete.
# Deleting a task.
# Quitting the application.
# User Interaction:
# Allow users to interact with the application by selecting menu options using input().
# Implement input validation to handle unexpected user input gracefully.
# Error Handling:
# Implement error handling using try, except, else, and finally blocks to handle potential issues.
# Code Organization:
# Organize your code into functions to promote modularity and readability.
# Use meaningful function names with appropriate comments and docstrings for clarity.
# Testing and Debugging:
# Thoroughly test your application to identify and fix any bugs.
# Consider edge cases, such as empty task lists or incorrect user input.
# Documentation:
# Include a README file that explains how to run the application and provides a brief overview of its features.
# Optional Features (Bonus):
# If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.
# GitHub Repository:
# Create a GitHub repository for your project.
# Commit your code to the repository regularly.
# Include a link to your GitHub repository in your project documentation.
