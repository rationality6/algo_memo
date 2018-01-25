import math


def get_components_from_mag(p_mag, p_deg):
    x = p_mag * math.sin(math.radians(p_deg))
    y = p_mag * math.cos(math.radians(p_deg))
    return (round(x, 2), round(y, 2))


def get_mag_from_components(x, y):
    result = math.sqrt(((x) ** 2) + ((y)**2))
    return result
