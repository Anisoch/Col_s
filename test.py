from random import shuffle
from copy import deepcopy
from pygame import draw

class TEST:
    def __init__(
                self,
                dots_vok,
                screen,
                FPS
                ):
# параметры для работы pygame
# принимается из основного модуля программы
        self.screen = screen
        self.FPS = FPS

# создаем список координат точек
        self.dots_for_use = self.list_from_voc(dots_vok)
# берем изначальные координаты
        self.coordinates = self.dots_for_use.pop(0)

# задаем изначальную яркость
# self.initial_brightness должна быть принята от первого объекта
        self.initial_brightness = 0
        self.brightness = self.initial_brightness

# работа таймеров
        self.timer = 0
        self.drawing = True
        self.delay = False
        self.response_delay = False

# создаем список для записи результатов
        self.results = []



    def list_from_voc(
                      self,
                      d):

        '''Принимает словарь (номер точки) - кортеж координат
        пример 1 : (200,300)
        возвращает перемешанный "список" координат'''

        spis = [d[i] for i in d]
        shuffle(spis)
        return spis

    def go_on(self):
# если нет команды о задержке после нажатия
        if not self.response_delay:
# отрисовываем точку
            if self.drawing and not self.delay:
                self.draw_a_dot()
# время демонстрации точки
                self.drawing = self.needed_time(1, True, False)
# окончание отрисовки запускает задержку между точками
                if not self.drawing:
                    self.delay = True 

            elif not self.drawing and self.delay:
                print('delay')
                self.delay = self.needed_time(1, True, False)
                if not self.delay:
                    self.drawing = True
                    self.brightness_increase(60, 5)
        else:
            print('response delay')
            print(self.timer)
            self.response_delay = self.needed_time(1, True, False)


    def draw_a_dot(self):
        '''Функция рисует точку'''
        print(self.coordinates)
        draw.rect(
                  self.screen,
                 (self.brightness,0,0),
                 (self.coordinates[0],self.coordinates[1],10,10)
                  )

    def needed_time(
                    self,
                    t,
                    a,
                    b
                    ):
        """Функция принимает 3 аргумента a,b,t
    до истечения времени t возвращает аргумент a
    по истечению времени t возвращает аргумент b"""

        if self.timer < t:
            self.timer += (1/self.FPS)
            return a
        else:
            self.timer = 0
            return b

    def brightness_increase(
                            self,
                            to,
                            step
                            ):
        '''Функция принимает 2 аргумента:
        to - до какого уровня дожна импульсно нарастать яркость
        step - шаг нарастания яркости'''

        if self.brightness < to:
            self.brightness += step
            print('новая яркость: ', self.brightness)
        else:
            self.brightness = self.initial_brightness
            print('возвращена исходная яркость: ', self.brightness)

    def response(self):
        if len(self.dots_for_use) > 0:
            self.response_delay = True
            print('response')
            self.results.append((self.coordinates, self.brightness))
            self.timer = 0
            self.drawing = True
            self.delay = False
            self.coordinates = self.dots_for_use.pop(0)
            self.brightness = self.initial_brightness
            return True
        else:
            return False

