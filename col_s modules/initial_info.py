'''
В этом модуле создается словари:
1) (цвет квадратов), (коордниата х, координата y, сторона, сторона)
2) разрешение экрана и сторона квадрата

This module creates dictionaries:
1) (COLOUR), (coordinate_x, coordinate_y, side, side)
2) screen resolution, side of a square
'''
# запуск GUI
# run GUI
import gui_initial_data as g
sd = g.window.sample_data

# разрешение экрана
# screen resolution
sd['res_x'] = int(sd['res_x'])
sd['res_y'] = int(sd['res_y'])

# размер квадрата
# square side
sd['dot_size'] = int(sd['dot_size'])

# основные цвета
# basic colurs
BLACK = (0,0,0)
WHITE = (200,200,200)
BLUE = (0,50,150)

# создаем список всех координат 'x'
# creating a list of all 'x' coordinates
x_coordinates = [i for i in range(
								  0,
								  sd['res_x'],
								  sd['dot_size']
								  )
				]

# создаем список всех координат 'y'
# creating a list of all 'y' coordinates
y_coordinates = [i for i in range(
								  0,
								  sd['res_y'],
								  sd['dot_size']
								  )
				]

# создаем список вложенных кортежей координат ('x','y')
# creating a list of tuples of coordinates ('x', 'y')
square_coordinates = []
for x in x_coordinates:
	l = [(x,y) for y in y_coordinates]
	square_coordinates.extend(l)

# переводим список в словарь (номер : ЦВЕТ, ('x','y'))
# turnig a list in a dictionary (number : COLOUR, ('x','y'))
d_square_coordinates = {}
for i in range(0,len(square_coordinates)):
	d_square_coordinates[i] = [
				BLUE, 
				(
				square_coordinates[i][0],
				square_coordinates[i][1],
				sd['dot_size'], sd['dot_size']
				)
			]


vertical_lines = [
				  ((i,0), (i,sd['res_y'])) for i in range(
													 sd['dot_size'],
													 sd['res_x'],
													 sd['dot_size']
													 )
				  ]

horizontal_lines = [
					((0,i),(sd['res_x'],i)) for i in range(
													 sd['dot_size'],
													 sd['res_y'],
													 sd['dot_size'])
					]


print(sd)
