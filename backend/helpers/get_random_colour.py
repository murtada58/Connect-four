import random


def get_random_colour(
    min_hue=0,
    max_hue=360,
    min_saturation=0,
    max_saturation=100,
    min_lightness=0,
    max_lightness=100,
):
    return f"""hsl(
        {min_hue + ((max_hue - min_hue) * random.random())},
        {min_saturation + ((max_saturation - min_saturation) * random.random())}%,
        {min_lightness + ((max_lightness - min_lightness) * random.random())}% 
    )"""
