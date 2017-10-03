from tkinter import *
import tkinter.messagebox as messagebox
import tkinter.scrolledtext as scrolledtext
import sys
sys.path.append("..")
from indent.indent import proc_indent

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #self.nameInput1 = Entry(self)
        #self.nameInput1.pack()
        self.alertButton = Button(self, text='整理缩进', command=self.hello)
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
        text1 = self.output.get('1.0', END)
        text2 = proc_indent(text1.split('\n'))
        #messagebox.showinfo('Message', 'Hello,%s' % name1)
        self.output1.insert(INSERT, text2)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
#app.master.ou
# 主消息循环:
app.mainloop()