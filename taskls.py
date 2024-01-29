task_list = []

# def generate_unique_id(id = 0):
#     if not task_list:
#         return 1
#     return max(task['id'] for task in task_list) + 1

def add_task():
    task_id = input('enter a task id: ')
    description = input("Enter task description: ")
    if not description:
        print("Task description cannot be empty.")
        return
    status = "incompelete"
    priority = "none"
    task = {
        'id': task_id,
        'description': description,
        'compeletion': status,
        'priority': priority
    }
    task_list.append(task)
    print("Task added successfully.")

def remove_task():
    task_id = int(input('please enter the task id which you want removed: '))
    for task in task_list:
        task_id == task['id']
        task_list.remove(task)
        print('task removed')
        return
    else:
        print('task not found in task list')

def list_tasks():
    if not task_list:
        print('no such task found')
        return
    for task in task_list:
        print(f"ID: {task['id']},Description: {task['description']},Status: {task['compeletion']},Priority: {task['priority']}")

# def toggle_task_completion():
#     task_id = int(input("Enter the task ID to mark as completed/not completed: "))
#     for task in task_list:
#         if task['id'] == task_id:
#             task['completed'] = not task['completed']
#             print("Task status updated.")
#             return
#     print("Task not found in the to-do list.")


def task_status():
    task_id = input("please enter id of the task to change status: ")
    status = input("enter status of the task: ")
    for task in task_list:
        if task['id'] == task_id:
            task['compeletion'] = status
            print('task status updated')
            return

def list_compeleted():
    if not task_list:
        print('to tasks found')
    for task in task_list:
        if task['compeletion'] == 'compelete':
            print(f"ID: {task['id']},Description: {task['description']},"
                f"Status: {task["compeletion"]},{task['priority']}")
    else:
        print('task not in task list')

def task_priority():
    task_id = input('enter the if of the task to which you want to set priority: ')
    priority = input("please enter the priority of the task(low,medium,high)").lower()
    for task in task_list:
        if task['id'] == task_id:
            if priority in('low','medium','high'):
                task['priority'] = priority
                print("task priority updated")
            else:
                print("wrong priority please enter either low, medium or high")
            return
    else:
        print('task not foun in task list check id')

def list_by_priority():
    if not task_list:
        print('no tasks to list')
    for task in task_list:
        print(min(list({task['priority']})))


# def list_by_priority():
#     if not task_list:
#         print('to tasks found')
#     criteria=['high','medium','low']
#     for task in task_list:
#         for k in criteria:
#             # print(my)
#             # for task['priority'] in ('low','medium','high') :
#             print(f"ID: {task['id']},Description: {task['description']},"
#                 f"Status: {task["compeletion"]},{task['priority']}")
#     return


while True:
    print("Welcome to the task list menue.\nto add a task press 1\nto remove a task press 2\n"
          "to list all the tasks press 3\nto change task status press 4\nto list compeleted tasks press 5\n"
          "to change task priority press 6\n to list by priority 7\nto exit press q")

    choice = input('please choose the desired operation: ')

    if choice == '1':
        add_task()
    if choice == '2':
        remove_task()
    if choice == '3':
        list_tasks()
    if choice == '4':
        task_status()
    if choice == '5':
        list_compeleted()
    if choice == '6':
        task_priority()
    if choice == '7':
        list_by_priority()
    if choice =='q':
        print('quitting')
        break

