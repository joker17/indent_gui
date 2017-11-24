from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as messagebox
import tkinter.scrolledtext as scrolledtext
import math
import sys
sys.path.append("..")
from indent.indent import proc_indent
from gene_sum.mysum import generate_sum
from gene_sum.parase_xml import get_words
from gene_sum.parase_xml import get_indexs

class Application(Frame):
    __column = 0
    __row = 0
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.FileButton = Button(self, text='1.选择UFC对象文件', command=self.SelectPath)
        self.FileButton.pack()
        self.lb00 = Label(self, text='2.选择索引')
        self.lb00.pack()
        self.lb0 = Label(self)
        self.lb0.pack()
        self.lb01 = Label(self, text = "3.选择要求和的字段")
        self.lb01.pack()
        self.lb1 = Label(self)
        self.lb1.pack()
        self.alertButton = Button(self, text='4.生成UFC求和代码', command=self.GeneCode)
        self.alertButton.pack()
        self.alertButton = Button(self, text='可选:整理缩进-对代码框处理', command=self.format_indent)
        self.alertButton.pack()
        self.lb2 = Label(self, text = "代码框:")
        self.lb2.pack()
        self.output = Text(self)
        self.output.pack()
        #self.lb2 = Label(self, text = "整理后的代码")
        #self.lb2.pack()
        #self.output1 = Text(self)
        #self.output1.pack()

    def format_indent(self):
        text1 = self.output.get('1.0', END)
        text2 = proc_indent(text1.split('\n'))
        #messagebox.showinfo('Message', 'Hello,%s' % self.mypath)
        self.output.delete(0.0, END)
        self.output.insert(INSERT, text2)

    def GeneCode(self):
        tmp_ckvaluse_list = []
        self.output.delete(0.0, END)
        #messagebox.showinfo('Message', 'Hello1111,%s' % self.combobox_var.get() )

        for i in range(len(self.ck_var_list)):
            if len(self.ck_var_list[i].get()) > 0:
                tmp_ckvaluse_list.append(self.ck_var_list[i].get())
        text1 = generate_sum(self.mypath, tmp_ckvaluse_list, self.combobox_var.get() )

        self.output.insert(INSERT, text1)

    def SelectPath(self):
        self.mypath = askopenfilename()
        self.ck_name_list = []
        self.ck_var_list = []

        #下拉框
        check_list = get_indexs(self.mypath) 
        self.combobox_var = StringVar()
        #self.index_listbox = Listbox(self.lb0, selectmode = MULTIPLE).grid(column=0,row=1)
        self.index_listbox = ttk.Combobox(self.lb0, 
            textvariable=self.combobox_var, state='readonly', width=100,
            values=check_list)
        self.index_listbox.grid(column=0, row=1)

        #复选框
        check_list = get_words(self.mypath) 
        for i in range(len(check_list)):
            __column = i%5+1
            __row = math.floor(i/5+2)
            print('===%d ===%d' % (__column, __row) )
            self.ck_name_list.append('ck_name%d' % i)
            self.ck_var_list.append(0)
            self.ck_var_list[i] = StringVar()
            self.ck_name_list[i] = Checkbutton(self.lb1, text = check_list[i], variable = self.ck_var_list[i],
                onvalue = check_list[i], offvalue= '', 
                command = self.modf_cklist).grid(column = __column, row = __row)
            #self.ck_name_list[i].pack()

    def modf_cklist(self):
        pass
        #for i in range(len(self.ck_var_list)):
        #    messagebox.showinfo('Message', 'Hello,%s' % self.ck_var_list[i])

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
#app.master.ou
# 主消息循环:
app.mainloop()