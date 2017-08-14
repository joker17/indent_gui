from tkinter import *
import tkinter.messagebox as messagebox
import tkinter.scrolledtext as scrolledtext

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput1 = Entry(self)
        self.nameInput1.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
        self.output = Text(self)
        self.output.pack()

    def hello(self):
        name = self.nameInput1.get() or 'world'
        messagebox.showinfo('Message', 'Hello,%s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
#app.master.ou
# 主消息循环:
app.mainloop()