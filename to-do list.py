def Add():
    if (tasks2=="rem"):
        tasks.pop(int(input("enter the index")))
        for i in tasks:
            print(i)

    elif(tasks2=="N"):
        print("goodbye")
    else:
        new=[tasks2]
        tasks.extend(new)
        for i in tasks:
            print(i)
print("                                                    TO-DO LIST                                                     ")
tasks=["create a python code for calculator","Create a python code Rock,paper and scissor","complete your breakfast before noon","walk for 20 min daily at 4 pm"]
print(tasks[0])
print(tasks[1])
print(tasks[2])
print(tasks[3])
print("                                               ADDING     AND        REMOVING                                                     ")
print("if you wish to add tasks, please enter your tasks if not  enter N")
tasks2=input("enter the tasks")
Add()