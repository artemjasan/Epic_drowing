import simple_draw as sd


def smile(x, y):
    point = sd.get_point(x, y)
    sd.circle(point, radius=60, color=sd.COLOR_YELLOW, width=0)
    sd.circle(point, radius=60, color=sd.COLOR_BLACK, width=3)
    point_1 = sd.get_point(x + 10, y + 20)
    point_2 = sd.get_point(x - 30, y + 20)
    point_3 = sd.get_point(x, y - 20)
    v1 = sd.get_vector(start_point=point_1, angle=0, length=15, width=3)
    v2 = sd.get_vector(start_point=point_2, angle=0, length=15, width=3)
    v1.draw(sd.COLOR_BLACK)
    v2.draw(sd.COLOR_BLACK)
    sd.circle(point_3, radius=20, color=sd.COLOR_DARK_RED, width=0)
    sd.circle(point_3, radius=20, color=sd.COLOR_BLACK, width=3)
    sd.sleep(0.3)
    sd.circle(point_3, radius=20, color=sd.COLOR_YELLOW, width=0)
    for a in [-20, 20]:
        y1 = y + 20
        eye = sd.get_point(x + a, y1)
        sd.circle(eye, radius=10, color=sd.COLOR_WHITE, width=0)
        sd.circle(eye, radius=10, color=sd.COLOR_BLACK, width=2)
        sd.circle(eye, radius=5, color=sd.COLOR_BLACK, width=0)

    y1 = y - 20
    x1_point = sd.get_point(x - 30, y1)
    x2_point = sd.get_point(x + 30, y1)
    sd.line(start_point=x1_point, end_point=x2_point, color=sd.COLOR_BLACK, width=3)


sd.start_drawing()
sd.finish_drawing()



