To-Do List Manager:
A simple and efficient task management application that helps you organize and track your daily tasks through a command-line interface.

Description:
This is a Python-based to-do list application that allows users to add, view, complete, and delete tasks. The program uses a list of dictionaries to store tasks along with their completion status. This project demonstrates fundamental programming concepts including data structures (lists and dictionaries), loops, conditional statements, and CRUD operations. It's perfect for beginners learning Python or as a portfolio project.

Features:
Add new tasks to your list
View all tasks with completion status
Mark tasks as complete
Delete unwanted tasks
Task counter showing total, completed, and pending tasks
Simple menu-driven interface
No external dependencies required
Data persistence during program execution

How to Use:
1. Run the program
2. Choose an option from the menu (1-5)
3. Add Task: Enter task description
4. View Tasks: See all tasks with status markers
5. Mark Complete: Enter task number to mark as done
6. Delete Task: Enter task number to remove
7. Exit: Close program and see final summary

Variables Used:
t - Task list (stores all tasks)
c - User's menu choice
task - Task description
i - Loop counter
n - Task number for operations
status - Task completion status marker
done - Boolean flag for task completion
completed - Count of completed tasks

Main Components:
1. Menu Display - Show available operations
2. Add Task - Create new task entry
3. View Tasks - Display all tasks with status
4. Mark Complete - Update task completion status
5. Delete Task - Remove task from list
6. Exit Summary - Show final statistics

Project Structure:
todo_list/
│
├── todo.py                # Main to-do list file
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License
└── .gitignore            # Git ignore file

Stay organized! Track your tasks efficiently!
