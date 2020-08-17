import simple_draw as sd


def fractal_flower(point, angle, length, delta, color, border):
    if length < border:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    if border < length < border + 5:
        v1.draw(color=color)
    else:
        v1.draw(color=sd.COLOR_GREEN, width=3)
    random_delta = sd.random_number((delta - 0.4 * delta), int(delta + 0.41 * delta))  # random delta for the angles
    next_point = v1.end_point
    next_angle = angle - random_delta
    next_point2 = v1.end_point
    next_angle2 = angle + random_delta
    shift_length = 75
    coef = sd.random_number(int(shift_length * 0.8), int(shift_length * 1.21))  # random coef. for the length branch
    next_length = length * (coef / 100)
    fractal_flower(point=next_point, angle=next_angle, length=next_length,
                   delta=delta, color=color, border=border)
    fractal_flower(point=next_point2, angle=next_angle2, length=next_length,
                   delta=delta, color=color, border=border)
