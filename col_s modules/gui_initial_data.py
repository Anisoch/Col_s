from tkinter import *
import os

class info(Frame):
	def __init__(self, master):
		super().__init__(master)
		self.wigets_place()


	def wigets_place(self):

# лейба для ввода имени
		self.lbl_1 = Label()
		self.lbl_1.grid(row=0,
					column=0,
					columnspan=2,
					sticky=W,
					)
		self.lbl_1['text'] = 'Задайте имя нового шаблона'
# поле ввода для имени шаблона
		self.entr_1 = Entry(width=40)
		# entr_1.place(x = 200, y = 0,
		# 			 width = 400, height = 30,
		# 			 anchor = NW)
		self.entr_1.grid(row=0,
					column=2,
					columnspan=2,
					sticky=W)


# лейба для имени автора	
		lbl_2 = Label()
		# lbl_2.place(relx = 0.5 , y = 30,
		# 			 width = 400, height = 30,
		# 			 anchor = N)
		lbl_2.grid(row=1,
					column=0,
					columnspan=2,
					sticky=W)
		lbl_2['text'] = 'ФИО автора'	
# поле ввода для имени автора
		self.entr_2 = Entry(width=40)
		# entr_1.place(x = 200, y = 0,
		# 			 width = 400, height = 30,
		# 			 anchor = NW)
		self.entr_2.grid(row=1,
					column=2,
					columnspan=2,
					sticky=W)


# лейба разрешение по X
		lbl_3 = Label()
		lbl_3.grid(row=2,
					column=0,
					sticky=W)
		lbl_3['text'] = 'Разрешение по X, px'
# поле ввода разрешения по X
		self.entr_3 = Entry()
		self.entr_3.grid(row=2,
			column=1)


# лейба разрешение по Y
		lbl_4 = Label()
		lbl_4.grid(row=2,
					column=2,
					sticky=W)
		lbl_4['text'] = 'Разрешение по Y, px'
# поле ввода разрешения по Y
		self.entr_4 = Entry()
		self.entr_4.grid(row=2,
				column=3,
				sticky=W)


# лейба размер квадрата
		lbl_5 = Label(text="сторона квадрата, px")
		lbl_5.grid(row=3,
					column=0,
					sticky=W)
# поле ввода сторона квадрата
		self.entr_5 = Entry()
		self.entr_5.grid(row=3,
						column=1,
						sticky=W)

# лейба расшифровка px
		lbl_7 = Label()
		lbl_7.grid(row=3,
				column=3,
				sticky=W)
		lbl_7['text'] = 'px - пиксели'

#лейба для описания
		lbl_6 = Label()
		# lbl_2.place(relx = 0.5 , y = 30,
		# 			 width = 400, height = 30,
		# 			 anchor = N)
		lbl_6.grid(row=4,
					column=1,
					columnspan=2)
		lbl_6['text'] = 'Кратко опишите свой шаблон'


# текстовое поле для описания
		self.t_field = Text(wrap=WORD)
		self.t_field.place(x = 10, y = 115,
					width = 450, height = 150)
		# self.t_field.grid(row=5,
		# 					padx=10,
		# 					ipadx=10,
		# 					pady=10,
		# 					ipady=10,
		# 					sticky=W)

# кнопка генерировать
		bttn_g = Button()
		bttn_g['text'] = 'приступить'
		bttn_g['command'] = self.generate
		bttn_g.place(relx=0.5,rely=0.8,
					anchor=CENTER)

	def generate(self):
		name = self.entr_1.get()
		self.check_name(name)

	def check_name(self,
					name):
		name = str(name) +'.json'
		os.chdir('..')
		os.chdir('samples')
		files = os.listdir()
		if name not in files:
			self.sample_name = name
			self.data_dict()
			root.quit()
		else:
			self.lbl_1['text'] = 'Имя шаблона занято\t  '
			self.lbl_1['bg'] = 'red'

	def data_dict(self):
		self.sample_data = {
		'sample_name' : self.sample_name,
		'author_name' : self.entr_2.get(),
		'res_x'		  : self.entr_3.get(),
		'res_y'		  : self.entr_4.get(),
		'dot_size'    : self.entr_5.get(),
		'description' : self.t_field.get(1.0,END)
		}
		# print(self.samle_data)

root = Tk()
root.geometry('500x400')
root.title('генератор шаблонов для Col_S')

window = info(root)
root.mainloop()


