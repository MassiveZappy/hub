# enum coins of bitcoin, ethereum, and litecoin
from tkinter import *
class coins:
    bitcoin = 0
    ethereum = 1
    testCoin = 2

def MinerBuddy(root):
    root.destroy()
    window = Tk()
    window.title("Miner Buddy")
    window.configure(background="white")
    window.iconbitmap("icon.ico")

    # GPUs listbox frame with 4 listboxs named Gpu Name, Price, Currency, PerSec
    gpuListboxFrame = Frame(window)
    gpuListbox = Listbox(gpuListboxFrame, height=4)
    priceListbox = Listbox(gpuListboxFrame, height=4)
    currencyListbox = Listbox(gpuListboxFrame, height=4)
    perSecListbox = Listbox(gpuListboxFrame, height=4)
    gpuListboxScrollbar = Scrollbar(gpuListboxFrame)

    def scrollbarMoved(*args):
        print("yscroll1" + str(args))
        print("e"+ str(gpuListboxScrollbar.set))
        gpuListbox.yview(*args)
        priceListbox.yview(*args)
        currencyListbox.yview(*args)
        perSecListbox.yview(*args)

    def listboxMoved(*args):
        print("yscroll2" + str(args))
        gpuListboxScrollbar.set(*args)
        gpuListbox.yview(MOVETO,args[0])
        priceListbox.yview(MOVETO,args[0])
        currencyListbox.yview(MOVETO,args[0])
        perSecListbox.yview(MOVETO,args[0])

    gpuListboxScrollbar.configure(command=scrollbarMoved)

    gpuListbox.configure(yscrollcommand=listboxMoved)
    priceListbox.configure(yscrollcommand=listboxMoved)
    currencyListbox.configure(yscrollcommand=gpuListboxScrollbar.set)
    perSecListbox.configure(yscrollcommand=gpuListboxScrollbar.set)

    # ADD GPUs TO LIST BOXES
    for i in range(40):
        gpuListbox.insert(END, "GPU Name" + str(i))
        priceListbox.insert(END, "Price"+ str(i))
        currencyListbox.insert(END, "Currency")
        perSecListbox.insert(END, "PerSec")

    # gid/render the window
    gpuListboxFrame.grid(row=0, column=0, sticky=N + S + E + W)
    gpuListbox.grid(row=1, column=1, sticky=N + S + E + W)
    priceListbox.grid(row=1, column=2, sticky=N + S + E + W)
    currencyListbox.grid(row=1, column=3, sticky=N + S + E + W)
    perSecListbox.grid(row=1, column=4, sticky=N + S + E + W)
    gpuListboxScrollbar.grid(row=1, column=5, sticky=N + S + E + W)
    window.mainloop()
    # MinerBuddy SelectedCurrencyVariable
    return window