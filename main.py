import json

class Task:
    def __init__(self):
        

class TaskManager:
    def __init__(self,task):

def selectMenu(selected):
    match selected:
        case 1:
            #add task
        case 2:
            #print task list
        case 3:
            #switch check
        case 4:
            #remove task
        case 5:
            #exit
        case _:
            print("1-5の数字で入力してください")

def printMenu():
    menu = """1. タスク追加
2. タスク一覧
3. 完了切り替え
4. タスク削除
5. 終了"""
    print(menu)
    select = input(">") -> int



printMenu()