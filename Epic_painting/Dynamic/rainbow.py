import simple_draw as sd


def rainbow_prepare(x, radius, delta, width):
    list_radius = [radius, radius - delta,
                   radius - delta * 2, radius - delta * 3,
                   radius - delta * 4, radius - delta * 5,
                   radius - delta * 6]
    rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
    return list_radius, rainbow_colors, x, width


def rainbow(prepare_lists):
    list_radius = prepare_lists[0]
    rainbow_colors = prepare_lists[1]
    x = prepare_lists[2]
    width = prepare_lists[3]
    point = sd.get_point(x, 0)
    sd.circle(
        point,
        radius=list_radius[0],
        color=sd.background_color,
        width=len(list_radius) * width
    )
    for j, (radius, color) in enumerate(zip(list_radius, rainbow_colors)):
        sd.start_drawing()
        sd.circle(point, radius=radius, color=color, width=width)
        sd.sleep(0.02)
        sd.finish_drawing()
        if sd.user_want_exit():
            break


# rainbow(x=500, radius=500, delta=20, width=20)
# sd.pause()
