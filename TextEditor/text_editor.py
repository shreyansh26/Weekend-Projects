from tkinter import *
import tkinter.filedialog as tk
import tkinter.messagebox as tk2

class Editor(Frame, object):

	def __init__(self, master):
		super(Editor, self).__init__(master)
		self.create_widgets()

	def create_widgets(self):
		self.text1 = Text(width=20, height=20, undo=True)
		self.text1.pack(expand=YES, fill=BOTH)

		menubar = Menu(self)
		filemenu = Menu(menubar)
		editmenu = Menu(menubar)
		toolsmenu = Menu(menubar)

		filemenu.add_command(label='New', command=self.newDoc)
		filemenu.add_command(label='Save', command=self.saveDoc)
		filemenu.add_command(label='Open', command=self.openDoc)

		editmenu.add_command(label='Copy', command=self.copy)
		editmenu.add_command(label='Paste', command=self.paste)
		editmenu.add_command(label='Cut', command=self.cut)
		editmenu.add_command(label='Clear', command=self.clear)

		toolsmenu.add_command(label = 'Word Count', command = self.wordCount)

		menubar.add_cascade(label='File', menu=filemenu)
		menubar.add_cascade(label='Edit', menu=editmenu)
		menubar.add_cascade(label='Tools', menu=toolsmenu)

		## Key Bindings
		root.bind('<Control-s>', self.saveDoc2)
		root.bind('<Control-o>', self.openDoc2)
		root.bind('<Control-a>', self.select_all)
		root.bind('<Control-c>', self.copy2)
		root.bind('<Control-v>', self.paste2)
		root.bind('<Control-x>', self.cut2)

		root.config(menu=menubar)

	def newDoc(self):
		if(tk2.askyesno("Message", "Unsaved work will be lost. Continue?")):
			self.text1.delete("1.0", END)

	def saveDoc(self):
		savefile = tk.asksaveasfile(mode='w', defaultextension='.txt')
		text2save = str(self.text1.get("1.0", END))
		savefile.write(text2save)
		savefile.close()

	def saveDoc2(self, event):
		self.saveDoc()

	def openDoc(self):
		openfile = tk.askopenfile(mode='r')
		text = openfile.read()
		self.text1.insert(END, text)
		openfile.close()

	def openDoc2(self, event):
		self.openDoc()

	def copy(self):
		#Copy the selected text
		copy_text = str(self.text1.get(SEL_FIRST, SEL_LAST))
		self.clipboard_clear()
		self.clipboard_append(copy_text)

	def copy2(self, event):
		self.copy()

	def cut(self):
		self.copy()
		self.delete("sel.first", "sel.last")

	def cut2(self, event):
		self.cut()

	def paste(self):
		# Insert clipboard into textbox
		result = self.selection_get(selection="CLIPBOARD")
		self.text1.insert(INSERT, result)

	def paste2(self, event):
		# Insert clipboard into textbox
		result = self.selection_get(selection="CLIPBOARD")
		result = str(result).split()
		result = result[:len(result)/2]
		result = ''.join(result)
		self.text1.insert(INSERT, result)

	def clear(self):
		self.text1.delete("1.0", END)

	def wordCount(self):
	    #Get text from textbox and split it by whitespace characters into a list. Then find length of list
	    userText = self.text1.get("1.0", END)
	    wordList = userText.split()
	    number_of_words = len(wordList)
	    tk2.showinfo('Word Count', 'Words:  ' + str(number_of_words))

	def select_all(self, event):
	    self.text1.tag_add(SEL, "1.0", END)
	    self.text1.mark_set(INSERT, "1.0")
	    self.text1.see(INSERT)
	    return 'break'


root = Tk()
root.title("Text Editor")
root.geometry('700x600')
editor = Editor(root)
editor.mainloop()