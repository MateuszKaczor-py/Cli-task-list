# Task Tracker CLI

A small command-line task manager. Tasks are stored as JSON in `tasks_data.json` next to the script.

## Requirements

- Python 3.8+
- No external dependencies (uses only the standard library: `json`, `argparse`, `time`).

## Usage

```bash
python main.py <command> [arguments]
```

### Commands

| Command | Arguments | Description |
|---|---|---|
| `add_task` | `<description>` | Add a new task. Created with status `Not Done`. |
| `delete_task` | `<id>` | Delete a task by ID. Remaining tasks are renumbered to stay sequential. |
| `update_task` | `<id> <description>` | Update an existing task's description. |
| `change_status` | `<id> <status>` | Change a task's status. Status must be one of `done`, `in_progress`, `not_done`. |
| `show_task_list` | `<filter>` | List tasks. Filter must be one of `all`, `done`, `not_done`, `in_progress`. |

### Examples

```bash
python main.py add_task "Buy milk"
python main.py add_task "Write report"
python main.py change_status 1 done
python main.py update_task 2 "Write quarterly report"
python main.py show_task_list all
python main.py show_task_list not_done
python main.py delete_task 1
```

## Data file

Tasks are stored in `tasks_data.json` in the current working directory. The file is created automatically on the first `add_task`. Each entry looks like:

```json
{
    "1": {
        "description": "Buy milk",
        "status": "Not Done",
        "created_at": "Wed Apr 22 14:30:00 2026",
        "updated_at": "Wed Apr 22 14:30:00 2026"
    }
}
```

### Note on IDs

Deleting a task triggers a re-index — remaining tasks are renumbered to keep IDs contiguous (1, 2, 3, ...). This means a task's ID can change after a deletion elsewhere in the list.

## project URL:
https://roadmap.sh/projects/task-tracker