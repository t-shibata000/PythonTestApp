import time
from task import Task
import pandas as pd
import datetime

path = r".\log.csv"

# 現在時刻を取得
def get_now():
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))) 
    return str(now.strftime("%Y/%m/%d/%H:%M:%S"))

# タスクをcsvに追加 (本来はDB処理で行うべき)
def add_task(task: Task):
    df = pd.read_csv(path)
    task.set_id(len(df))
    task.set_start_time(get_now())
    df = df.append(dict(task), ignore_index=True)
    df.to_csv(path, index=False)

# タスクを更新 (本来はDB処理で行うべき)
def update_task(task: Task):
    df = pd.read_csv(path)
    task.set_end_time(get_now())
    df.loc[task.id, "end_time"] = task.end_time
    df.to_csv(path, index=False)

# タスクログを取得
def get_log():
    df = pd.read_csv(path, index_col="id")
    return df

# 重い処理を行う関数
def main(task: Task):
    add_task(task)
    time.sleep(task.time)
    update_task(task)

if __name__=="__main__":
    task = Task(id=0,title="test",time=0,start_time="",end_time="")
    add_task(task)
    main(task)