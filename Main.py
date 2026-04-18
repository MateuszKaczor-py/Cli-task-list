import json
import argparse

filename ='tasks_data.json'
parser = argparse.ArgumentParser()
def add_task(task: str):
    
    try:
        with open(filename, 'r', encoding='utf8') as file:
                tasks = json.load(file)
    except FileNotFoundError:
        tasks = {}
    
    try:   


        new_id = str(len(tasks) + 1)
        
        tasks[new_id] = {"description" : task, "Status" : "Not Done"}

        
        with open(filename,'w', encoding='utf8') as file:
            json.dump(tasks, file,ensure_ascii=False, indent=4)
        print(f"Task was added '{task}',status: 'Not Done', ID:{new_id}")
    except json.JSONDecodeError:
        print("Error: Data file is corrupted")

def delete_task(num_of_task: int):
    
    try:
        with open(filename, 'r') as file:
                tasks = json.load(file)
    
    

        str_num = str(num_of_task)
        
        if str_num in tasks:
            deleted_task = tasks.pop(str_num)
            reindexed_tasks = {}
            for new_num, task_value in enumerate(tasks.values(), start=1):
                reindexed_tasks[str(new_num)] = task_value
                tasks = reindexed_tasks 
            with open(filename,'w', encoding='utf8') as file:
                json.dump(tasks, file, indent=4)
                print(f'Task with ID:{str_num} "{deleted_task}" was deleted')
        else:
            print(f"There's no task with ID:{str_num}")
        
    except FileNotFoundError:
        print("Error: No data file found.")
    
    except json.JSONDecodeError:
        print("Error: Data file is corrupted.")
    
def update_task(num_of_task: int, updated_task: str):
    
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
            
            str_num = str(num_of_task)
            
            if str_num in tasks:
                tasks[str_num] = updated_task
                with open(filename,'w', encoding='utf8') as file:
                    json.dump(tasks,file,indent=4)
                    print(f"Task was succesfully updated")
                    print(f"{updated_task}, ID:{num_of_task}")
            else:
                print('There is no tasks to update')
    except FileNotFoundError:
        print("Error: No data file found.")
    
    except json.JSONDecodeError:
        print("Error: Data file is corrupted.")

def show_task_list():
    
    try:
        with open(filename, 'r', encoding='utf8') as file:
            tasks = json.load(file)

            
            print(f"Here's list of tasks")
            for key, val in tasks.items():
                print(f"'{val}', ID:{key}")
            
    except  FileNotFoundError:
        print("Error: No data file found.")
    except json.JSONDecodeError:
        print("Error: Data file is corrupted.")




def change_status(num_of_task : int, status : str):
    try:
        with open(filename, 'r', encoding='utf8') as file:
            tasks = json.load(file)
            
        str_num = str(num_of_task)
        
        lwr_status = status.lower()

        if lwr_status == "done":
            status_type = 'Done'
        elif lwr_status == "in_progress":
            status_type = 'In progress'
        elif lwr_status == "not_done":
            status_type = 'Not Done'
        
        
        tasks[str_num]["status"] = status_type

        with open(filename,'w', encoding='utf8') as file:
                json.dump(tasks, file, indent=4)

        print(f"Status of task {num_of_task} changed to {status_type}")
        
    except UnboundLocalError:
            print(f"There's no option like {status}")   
    except KeyError:
            print(f"There's no task with ID: {num_of_task}") 
    except  FileNotFoundError:
        print("Error: No data file found.")
    except json.JSONDecodeError:
        print("Error: Data file is corrupted.")
    
            

parser = argparse.ArgumentParser('command', description="Task Tracker CLI")
subparsers = parser.add_subparsers(dest="command", required=True)

add_parser = subparsers.add_parser('add_task', help="Add a new task")
add_parser.add_argument('value', type=str, help="The task description")

delete_parser = subparsers.add_parser('delete_task', help="Delete task")
delete_parser.add_argument('id', type=str, help='ID of the task')

update_parser = subparsers.add_parser('update_task', help="Update a task")
update_parser.add_argument('id', type=str, help='ID of the task')
update_parser.add_argument('value', type=str, help='The task updated description')


status_parser = subparsers.add_parser('change_status', help= 'Change status of task')
status_parser.add_argument('id', type=str, help='ID of the task')
status_parser.add_argument('status_type', type=str,choices=['done','in_progress','not_done'], help= 'Status type done, in-progress, not-done')

list_parser = subparsers.add_parser('show_task_list', help='Showing the task list')

args = parser.parse_args()

if args.command == 'add_task':
    add_task(args.value)

elif args.command == 'delete_task':
    delete_task(args.id)

elif args.command == 'update_task':
    update_task(args.id, args.value)

elif args.command == 'show_task_list':
    show_task_list()

elif args.command == 'change_status':
    change_status(args.id, args.status_type)



