from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as messagebox
import tkinter.scrolledtext as scrolledtext
import sys
sys.path.append("..")
from indent.indent import proc_indent
from gene_sum.mysum import generate_sum
from gene_sum.parase_xml import get_words
from gene_sum.parase_xml import get_indexs

class Application(Frame):
    __colunme = 0
    __row = 0
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.FileButton = Button(self, text='选择UFC对象文件', command=self.SelectPath).grid(column=0, row=0)
        self.alertButton = Button(self, text='整理缩进', command=self.hello).grid(column=1, row=0)
        self.lb_black = Label(self, text = "字段：").grid(column=0, row=1)
        self.lb1 = Label(self, text = "源代码").grid(column=0, row=2)
        self.output = Text(self).grid(column=1, row=2)
        self.lb2 = Label(self, text = "整理后的代码").grid(column=0, row=3)
        self.output1 = Text(self).grid(column=1, row=3)

    def hello(self):
        text1 = self.output.get('1.0', END)
        text2 = proc_indent(text1.split('\n'))
        #messagebox.showinfo('Message', 'Hello,%s' % self.mypath)
        self.output1.insert(INSERT, text2)

    def SelectPath(self):
        self.mypath = askopenfilename()
        text1 = generate_sum(self.mypath)
        self.output.insert(INSERT, text1)
        self.ck_name_list = []
        self.ck_var_list = []

        #复选框
        check_list = get_indexs(self.mypath) 
        for i in range(len(check_list)):
            print('===%d ===%d' % (i%3, i/3) )
            self.ck_name_list.append('ck_name%d' % i)
            self.ck_var_list.append(0)
            self.ck_var_list[i] = StringVar()
            self.ck_name_list[i] = Checkbutton(self.lb1, text = check_list[i], variable = self.ck_var_list[i],
                onvalue = check_list[i], offvalue= '', 
                command = self.modf_cklist).grid(column = i, row = 1)

    def modf_cklist(self):
        for i in range(len(self.ck_var_list)):
            messagebox.showinfo('Message', 'Hello,%s' % self.ck_var_list[i].get())

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
#app.master.ou
# 主消息循环:
app.mainloop()