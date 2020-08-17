import simple_draw as sd


# sd.resolution = (1600, 900)
# Universal function for drawing of typical shapes (triangle, square, pentagon, hexagon a etc.)
# angle: triangle - 120, square - 90, pentagon - 72, hexagon - 60
def shape(point, length, angle, color, width):
    abc = 50
    start_point = point
    for delta in range(0, (360 - angle), angle):
        v = sd.get_vector(start_point=point, angle=delta, length=(length + abc), width=width)
        v.draw(color)
        point = v.end_point
    sd.line(start_point=start_point, end_point=point, width=width, color=color)


# Drawing the tube
def tube(point, length, color, width):
    start_point = point
    abc = 50
    v = sd.get_vector(start_point=start_point, angle=0, length=(length + abc), width=width)
    v.draw(color)
    point_0 = v.end_point
    v1 = sd.get_vector(start_point=point_0, angle=120, length=(length + abc) / 3, width=width)
    v1.draw(color)
    point_1 = v1.end_point
    v2 = sd.get_vector(start_point=point_1, angle=90, length=(length + abc) / 4, width=width)
    v2.draw(color)
    point_2 = v2.end_point
    v3 = sd.get_vector(start_point=point_2, angle=180, length=(length + abc) / 12, width=width)
    v3.draw(color)
    point_3 = v3.end_point
    v3 = sd.get_vector(start_point=point_3, angle=270, length=(length + abc) / 10, width=width)
    v3.draw(color)


def square(point, length, wall_h):  # Colored border around the brick wall
    vertical_length = wall_h * 25
    start_point = point
    v1 = sd.get_vector(start_point=point, angle=0, length=length, width=3)
    v1.draw(sd.COLOR_ORANGE)
    point = v1.end_point
    v2 = sd.get_vector(start_point=point, angle=90, length=vertical_length, width=3)
    v2.draw(sd.COLOR_ORANGE)
    point = v2.end_point
    v3 = sd.get_vector(start_point=point, angle=180, length=length, width=3)
    v3.draw(sd.COLOR_ORANGE)
    point = v3.end_point
    sd.line(start_point=start_point, end_point=point, width=3, color=sd.COLOR_ORANGE)


def window(point, side, color):
    sd.square(left_bottom=point, side=side, color=color, width=0)  # Colored square of the window
    shape(point=point, length=(side / 2 + 25),
          angle=90, width=5, color=sd.COLOR_BLACK)  # Black border around the window
    #  Painting black line on the middle of the colored square
    v = sd.get_vector(start_point=point, length=(side / 2), angle=0, width=5)
    v.draw(sd.COLOR_BLACK)
    next_point = v.end_point
    v1 = sd.get_vector(start_point=next_point, length=side, angle=90, width=5)
    v1.draw(sd.COLOR_BLACK)


# Drawing the brick wall
def house(xpoint, ypoint, wall_heigth, wall_width):
    width = 50  # Size of the brick
    height = 25  # Size of the brick
    y = ypoint
    y1 = height
    point_0 = sd.get_point((xpoint - height), (wall_heigth + 2) * height)  # Start point for the roof
    side_window = width * (wall_width / 2)  # The width of the window, which depends on the width of the brick wall
    point_win_x = xpoint + (width * wall_width / 4)
    point_win_y = ypoint + (height * wall_heigth / 4)
    point_win = sd.get_point(point_win_x, point_win_y)

    for i in range(wall_heigth):
        y_end = xpoint + width * wall_width
        start_point = sd.get_point(xpoint, y)
        end_point = sd.get_point(y_end, y)
        sd.line(start_point, end_point, sd.COLOR_ORANGE, width=3)

        if i % 2 == 0:
            x1 = xpoint
            x2 = xpoint
            for _ in range(wall_width + 1):
                start_point = sd.get_point(x1, y)
                end_point = sd.get_point(x2, y + y1)

                sd.line(start_point, end_point, sd.COLOR_ORANGE, width=3)
                x1 += width
                x2 += width
        else:
            x1 = xpoint + (width / 2)
            x2 = xpoint + (width / 2)
            for _ in range(wall_width):
                start_point = sd.get_point(x1, y)
                end_point = sd.get_point(x2, y + y1)
                sd.line(start_point, end_point, sd.COLOR_ORANGE, width=3)
                x1 += width
                x2 += width
        y += height

    # Calling other parts of the house
    square(point=sd.get_point(xpoint, ypoint), length=wall_width * width, wall_h=wall_heigth)  # call square function
    window(point=point_win, side=side_window, color=sd.COLOR_DARK_YELLOW)  # call window function
    shape(point=point_0, angle=120, length=wall_width * width, width=3, color=sd.COLOR_RED)  # call roof function
    tube(point=point_0, length=wall_width * width, width=3, color=sd.COLOR_RED)  # call tube function
    # sd.pause()
    return point_win, side_window
# house(ypoint=50, xpoint=600, wall_heigth=10, wall_width=9)
