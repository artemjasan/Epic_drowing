# -*- coding: utf-8 -*-
import simple_draw as sd
import random

from Dynamic.smoke import smoke_prepare, smoke
from Dynamic.snowfall import snowfall, snow_prepare
from Dynamic.sun import sun_prepare, sun
from Dynamic.rainbow import rainbow, rainbow_prepare
from Dynamic.smile import smile
from Static.flowers import fractal_flower

from Static.house import house
from Static.field import field
from Static.trees import fractal_tree

sd.resolution = (1400, 800)
n = 0  # Counter

# Drawing the field
field(b=1400, color=sd.COLOR_BROWN)

# Drawing the fractal trees
fractal_tree(point=sd.get_point(1200, 50), angle=90, length=100, delta=30,
             color=sd.COLOR_BROWN, colorleaf=sd.COLOR_GREEN)
fractal_tree(point=sd.get_point(1050, 50), angle=90, length=110, delta=25,
             color=sd.COLOR_BROWN, colorleaf=sd.COLOR_GREEN)
fractal_tree(point=sd.get_point(850, 50), angle=90, length=100, delta=30,
             color=sd.COLOR_BROWN, colorleaf=sd.COLOR_GREEN)

# Drawing the fractal garden grass
flower_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_WHITE,
                 sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

for i in range(560, 1400, 9):
    fractal_flower(point=sd.get_point(i, 50), angle=90, length=20, delta=10, border=7,
                   color=flower_colors[random.randint(0, len(flower_colors)-1)])

# Create a house
house(ypoint=50, xpoint=250, wall_heigth=10, wall_width=6)

# Prepare data for the animation functions
prepare_lists_sun = sun_prepare(xpoint=750, ypoint=670, radius=40, color=sd.COLOR_YELLOW, angle=30)
prepare_lists_smoke = smoke_prepare(number=50, xstart=500, ystart=495)
prepare_lists_snowfall = snow_prepare(number=50, xstart=0, xend=180)
prepare_lists_rainbow = rainbow_prepare(x=550, radius=1050, delta=10, width=10)

while True:  # while loop for animation
    n += 1
    snowfall(prepare_lists_snowfall)  # call snowfall function
    smoke(prepare_lists_smoke)  # call smoke function
    if n % 30 == 0:
        sun(prepare_lists_sun)  # call sunshine function
    if n % 150 == 0:
        rainbow(prepare_lists_rainbow)  # call rainbow function
    if n % 250 == 0:
        smile(x=400, y=380)  # call smile function
    if sd.user_want_exit():
        break

sd.pause()
# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)
# пример см. results/04_painting.jpg
# **************************************************
# Усложненное задание.
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
