# importing modules
# импортруем модули
from tkinter import *
from tkinter.ttk import Combobox

import sys
import os
import json

class GUI_COLS(Frame):
	def __init__(self):
		super().__init__()
		self.widgets()

	def widgets(self):
		'''function places widgets on window'''

# выбор настроек\settigs choice
# Лейба\Label
		lbl_settings = Label()
		lbl_settings['text'] = 'Задайте настройки (по умолчанию basic)'
		lbl_settings.place(x=0,
							y=0)
# комбобокс\combobox
		os.chdir('..')
		os.chdir('settings')
		self.settings = os.listdir()
		self.cbox_settings = Combobox(values= os.listdir())
		self.cbox_settings.place(
								x=250,
								y=0)
		self.cbox_settings.current(0)	


# выбор шаблона\sample choice 
# лейба\label
		lbl_sample = Label()
		lbl_sample['text'] = 'Выберите шаблон предъявления точек'
		lbl_sample.place(
						x=0,
						y=30,
						)
# комбобокс\combobox
		os.chdir('..')
		os.chdir('samples')
		self.cbox_samples = Combobox(values= os.listdir())
		self.cbox_samples.place(
								x=250,
								y=30)
		self.cbox_samples.bind('<<ComboboxSelected>>',self.sample_description)

# описание шаблона\sample description
# лейба\label
		lbl_description = Label()
		lbl_description.place(relx=0.5,
							  y=60,
							  anchor=N)
		lbl_description['text'] = 'Описание шаблона'
# текстовое поле описания\text field with description
		self.description = Text()
		self.description.place(x=30,
						  y=90,
						  relwidth=0.85,
						  relheight=0.5)


	def sample_description(self,event):
		print(self.cbox_samples.get())
		with open(self.cbox_samples.get(), 'r') as read_file:
			self.data = json.load(read_file)
			self.description.delete(1.0, END)
			self.description.insert(1.0, self.data['description'])




root = Tk()
root.geometry('398x470')
root.title('Col_s start')

new = GUI_COLS()

root.mainloop()