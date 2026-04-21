import json
import argparse
import time

filename = 'tasks_data.json'


def load_tasks():
    # Returns None on corruption (after printing the error) so callers can early-return.
    # FileNotFoundError is treated as an empty store so the first add can create the file.
    try:
        with open(filename, 'r', encoding='utf8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: Data file is corrupted.")
        return None


def save_tasks(tasks):
    with open(filename, 'w', encoding='utf8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def add_task(task: str):
    if not task.strip():
        print("Error: Task description cannot be empty.")
        return

    tasks = load_tasks()
    if tasks is None:
        return

    new_id = str(max((int(k) for k in tasks), default=0) + 1)
    now = time.asctime()
    tasks[new_id] = {"description": task, "status": "Not Done", "created_at": now, "updated_at": now}

    save_tasks(tasks)
    print(f"Task was added '{task}', status: 'Not Done', ID:{new_id}")


def delete_task(num_of_task: str):
    tasks = load_tasks()
    if tasks is None:
        return

    str_num = str(num_of_task)
    if str_num not in tasks:
        print(f"There's no task with ID:{str_num}")
        return

    deleted_task = tasks.pop(str_num)
    reindexed_tasks = {}
    for new_num, task_value in enumerate(tasks.values(), start=1):
        reindexed_tasks[str(new_num)] = task_value

    save_tasks(reindexed_tasks)
    print(f'Task with ID:{str_num} "{deleted_task["description"]}" was deleted')


def update_task(num_of_task: str, updated_task: str):
    if not updated_task.strip():
        print("Error: Updated description cannot be empty.")
        return

    tasks = load_tasks()
    if tasks is None:
        return

    str_num = str(num_of_task)
    if str_num not in tasks:
        print('There are no tasks to update')
        return

    tasks[str_num]["description"] = updated_task
    tasks[str_num]["updated_at"] = time.asctime()

    save_tasks(tasks)
    print("Task was successfully updated")
    print(f"{updated_task}, ID:{num_of_task}")


def show_task_list(arg: str):
    arg = arg.lower()
    tasks = load_tasks()
    if tasks is None:
        return

    if arg == 'all':
        print("Here's list of all tasks")
        for key, val in tasks.items():
            print(f"'{val}', ID:{key}")
        return

    status_map = {'done': 'Done', 'not_done': 'Not Done', 'in_progress': 'In progress'}
    target = status_map[arg]
    matches = [(k, v) for k, v in tasks.items() if v["status"] == target]
    if not matches:
        print(f"There's no tasks with status {target}")
        return
    for key, val in matches:
        print(f"{val['description']}, {val['status']}, ID:{key}")


def change_status(num_of_task: str, status: str):
    status_map = {"done": "Done", "in_progress": "In progress", "not_done": "Not Done"}
    lwr_status = status.lower()
    if lwr_status not in status_map:
        print(f"There's no option like {status}")
        return
    status_type = status_map[lwr_status]

    tasks = load_tasks()
    if tasks is None:
        return

    str_num = str(num_of_task)
    if str_num not in tasks:
        print(f"There's no task with ID: {num_of_task}")
        return

    tasks[str_num]["status"] = status_type
    save_tasks(tasks)
    print(f"Status of task {num_of_task} changed to {status_type}")


parser = argparse.ArgumentParser(description="Task Tracker CLI")
subparsers = parser.add_subparsers(dest="command", required=True)

add_parser = subparsers.add_parser('add_task', help="Add a new task")
add_parser.add_argument('value', type=str, help="The task description")

delete_parser = subparsers.add_parser('delete_task', help="Delete task")
delete_parser.add_argument('id', type=str, help='ID of the task')

update_parser = subparsers.add_parser('update_task', help="Update a task")
update_parser.add_argument('id', type=str, help='ID of the task')
update_parser.add_argument('value', type=str, help='The task updated description')

status_parser = subparsers.add_parser('change_status', help='Change status of task')
status_parser.add_argument('id', type=str, help='ID of the task')
status_parser.add_argument('status_type', type=str, choices=['done', 'in_progress', 'not_done'], help='Status type done, in-progress, not-done')

list_parser = subparsers.add_parser('show_task_list', help='Showing the task list')
list_parser.add_argument('status_type', type=str, choices=['all', 'done', 'in_progress', 'not_done'], help='Status type done, in-progress, not-done')

args = parser.parse_args()

if args.command == 'add_task':
    add_task(args.value)
elif args.command == 'delete_task':
    delete_task(args.id)
elif args.command == 'update_task':
    update_task(args.id, args.value)
elif args.command == 'show_task_list':
    show_task_list(args.status_type)
elif args.command == 'change_status':
    change_status(args.id, args.status_type)
