from random import randint

class Color:
    white = (255, 255, 255)
    dark_gray = (int("33", 16), int("33",16), int("33",16))
    gray = (int("66", 16), int("66",16), int("66",16))
    light_gray = (int("99", 16), int("99",16), int("99",16))
    lighter_gray = (int("CC", 16), int("CC",16), int("CC",16))
    lightest_gray = (int("EE", 16), int("EE",16), int("EE",16))
    brown = (int("65", 16), int("43",16), int("21",16))
    black = (0, 0, 0)
    orange = (255, 165, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    pink = (255, 0, 255)

    @classmethod
    def random_color(cls):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

    @classmethod
    def random_gray(cls):
        c = randint(0,255)
        return (c, c, c)

    @classmethod
    def random_red(cls):
        c = randint(0,255)
        return (c, 0, 0)

    @classmethod
    def random_green(cls):
        c = randint(0,255)
        return (0, c, 0)

    @classmethod
    def random_blue(cls):
        c = randint(0,255)
        return (0, 0, c)

    @classmethod 
    def random_yellow(cls):
        c = randint(0,255)
        return (c, c, 0)

    @classmethod
    def random_pink(cls):
        c = randint(0,255)
        return (c, 0, c)

