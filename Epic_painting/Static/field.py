import simple_draw as sd


def field(b, color):
    x, y = 0, 0  # start position

    for i in range(x, b, 50):
        point = sd.get_point(i, y)
        sd.square(left_bottom=point, side=50, color=color, width=0)

