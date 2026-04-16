import json
import typer
app = typer.Typer()
filename ='tasks_data.json'
@app.command()
def add_task(key: int, value: str):
    
    try:
        with open(filename, 'r') as file:
                tasks = json.load(file)
    except FileNotFoundError:
        tasks = {}
    
    tasknum = str(key)
    tasktodo = str(value)
    
    if tasknum in tasks:
        typer.echo('The tasks number is occupied')
    
    elif tasknum not in tasks:
        tasks[tasknum] = tasktodo
        with open(filename,'w', encoding='utf8') as file:
            json.dump(tasks, file,ensure_ascii=False, indent=4)
        typer.echo(f"Task was added {tasks}")
@app.command()
def delete_task(num_of_task: int):
    
    try:
        with open(filename, 'r') as file:
                tasks = json.load(file)
    
    

        str_num = str(num_of_task)
        
        if str_num in tasks:
            deleted_task = tasks.pop(str_num)
            with open(filename,'w', encoding='utf8') as file:
                json.dump(tasks, file, indent=4)
                typer.echo(f'Task {str_num}. "{deleted_task}" was deleted')
        else:
            typer.echo(f"There's no task like {str_num}")
        
    except FileNotFoundError:
        typer.echo("Error: No data file found.")
    
    except json.JSONDecodeError:
        typer.echo("Error: Data file is corrupted.")
@app.command()    
def update_task(num_of_task: int, updated_task: str):
    
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
            
            str_num = str(num_of_task)
            
            if str_num in tasks:
                tasks[str_num] = updated_task
                with open(filename,'w', encoding='utf8') as file:
                    json.dump(tasks,file,indent=4)
                    typer.echo("Task was succesfully updated")
            else:
                typer.echo('There is no tasks to update')
    except FileNotFoundError:
        typer.echo("Error: No data file found.")
    
    except json.JSONDecodeError:
        typer.echo("Error: Data file is corrupted.")
@app.command()
def show_task_list():
    
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)

        typer.echo(f'Here"s list of tasks {tasks}')
    except  FileNotFoundError:
        typer.echo("Error: No data file found.")



if __name__ == "__main__":
    app()
    
# print(add_task(5, 'Go for a walk'))
# print(delete_task(7))
# print(update_task(1, 'Going out'))
# print(show_task_list())