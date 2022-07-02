from tkinter import *
def readTodo():
    try:
        with open('todo.txt', 'r') as f:
            todo = f.readlines()
    except FileNotFoundError:
        todo = []
    return todo
def writeTodo(todo):
    with open('todo.txt', 'w') as f:
        f.writelines(todo)
def addTodo(todo, task, todoListbox, todoTextbox):
    todo.append(task)
    writeTodo(todo)
    todoListbox.delete(0,END)
    for item in todo:
        todoListbox.insert(END, item)
    todoTextbox.delete(0, END)
def removeTodo(todo, task, todoListbox):
    todo.remove(task)
    writeTodo(todo)
    todoListbox.delete(0,END)
    for item in todo:
        todoListbox.insert(END, item)