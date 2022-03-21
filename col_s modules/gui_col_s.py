

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
		lbl_settings['text'] = (
			'Задайте настройки'+'\n(по умолчанию basic)')
		lbl_settings.place(x=0,
							y=0)
# комбобокс\combobox
		os.chdir('..')
		os.chdir('settings')
		self.settings = os.listdir()
		self.cbox_settings = Combobox(values= os.listdir())
		self.cbox_settings.place(
								x=220,
								y=0)
		self.cbox_settings.current(0)	


# выбор шаблона\sample choice 
# лейба\label
		os.chdir('..')
		os.chdir('samples')
		self.lbl_sample = Label()
		self.lbl_sample['text'] = (
			'Выберите шаблон'+'\nпредъявления точек'
								)
		self.lbl_sample.place(
						x=0,
						y=40,
						)
# комбобокс\combobox
		self.cbox_samples = Combobox(values= os.listdir())
		self.cbox_samples.place(
								x=220,
								y=40)
		self.cbox_samples.bind('<<ComboboxSelected>>',
								self.preview_decription)


# описание шаблона\sample description
# лейба\label
		lbl_description = Label()
		lbl_description.place(x=160,
							  y=80,
							  )
		lbl_description['text'] = 'Описание шаблона'
# текстовое поле описания\text field with description
		self.description = Text(
								wrap=WORD,
								borderwidth = 3,
         						relief="sunken"
         						)
		self.description.place(x=30,
							  y=100,
							  width=400,
							  height=150)
# превьюшка шаблона
# sample preview
		lbl_preview = Label()
		lbl_preview.place(
							x=30,
							y=250)
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
														y=250)
		self.r_bttn_linear = Radiobutton(
								self,
								text= 'экспоненциальный',
								variable=self.mode,
								value='экспоненциальный')
		self.r_bttn_linear.place(
							x=250,
							y=295
							)

		self.r_bttn_imp = Radiobutton(
								self,
								text= 'импульсный',
								variable=self.mode,
								value='импульсный')
		self.r_bttn_imp.place(
								x=250,
								y=315
							)


# рамка для ввода информации о пользователе
		self.name_frame = Frame(
							self,
							borderwidth = 3,
         					relief="sunken"
         					)
		self.name_frame.place(
								x=435,
								y=0,
								width=280,
								height=383
								)
# лейба: имя файла
		self.lbl_file_name= Label(
									self.name_frame,
									text='Имя файла(желательно латиницей)'
									)
		self.lbl_file_name.place(
								x=0,
								y=0)
# поле для ввода имени файла
		self.file_name = Entry(
									self.name_frame,
									)
		self.file_name.place(
								x=0,
								y=30,
								relwidth=1
								)

# лейба: поле для ввода имени испытуемого
		Label(
			self.name_frame,
			text='ФИО испытуемого'
			).place(
					x=0,
					y=60)
# поле для ввода имени испытуемого
		self.patient_name = Entry(
									self.name_frame,
									)
		self.patient_name.place(
								x=0,
								y=90,
								relwidth=1
								)

# лейба: поле для описания эксперимента
		Label(
			self.name_frame,
			text='Описание эксперимента'
			).place(
					x=0,
					y=120)
# Текстовое поле для ввода описания эксперимента
		self.exp_description = Text(
								self.name_frame,
								borderwidth=3,
								relief='ridge',
								wrap=WORD
									)
		self.exp_description.place(
									x=0,
									y=150,
									relwidth=1,
									height=220
									)




# инициализация кнопки 
		start_button = Button(
								root,
								text='start',
								command=self.start
								).place( 
										relx=0.5,
										y=400)


# блок функций которые выполняются окном

# функции превьюшки
	def preview_decription(self,event):
		os.chdir('..')
		os.chdir('samples')
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
		self.description.insert(2.0, "автор шаблона: " + 
						data['author_name'] +
						"\nописание: "+ data['description']+
						'\nсоздан под разрешение экрана: '+
						str(data['res_x'])+'x'+str(data['res_y']))
	
# работа кнопки start
	def start(self):
		schk = self.check_sample()
		if schk:
			nchk = self.check_name()
		else:
			nchk = False


		if nchk and schk:
			self.settings_download()
			self.data['sample'] = self.cbox_samples.get()
			self.data['mode'] = self.mode.get()
			self.data['patient_name'] = self.patient_name.get()
			self.data['exp_description'] = self.exp_description.get(1.0,END)
			for i in self.data:
				print(i,':',self.data[i])
			root.quit()

	def check_name(
				self
					):
		name = self.file_name.get()
		name = str(name) +'.json'
		os.chdir('..')
		os.chdir('results')
		files = os.listdir()
		if name == '.json':
			self.lbl_file_name['text'] = 'Задайте имя!'				
			self.lbl_file_name['bg'] = 'red'
			return False
		elif name in files:
			self.lbl_file_name['text'] = 'Имя файла занято'			
			self.lbl_file_name['bg'] = 'red'
			return False
		else:
			self.data['file_name'] = name
			return True

	def check_sample(
					self
					):
		if self.cbox_samples.get() == '':
			self.lbl_sample['bg'] = 'red'
			return False
		else:
			self.lbl_sample['bg'] = 'white'			
			return True

	def settings_download(
						self
							):
		os.chdir('..')
		os.chdir('settings')
		with open(self.cbox_settings.get(), 'r') as settings_file:
			self.data['settings'] = json.load(settings_file)




root = Tk()
root.geometry('800x470')
root.title('Col_s start')

new = GUI_COLS(root)
root.mainloop()