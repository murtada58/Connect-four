import random


def get_random_colour(
    min_hue: int = 0,
    max_hue: int = 360,
    min_saturation: int = 0,
    max_saturation: int = 100,
    min_lightness: int = 0,
    max_lightness: int = 100,
) -> str:
    return f"""hsl(
        {min_hue + ((max_hue - min_hue) * random.random())},
        {min_saturation + ((max_saturation - min_saturation) * random.random())}%,
        {min_lightness + ((max_lightness - min_lightness) * random.random())}% 
    )"""
