# Task List
tasks = []

# Display welcome message and menu
def show_menu():
    print("Welcome to Elijah's To-Do List App!\n")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

# Add a task
def add_task():
    title = input("Enter the title of the task: ")
    tasks.append({'title': title, 'status': 'Incomplete'})
    print("Task added successfully!")

# View all tasks
def view_task():
    if tasks: 
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task['title']} - {task['status']}")
    else:
        print("No task available.")

# Mark a task as complete
def mark_task_complete():
    if tasks:
        view_task()
        task_number = int(input("Enter the task number to mark as complete: "))
        if 0 < task_number <= len(tasks):
            tasks[task_number -1]['status'] = 'Complete'
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks available to mark complete.")

# Delete a task
def delete_task():
    if tasks:
        view_tasks()
        task_number = int(input("Enter the task number to delete: "))
        if 0 < task_number <= len(tasks):
            del tasks[task_number - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task number")
    else:
        print("No tasks available to delete")

# Function to run the application
def run_app():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Thank you for using Elijah's To-Do List App. Have a great day!")
            break
        else:
            print("Invalid choice. Please choose a number 1-5.")

# Run the Program
run_app()