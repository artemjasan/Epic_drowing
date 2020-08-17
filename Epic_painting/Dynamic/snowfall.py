from typing import Tuple, List, Union

import simple_draw as sd

import random


sd.resolution = (1400, 800)


def snow_prepare(number, xstart, xend) -> Tuple[Union[List[Union[float, int]], int], ...]:
    x_list = []
    y_list = []
    list_delta = []
    list_fa = []
    list_fb = []
    list_fc = []
    y_sugrob = []
    for _ in range(number):
        x_list.append(sd.random_number(xstart, xend))
        y_list.append(sd.random_number(800, 1200))
        list_delta.append((sd.random_number(20, 35)) / 10)
        list_fa.append((random.randint(1, 99)) / 100)
        list_fb.append((random.randint(1, 99)) / 100)
        list_fc.append(random.randint(1, 179))
        y_sugrob.append(60)
    return x_list, y_list, list_delta, list_fa, list_fb, list_fc, y_sugrob, xend


def snowfall(prepared_lists: Tuple[Union[List[Union[float, int]], int], ...]):
    x_list = prepared_lists[0]
    y_list = prepared_lists[1]
    list_delta = prepared_lists[2]
    list_fa = prepared_lists[3]
    list_fb = prepared_lists[4]
    list_fc = prepared_lists[5]
    y_sugrob = prepared_lists[6]
    xend = prepared_lists[7]
    sd.start_drawing()
    for j, x in enumerate(x_list):
        if x_list[j] > (xend + 5):
            x_list[j] = xend
        if y_list[j] < y_sugrob[j]:
            y_sugrob[j] += 5
            y_list[j] = sd.random_number(800, 900)
            continue
        y = y_list[j]
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=10, color=sd.background_color,
                     factor_a=list_fa[j],
                     factor_b=list_fb[j],
                     factor_c=list_fc[j])
        x_list[j] = x_list[j] + random.randint(-1, 1)
        y_list[j] -= list_delta[j]
        new_point = sd.get_point(x_list[j], y_list[j])
        sd.snowflake(center=new_point, length=10, color=sd.COLOR_WHITE,
                     factor_a=list_fa[j],
                     factor_b=list_fb[j],
                     factor_c=list_fc[j])

    sd.sleep(0.01)
    sd.finish_drawing()
    # if sd.user_want_exit():
    #     break




#sd.pause()
