"""Task Scheduler - priority queue (min-heap) implementation.

ITDPA2-44 Data Structures and Algorithms in Python - Question 1.
"""
import heapq
import json


# Task Class
class Task:
    def __init__(self, description, due_date, priority, est_time):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.est_time = est_time

    def __lt__(self, other):
        # lower priority number = higher importance
        return self.priority < other.priority

    def __repr__(self):
        return f"{self.description} (Priority: {self.priority}, Due: {self.due_date}, Est. time: {self.est_time} hrs)"

    def print_info(self):
        print(f"Task: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority}\nEstimated Time: {self.est_time} hrs\n")

# Scheduler Class
class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        heapq.heappush(self.tasks, task)
        print("Task added successfully.\n")

    def get_next_task(self):
        if self.tasks:
            next_task = heapq.heappop(self.tasks)
            print("Next task to do:")
            next_task.print_info()
        else:
            print("No tasks available.\n")

    def print_task_list(self):
        print("\nCurrent Task List (by priority):")
        for t in sorted(self.tasks, key=lambda x: x.priority):
            print(f"- {t}")
        print()

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump([t.__dict__ for t in self.tasks], file)
        print("Tasks saved to file.\n")

    def read_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**data) for data in tasks_data]
            print("Tasks loaded from file.\n")
        except FileNotFoundError:
            print("No saved task file found.\n")

# Main Menu
def main():
    scheduler = Scheduler()

    while True:
        print("===== Task Scheduler Menu =====")
        print("1. Add Task")
        print("2. View Next Task")
        print("3. View All Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            desc = input("Enter task description: ")
            due = input("Enter due date (YYYY-MM-DD): ")
            priority = int(input("Enter priority (1 = highest): "))
            time = float(input("Enter estimated time (hours): "))
            scheduler.add_task(Task(desc, due, priority, time))
        elif choice == "2":
            scheduler.get_next_task()
        elif choice == "3":
            scheduler.print_task_list()
        elif choice == "4":
            scheduler.save_tasks()
        elif choice == "5":
            scheduler.read_tasks()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
