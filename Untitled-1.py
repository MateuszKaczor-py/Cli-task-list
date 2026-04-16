import json

def add_task(key, value):
    filename = 'tasks_data.json'
    try:
        with open(filename, 'r') as file:
                tasks = json.load(file)
    except FileNotFoundError:
        tasks = {}
    try:
        if not isinstance(key, int):
            tasknum = int(key)
    except ValueError:
        return 'ERROR: KEY IS NOT A INTEGER'
    try:
        if not isinstance(value, str):
            tasktodo = str(value)
    except ValueError:
        return 'ERROR: VALUE IS NOT A STRING'
    tasknum = int(key)
    tasktodo = str(value)
    task = {

}
    task[tasknum] = tasktodo
    
    with open(filename,'w', encoding='utf8') as file:
        json.dump(task, file,ensure_ascii=False, indent=4)
    return f"Task was added {task}"

def delete_task(num_of_task):
    filename = 'tasks_data.json'
    try:
        with open(filename, 'r') as file:
                task = json.load(file)
    
    
    
        str_num = str(num_of_task)

        if str_num in task:
            deleted_task = task.pop(str_num)

        with open(filename,'w', encoding='utf8') as file:
            json.dump(task, file, indent=4)
            return f'Task {deleted_task} was deleted'
    except FileNotFoundError:
        return "Error: No data file found."
    
    except json.JSONDecodeError:
        return "Error: Data file is corrupted."    
def update_task(num_of_task, updated_task):
    filename ='tasks_data.json'
    try:
        with open(filename, 'r') as file:
            task = json.load(file)
            
            str_num = str(num_of_task)
            
            if str_num in str(task):
                task[str_num] = updated_task
            with open(filename,'w', encoding='utf8') as file:
                json.dump(task,file,indent=4)
                return f'Task was succesfully updated'
    except FileNotFoundError:
        return "Error: No data file found."
    
    except json.JSONDecodeError:
        return "Error: Data file is corrupted."

    
# print(add_task(1, 'Take out the trash'))
# print(delete_task(1))
print(update_task(1, 'Going out'))