import simple_draw as sd
import random

sd.resolution = (1400, 900)


def sun_prepare(xpoint, ypoint, radius, color, angle):
    delta_list = []
    radius_list = []
    for delta in range(0, 360, angle):
        delta_list.append(delta)
        radius_list.append(random.randint(radius - 10, radius + 10))

    return xpoint, ypoint, color, radius, delta_list, radius_list


def sun(prepare_list):
    xpoint = prepare_list[0]
    ypoint = prepare_list[1]
    color = prepare_list[2]
    radius = prepare_list[3]
    delta_list = prepare_list[4]
    radius_list = prepare_list[5]

    sd.start_drawing()
    point = sd.get_point(xpoint, ypoint)

    sd.circle(center_position=point, radius=radius * 4, color=sd.background_color, width=0)
    sd.circle(center_position=point, radius=radius, color=color, width=0)
    for j, (delta, radius) in enumerate(zip(delta_list, radius_list)):
        v = sd.get_vector(start_point=point, angle=delta, length=random.randint(radius * 2, radius * 3), width=5)
        v.draw(color)
        sd.sleep(0.02)
    sd.finish_drawing()


# prepare_data = sun_prepare(xpoint=700, ypoint=650, radius=40, color=sd.COLOR_YELLOW, angle=45)
# while True:
#     sun(prepare_data)
#     if sd.user_want_exit():
#         break

#sd.pause()
