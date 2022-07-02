import webbrowser
from tkinter import *
import MinerBuddy
import mic
import todo

def renderHomeWindow(*root):
    print(root)
    if root != ():
        root[0].destroy()
    root = Tk()
    root.title("Home")
    homeButton = Button(root, text="Home", command=lambda: renderHomeWindow(root))
    homeButton.pack()
    todoButton = Button(root, text="Todo", command=lambda: renderTodoWindow(root))
    todoButton.pack()
    bookCalculatorButton = Button(root, text="Book Calculator", command=lambda: renderBookCalculatorWindow(root))
    # disable the bookCalculatorButton
    bookCalculatorButton.configure(state=DISABLED)
    bookCalculatorButton.pack()
    aboutButton = Button(root, text="About", command=lambda: renderAboutWindow(root))
    aboutButton.pack()
    root.iconbitmap("icon.ico")
    root.mainloop()
def renderTodoWindow(root):
    root.destroy()
    window = Tk()
    window.iconbitmap("icon.ico")
    window.title("Todo")
    window.configure(background="white")
    window.iconbitmap("icon.ico")
    # create a list of todo items
    todoList = todo.readTodo()
    # create a listbox to display the todo items
    todoListboxFrame = Frame(window)
    todoListbox = Listbox(todoListboxFrame)
    # create a scrollbar to scroll the todo items
    todoScrollbar = Scrollbar(todoListboxFrame)
    todoScrollbarX = Scrollbar(todoListboxFrame, orient=HORIZONTAL)
    # link the scrollbar to the listbox
    todoListbox.configure(yscrollcommand=todoScrollbar.set)
    todoScrollbar.configure(command=todoListbox.yview)
    # add the todo items to the listbox
    for item in todoList:
        todoListbox.insert(END, item)

    todoListbox.grid(row=0, column=0, sticky=N+S+E+W)
    todoListboxFrame.grid(row=1, column=1, sticky=N+S+E+W)
    todoScrollbar.grid(row=0, column=1, rowspan=2, sticky=N+S+E+W)
    todoScrollbarX.grid(row=1, column=0, sticky=N+S+E+W)

    todoListbox.configure(xscrollcommand=todoScrollbarX.set)
    todoScrollbarX.configure(command=todoListbox.xview)
    # create a textbox to add a new todo item
    todoTextbox = Entry(window, width=24)
    # create a button to add a new todo item
    todoButton = Button(window, text="Add", command=lambda: todo.addTodo(todoList, todoTextbox.get(), todoListbox, todoTextbox))
    # add the textbox and button to the window
    todoTextbox.grid(row=2, column=1, sticky=N+S+E+W)
    todoButton.grid(row=1, column=2, sticky=N+S+E+W)
    # create a button to remove a todo item
    todoRemoveButton = Button(window, text="Remove", command=lambda: todo.removeTodo(todoList, todoListbox.get(ACTIVE), todoListbox))
    # add the button to the window
    todoRemoveButton.grid(row=2, column=2, sticky=N+S+E+W)
    # home button
    homeButton = Button(window, text="Home", command=lambda: renderHomeWindow(window))
    homeButton.grid(row=0, column=1, columnspan=2, sticky=N + S + E + W)
    window.mainloop()
def renderBookCalculatorWindow(root):
    root.destroy()
    window = Tk()
    window.title("Book Calculator")
    window.configure(background="white")
    window.iconbitmap("icon.ico")
    window.mainloop()
    return window
def renderAboutWindow(root):
    root.destroy()
    window = Tk()
    window.iconbitmap("icon.ico")
    window.title("About")
    # make a header named "About"
    aboutHeader = Label(window, text="About", font=("Ubuntu", 16))
    aboutHeader.grid(row=0, column=0, sticky=N+S+E+W)

    # make a label with the name of the author and a button to add a web browser to open the author's website
    authorLabel = Label(window, text="By: MassiveZappy", font=("Ubuntu", 16))
    authorLabel.grid(row=1, column=0, sticky=N+S+E+W)
    authorButton = Button(window, text="Visit Author's Website", command=lambda: webbrowser.open("https://github.com/MassiveZappy/"))
    authorButton.grid(row=2, column=0, sticky=N+S+E+W)
    # show the link incase it didn't open
    authorLabel2 = Label(window, text="If it didn't open, visit this url https://github.com/MassiveZappy/.", font=("Ubuntu", 8))
    authorLabel2.grid(row=3, column=0, sticky=N+S+E+W)
    aboutLabel = Label(window, text=mic.aboutTxt(),font=("Ubuntu", 12))
    aboutLabel.grid(row=4, column=0, sticky=N+S+E+W)
    window.configure(background="white")
    window.iconbitmap("icon.ico")
    #return Home
    homeButton = Button(window, text="Home", command=lambda: renderHomeWindow(window))
    homeButton.grid(row=5, column=0, sticky=N+S+E+W)
    window.mainloop()
    return window
def renderMinerBuddyWindow(root):
    MinerBuddy.MinerBuddy(root)