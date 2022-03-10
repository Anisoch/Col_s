from random import shuffle
from copy import deepcopy
from pygame import draw

class INITIAL_DOTS:
    #принимает словарь координат точек
    #работает в pygame, требует его импорта
    def __init__(
                self,
                dots_vok,
                screen,
                FPS
                ):
# принимаем значения из pygame
        self.screen = screen
        self.FPS = FPS

# создаем список координат точек копируем его для
# дальнейшего использования 
        self.original_dots = self.list_from_voc(dots_vok)
        self.dots_for_use = deepcopy(self.original_dots)
# берем изначальные координаты
        self.coordinates = self.dots_for_use.pop(0)

# задаем стартовые показатели
        self.brightness = 0
        self.timer = 0
        self.drawing = True

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
        '''ничего не принимает, решает продолжать ли
        действия или вернуть False'''

        if self.brightness < 256 and self.drawing:
            self.draw_a_dot()
# сколько секунд рисовать точку??
            self.drawing = self.needed_time(0.5,
                                         True,
                                         False)
            return True

        elif self.brightness < 256 and not self.drawing:
# сколько секунд задержка между точками
            self.drawing = self.needed_time(0.5,
                                      False,
                                      True)
            if self.drawing:
                self.check_the_list()
            return True

        else:
            return False

    def draw_a_dot(self):
        '''Функция рисует точку'''

        print(self.brightness)
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
            print(self.timer)
            self.timer += (1/self.FPS)
            return a
        else:
            self.timer = 0
            return b

    def check_the_list(self):
        """Функция проверяет длину списка точек.
        Если > 0, берет следующую из списка
        Если < 0, повышает яркость, пересоздает список
        координат от оригинального"""

        if len(self.dots_for_use) > 0:
            self.coordinates = self.dots_for_use.pop(0)
            print(self.coordinates)
        else:
            self.brightness_increase()
            self.dots_for_use = deepcopy(self.original_dots)
            self.coordinates = self.dots_for_use.pop(0)

    def brightness_increase(
                            self,
                            plus = 10
                            ):
        """принимает аргумент plus, который прибавляется к 
        имеющемуся уровню яркости"""

        self.brightness += plus

    def take_coordinates(
                        self,
                        brightness_plus = 25.5
                        ):
        '''функция принимает константный аргумент brightness_plus - 
        значение на которое будет возрастать яркость R в RGB.
        Заменяеет координаты точки self.coordinates
        на первый элемент списка методом "pop".
        По окончании списка повышает яркость и пересоздает список из
        оригинального '''
        
        if not self.next:
            if len(self.dots_for_use) > 0:
                self.coordinates = self.dots_for_use.pop(0)
            else:
                #эта часть останется, скорее всего
                self.dot_brightness += brightness_plus
                self.dots_for_use = deepcopy(self.original_dots)
                self.coordinates = self.dots_for_use.pop(0)
