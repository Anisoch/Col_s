
import os
import sys
os.chdir('col_s modules')
sys.path.append(os.getcwd())

from initial_info import d_square_coordinates as dsc
from initial_info import vertical_lines
from initial_info import horizontal_lines

import pygame as pg
import json as j

# словарь с данными о шаблоне
from initial_info import sd

# создаем исходный список, в который будут записываться координаты
# creating a list of coordinates to be sent to next programm
list_of_coordinates = []

# устанавливаем ширину и высоту окна
# setting a width and height of the window
res_x = sd['res_x']
res_y = sd['res_y']

# основные цвета
# basic colours
BLACK = (0,0,0)
WHITE = (100,100,100)
BLUE = (0,50,150)
RED = (200,50,50)

# устанавливаем ФПС
# setting FPS
FPS = 60

# запускаем pygame
# run pygame
pg.init()
screen = pg.display.set_mode((res_x, res_y))
pg.display.set_caption("name")
clock = pg.time.Clock()

side = sd['dot_size']

running = True
while running:
	screen.fill(BLACK)

	for i in dsc:
		pg.draw.rect(
					 screen,
					 dsc[i][0],
					 dsc[i][1])
	for i in vertical_lines:
		pg.draw.line(screen,WHITE,i[0],i[1])
	for b in horizontal_lines:
		pg.draw.line(screen,WHITE,b[0],b[1])
# отрисовка линий для позиционирования
# линии по центру
		pg.draw.line(screen,RED,((res_x/2),0),(res_x/2,res_y),3)
		pg.draw.line(screen,RED,(0,(res_y/2)), ((res_x),(res_y/2)),3)
# вертикальные линии по четвертям
		pg.draw.line(screen,RED,((res_x/4),0),(res_x/4,res_y),1)
		pg.draw.line(screen,RED,((res_x/4 * 3),0),(res_x/4 *3,res_y),1)	
# горизонтальные линии по четвертям		
		pg.draw.line(screen,RED,(0,(res_y/4)), ((res_x),(res_y/4)),1)
		pg.draw.line(screen,RED,(0,(res_y/4 * 3)), ((res_x),(res_y/4 * 3)),1)
# проверяем события
# checking for events
	for event in pg.event.get():

# проверяем закрывшееся окно
		if event.type == pg.QUIT:
		    running = False

# проверяем события клавиатуры
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_KP_ENTER:
				running = False
# проверяем события мыши
		if event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1:
				print('left click', event.pos)
				for i in dsc:
					if (event.pos[0] in range(dsc[i][1][0],(dsc[i][1][0] + side)) and 
						event.pos[1] in range(dsc[i][1][1],(dsc[i][1][1] + side))):
						print(dsc[i])
						if (dsc[i][1][0], dsc[i][1][1]) not in list_of_coordinates:
							list_of_coordinates.append((dsc[i][1][0], dsc[i][1][1]))
						print(list_of_coordinates)
						dsc[i][0] = WHITE


			if event.button == 3:
				print('right click', event.pos)
				for i in dsc:
					if (event.pos[0] in range(dsc[i][1][0],(dsc[i][1][0] + side)) and 
						event.pos[1] in range(dsc[i][1][1],(dsc[i][1][1] + side))):
						print(dsc[i])
						if (dsc[i][1][0], dsc[i][1][1]) in list_of_coordinates:
							list_of_coordinates.remove((dsc[i][1][0], dsc[i][1][1]))
						print(list_of_coordinates)
						dsc[i][0] = BLUE

	clock.tick(FPS)
	pg.display.flip()

sd['dot_coordinates'] = {i: list_of_coordinates[i] 
					for i in range(0, len(list_of_coordinates))}

pg.quit()

with open(sd['sample_name'], 'w') as write_file:
	j.dump(sd,
			write_file,
			indent=4,
			ensure_ascii=False
			)