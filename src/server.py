from fastapi import FastAPI, BackgroundTasks
from task import Task
from backend import main

app = FastAPI()

# タスクを追加
@app.post("/tasks")
def add_task(task: Task, background_tasks: BackgroundTasks):
    background_tasks.add_task(main, task=task)
    return "Add Task!"