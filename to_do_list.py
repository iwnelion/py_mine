tasks=[]

def displayTasks():
    print("To-Do List: ", tasks)

def addTask():
    numOfTasks=int(input("How many tasks do you want to add? "))
    for i in range(numOfTasks):
        task=input("Add task: ")
        tasks.append(task)
    displayTasks()

def removeTask():
    listLen=len(tasks)
    print("Which task do you want to remove? (1 -", listLen,")")
    rmTask=int(input())-1
    if rmTask<listLen:
        tasks.pop(rmTask)
        displayTasks()
    else:
        print("Invalid task number.")

def markTask():
    listLen=len(tasks)
    print("Which task do you want to mark as complete? (1 -", listLen,")")
    markComplete=int(input())-1
    if markComplete<listLen:
        tasks[markComplete]="[COMPLETE]"
        displayTasks()
    else:
        print("Invalid task number.")
    
def doAct():
    actionList=["add", "remove", "mark", "display", "exit"]
    action=str(input("What do you want to do? (add, remove, mark, display, exit): "))
    while action in actionList:
        if action.lower()=="add":
            addTask()
            doAct()
        elif action.lower()=="remove":
            removeTask()
            doAct()
        elif action.lower()=="mark":
            markTask()
            doAct()
        elif action.lower()=="display":
            displayTasks()
            doAct()
        elif action.lower()=="exit":
            print("Goodbye!")
            exit()
        else:
            print("Invalid action, try again")
            doAct()
        
doAct()
