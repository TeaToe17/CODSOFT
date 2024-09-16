import tkinter as tk
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x550+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        updateTaskFile()
        listbox.delete(ANCHOR)

def updateTaskFile():
    with open("tasklist.txt", "w") as taskfile:
        for task in task_list:
            taskfile.write(task + "\n")

def OpenTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

            for task in tasks:
                if task != "\n":
                    task_list.append(task.strip())
                    listbox.insert(END, task.strip())
    except:
        file = open("tasklist.txt", "w")
        file.close()

def updateTask():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        print(selected_task_index)
        new_task = task_entry.get()
        if new_task:
            task_list[selected_task_index[0]] = new_task

            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, new_task)

            task_entry.delete(0, END)
            updateTaskFile()

heading = Label(root, text="ALL TASKS", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=100)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=25, y=7)
task_entry.focus()

add_button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
add_button.place(x=300, y=0)

update_button = Button(frame, text="UPDATE", font="arial 20 bold", width=10, bg="#5a95ff", fg="#fff", bd=0, command=updateTask)
update_button.place(x=140, y=0)

# List
frame1 = Frame(root, bd=3, width=700, height=200, bg="#32405b")
frame1.place(x=10, y=160)

listbox = Listbox(frame1, font=("arial", 12), width=40, height=16, bg="#32405b")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Delete
# Delete_icon = PhotoImage(file="delete.png", width=100, height=100)
Button(root, bd=0,bg="red",fg="white",text="Delete",command=deleteTask).pack(side=BOTTOM, pady=15)

OpenTaskFile()
root.mainloop()