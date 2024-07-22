
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = '✓' if self.completed else '✗'
        return f"{status} {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Added task: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Removed task: {removed_task.description}")
        else:
            print("Invalid task index.")

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"Marked task as completed: {self.tasks[index].description}")
        else:
            print("Invalid task index.")


1
def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '4':
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_task_complete(index)
        elif choice == '5':
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
