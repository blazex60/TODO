import json

class Task:
    def __init__(self):
        with open("/data/tasks.json", "r+w") as r:
           load_json = json.loads(r)
           if (len(load_json) == 0):
                json.dumps(task_list,f,indent=2)

    def write(self,task):
        task_list = {"task":task,"status":False}
        tasks = self.read()
        

    def read(self):
        with open("/data/task.json","r") as f:
            taskList = json.loads(f)
            return taskList

class TaskManager:
    def __init__(self):
        print("init")
    def add(self,tasks):
        if (len(tasks) == 0):
            print("error:タスクを入力してください")
        else:
            Task.write(tasks)


def selectMenu(selected):
    match selected:
        case 1:
            tasks = input("追加したいタスクを入力してください(Tip:コンマで区切れば複数追加できます)")
            tm = TaskManager
            tm.add(tasks)
        case 2:
            #print task list
            print(2)
        case 3:
            #switch check
            print(3)
        case 4:
            #remove task
            print(4)
        case 5:
            #exit
            print("タスクを終了します")
        case _:
            print("1-5の数字で入力してください")

def printMenu():
    menu = """1. タスク追加
2. タスク一覧
3. 完了切り替え
4. タスク削除
5. 終了"""
    print(menu)
    select = int(input(">"))
    return select



selectMenu(printMenu()) 