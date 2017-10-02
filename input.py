from tkinter import *
import tkinter.messagebox as messagebox
import tkinter.scrolledtext as scrolledtext

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #self.nameInput1 = Entry(self)
        #self.nameInput1.pack()
        self.alertButton = Button(self, text='Hello tst', command=self.hello)
        self.alertButton.pack()
        self.lb1 = Label(self, text = "请输入源代码")
        self.lb1.pack()
        self.output = Text(self)
        self.output.pack()
        self.lb2 = Label(self, text = "整理后的代码")
        self.lb2.pack()
        self.output1 = Text(self)
        self.output1.pack()

    def hello(self):
        name = self.nameInput1.get() 
        name1 = self.output1.get('1.0', END) or "world"
        messagebox.showinfo('Message', 'Hello,%s' % name1)
        self.output.insert(INSERT, name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
#app.master.ou
# 主消息循环:
app.mainloop()