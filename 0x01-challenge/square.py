#!/usr/bin/python3
"""Square Module
"""


class Square():
    """Square class
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """init function
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_my_square(self):
        """permiter_of_my_square function
        """
        return (self.width * 4)

    def __str__(self):
        """str function
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
