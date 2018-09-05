#!/usr/bin/env python
#coding=utf-8
import Tkinter as tk
import random
import sys
reload(sys)
sys.setdefaultencoding('utf8')
A = ['石头','剪刀','布']
B = random.choice(A)
window = tk.Tk(className='小游戏')
window.geometry('500x300')


def game():
	C = resultEntry.get()
	if C == B:
		confirmLabel.config(text="平局")
	elif C == '石头' and B == '剪刀':
		confirmLabel.config(text="你赢了")
	elif C == '剪刀' and B == '布':
		confirmLabel.config(text="你赢了")
	elif C == '布' and B == '石头':
		confirmLabel.config(text="你赢了")
	else:
		confirmLabel.config(text="你输了")

resultLabel = tk.Label(window, text="✊✂️布: ")
resultEntry = tk.Entry(window)
button = tk.Button(window, text="输入你的选择", command=game)
confirmLabel = tk.Label(window)

resultLabel.pack()
resultEntry.pack()
button.pack()
confirmLabel.pack()

window.mainloop()