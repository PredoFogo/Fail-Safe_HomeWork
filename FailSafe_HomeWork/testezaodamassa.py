from tkinter import *

class teste:
    def __init__(self,master):
        self.master = master
        self.label = Label(self.master, text = '1').grid()
        self.new_window = teste2
        self.master.after(2000, self.chamanochesque)
        self.master.mainloop()

    def chamanochesque(self):
        root2 = Toplevel(self.master)
        self.master.destroy()
        pb = teste2(root2)




class teste2:
    def __init__(self, master):
        self.master = master
        self.label = Label(self.master, text='2').grid()
        self.master.mainloop()


def main():
    root = Tk()
    failsafemain = teste(root)
    root.mainloop()

main()