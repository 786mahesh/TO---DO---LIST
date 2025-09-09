## TO-Do-List(task base)
import datetime as dt
print("\t\t\t\tTO - DO - LIST")
task_number =0
while True :
    print("1)Add Task")
    print("2)view Task")
    print("3)Delete Task")
    print("4)Quit")
    task_perform = int(input("Enter you want perform task : - "))
    if task_perform == 1:
        try:
            file = open("task.txt","a")
            date = dt.datetime.now()
            task_title = input("Enter What your task title  :")
            task_about = input("write your task : ")
            task =f"{task_number}.{date} | {task_title} |{task_about}\n" 
            file.write(task)
            print("Task added Sucessfully.!!!")
            task_number += 1
            file.close()
        except FileNotFoundError:
            print("File is not found")
    elif task_perform == 2:
        try:
            file = open("task.txt","r")
            task = file.readlines()
            if task:
                for task in task:
                    print(task.strip())
            else :
                print("Not found the task")
                file.close()
        except FileNotFoundError:
            print("File is not found")
    elif task_perform == 3:
        try:
            with open("task.txt", 'r') as file:
                tasks = file.readlines()

            if not tasks:
                print("Task not found")
            else:
                print("\n--- Your Tasks ---")
                for task in tasks:
                    print(task.strip())

                delete_task = input("Enter task number to delete: ")

                with open("task.txt", "w") as file:
                    for t in tasks:
                        if not t.startswith(delete_task + "."):
                            file.write(t)

                print("✅ Successfully deleted task!")

        except FileNotFoundError:
            print("File is not found")

    elif task_perform  == 4:
        print("Have good day , byy")
        break
    else :
        print("You chose incorrect option ,please chose correct option")
        
