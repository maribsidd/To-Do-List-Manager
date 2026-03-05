"""
To-Do List Manager
A simple task management application for organizing daily tasks
"""

t = []  # task list

print("=" * 50)
print("TO-DO LIST MANAGER")
print("=" * 50)
print()

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    print()
    
    c = input("Enter choice (1-5): ")
    
    if c == '1':
        # Add task
        task = input("Enter task: ")
        t.append({'task': task, 'done': False})
        print(f"Task '{task}' added!")
        
    elif c == '2':
        # View tasks
        if len(t) == 0:
            print("No tasks in list!")
        else:
            print("\nYour Tasks:")
            print("-" * 50)
            for i in range(len(t)):
                status = "✓" if t[i]['done'] else "✗"
                print(f"{i+1}. [{status}] {t[i]['task']}")
            print("-" * 50)
            
    elif c == '3':
        # Mark complete
        if len(t) == 0:
            print("No tasks to mark!")
        else:
            print("\nTasks:")
            for i in range(len(t)):
                print(f"{i+1}. {t[i]['task']}")
            n = int(input("Enter task number to mark complete: "))
            if 1 <= n <= len(t):
                t[n-1]['done'] = True
                print(f"Task '{t[n-1]['task']}' marked as complete!")
            else:
                print("Invalid task number!")
                
    elif c == '4':
        # Delete task
        if len(t) == 0:
            print("No tasks to delete!")
        else:
            print("\nTasks:")
            for i in range(len(t)):
                print(f"{i+1}. {t[i]['task']}")
            n = int(input("Enter task number to delete: "))
            if 1 <= n <= len(t):
                removed = t.pop(n-1)
                print(f"Task '{removed['task']}' deleted!")
            else:
                print("Invalid task number!")
                
    elif c == '5':
        print("\nGoodbye! Stay productive!")
        break
        
    else:
        print("Invalid choice! Please enter 1-5.")

print("\nFinal Task Summary:")
print(f"Total tasks: {len(t)}")
completed = sum(1 for task in t if task['done'])
print(f"Completed: {completed}")
print(f"Pending: {len(t) - completed}")
