

coords = [(1,2),(2,4)]



# importing modules
# импортруем модули
from tkinter import *
from tkinter.ttk import Combobox

import sys
import os
import json


class GUI_COLS(Frame):
	def __init__(self,master):
		super().__init__(master,)
		self.place(
					x=0,
					y=0,
					relwidth=1,
					relheight=1
					)
		self.mode = StringVar()
		self.mode.set('импульсный')
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
		self.cbox_samples.bind('<<ComboboxSelected>>',
								self.preview_decription)

# описание шаблона\sample description
# лейба\label
		lbl_description = Label()
		lbl_description.place(relx=0.5,
							  y=60,
							  anchor=N)
		lbl_description['text'] = 'Описание шаблона'
# текстовое поле описания\text field with description
		self.description = Text(wrap=WORD)
		self.description.place(x=30,
						  y=90,
						  relwidth=0.85,
						  relheight=0.3)
# превьюшка шаблона
# sample preview
		lbl_preview = Label()
		lbl_preview.place(
							x=30,
							y=240)
		lbl_preview['text'] = 'превью шаблона'

		self.preview_spot = Frame(
								self,
								borderwidth = 3,
         						relief="sunken")
		self.preview_spot.place(
							x=30,
							y=280,
							width=192,
							height=108
						   )


# выбор режима нарастания яркости
		Label(
			root,
			text='режим нарастания'+'\nяркости').place(
														x=250,
														y=240)
		r_bttn_linear = Radiobutton(
								self,
								text= 'экспоненциальный',
								variable=self.mode,
								value='экспоненциальный').place(
																x=250,
																y=275)

		r_bttn_imp = Radiobutton(
								self,
								text= 'импульсный',
								variable=self.mode,
								value='импульсный').place(
														x=250,
														y=295)

# инициализация кнопки
		start_button = Button(
								root,
								text='start'
								).place( 
										relx=0.5,
										y=400)


# блок функций которые выполняются окном



	def preview_decription(self,event):
		with open(self.cbox_samples.get(), 'r') as read_file:
			self.data = json.load(read_file)
		self.preview(self.data)
		self.sample_description(self.data)

	def preview(self,data):

		for i in self.preview_spot.place_slaves():
			i.destroy()

		preview = Frame(self.preview_spot,bg='black')
		preview.place(
					relx=0.5,
					rely=0.5,
					anchor=CENTER,
					width=data['res_x']/10,
					height=data['res_y']/10
					)

		size = data['dot_size']







		for i in data['dot_coordinates'].values():
			i = Label(preview).place(
									x=i[0]/10,
									y=i[1]/10,
									width=size/10,
									height=size/10
									)
	def sample_description(self,data):
		'''Shows a description of a sample
		выводит на текстовое поле описание шаблона'''
		self.description.delete(1.0, END)
		self.description.insert(2.0, "автор шаблона: " + data['author_name'] +
	"\nописание: "+ data['description']+
	'\nсоздан под разрешение экрана: '+str(data['res_x'])+'x'+str(data['res_y']))
								

root = Tk()
root.geometry('398x470')
root.title('Col_s start')

new = GUI_COLS(root)
root.mainloop()