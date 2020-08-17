from typing import Tuple, List, Union

import simple_draw as sd

import random

sd.resolution = (1400, 800)


def smoke_prepare(number, xstart, ystart) -> Tuple[Union[List[Union[float, int]], int], ...]:
    x_list = []
    y_list = []
    list_length = []
    list_delta = []
    list_width = []
    y_border = []

    for _ in range(number):
        x_list.append(sd.random_number(xstart, xstart + 5))
        y_list.append(sd.random_number(ystart + 5, ystart + 5))
        list_length.append(random.randint(5, 10))
        list_delta.append((random.randint(30, 150)) / 100)
        list_width.append((random.randint(1, 5)))
        y_border.append(900)

    return x_list, y_list, list_length, list_delta, list_width, y_border, xstart, ystart


def smoke(prepared_lists: Tuple[Union[List[Union[float, int]], int], ...]):
    x_list = prepared_lists[0]
    y_list = prepared_lists[1]
    list_length = prepared_lists[2]
    list_delta = prepared_lists[3]
    list_width = prepared_lists[4]
    y_border = prepared_lists[5]
    x_start = prepared_lists[6]
    y_start = prepared_lists[7]

    sd.start_drawing()
    for j, x in enumerate(x_list):
        if y_list[j] > y_border[j]:
            y_list[j] = sd.random_number(y_start + 5, y_start + 5)
            x_list[j] = sd.random_number(x_start - 2, x_start + 2)
            continue
        width = list_width[j]
        y = y_list[j]
        length = list_length[j]
        point = sd.get_point(x, y)
        sd.circle(center_position=point, radius=length, color=sd.background_color, width=width)
        x_list[j] = x_list[j] + random.randint(-1, 1)
        y_list[j] += list_delta[j]
        new_point = sd.get_point(x_list[j], y_list[j])
        sd.circle(center_position=new_point, radius=length, color=sd.COLOR_DARK_CYAN, width=width)

    sd.sleep(0.01)
    sd.finish_drawing()
    # if sd.user_want_exit():
    #     break

# sd.pause()
