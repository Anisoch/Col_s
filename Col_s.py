# импотрируем модули
# importing modules
import copy
import pygame
from sys import path
from os import getcwd,chdir
import json

# downloading sample
# загружаем шаблон
chdir('samples')
with open('new.json', 'r') as read_file:
	data = json.load(read_file)
chdir('..')

import brightness_determination_2 as b
import test as t


d = {
    1 : (100, 100),
    2 : (100, 200),
    3 : (100, 300),
    4 : (200, 100),
    5 : (200, 200),
    6 : (200, 300),
    7 : (300, 100),
    8 : (300, 200),
    9 : (300, 300)
    }


#задаем параметры окна экрана
WIDTH = data['res_x']
HEIGHT = data['res_y']


#задаем цвета
BLACK = (0,0,0)

#ФПС привязан к движку программы для старта - 60
FPS = 60

#создаем игру 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Col_S")
clock = pygame.time.Clock()

#создаем объекты
new_dot = b.INITIAL_DOTS(d, screen, FPS)
experiment = t.TEST(data['dot_coordinates'], screen, FPS)

# создаем крестик
cross = pygame.image.load('cross.png')
cross_coordinates = (WIDTH/2-2, HEIGHT/2-2)

running = True
while running:
	screen.fill(BLACK)
	screen.blit(cross,cross_coordinates)

	running = new_dot.go_on()

	for event in pygame.event.get():
# проверяем закрывшееся окно
		if event.type == pygame.QUIT:
		    running = False
# проверяем нажате на ENTER
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP_ENTER:
				running = False
				


	clock.tick(FPS)
	pygame.display.flip()

experiment.initial_brightness = new_dot.brightness
experiment.brightness = new_dot.brightness


running = True
while running:
	screen.fill(BLACK)
	screen.blit(cross,cross_coordinates)			
	experiment.go_on()

	for event in pygame.event.get():
# проверяем закрывшееся окно
		if event.type == pygame.QUIT:
		    running = False

# проверяем нажате на ENTER
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP_ENTER:
				running = experiment.response()
				

	clock.tick(FPS)
	pygame.display.flip()


pygame.quit()
l = experiment.results
print('\n\nполученные результаты: ')
# for i in l:
# 	print(i)
print(l)
 