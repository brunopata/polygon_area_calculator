class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        count = self.height
        polygon = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            while count > 0:
                polygon += "*" * self.width + "\n"
                count -= 1
        return polygon

    def get_amount_inside(self, new_polygon):
        area_polygon = self.width * self.height
        area_new_polygon = new_polygon.width * new_polygon.height
        count = 0
        while area_polygon - area_new_polygon >= 0:
                area_polygon -= area_new_polygon
                count += 1
        return count

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side
        
    def set_side(self, new_side):
        self.side = new_side
        self.width = new_side
        self.height = new_side

    def set_width(self, new_width):
        super().set_width(new_width)
        self.side = new_width
        self.height = new_width

    def set_height(self, new_height):
        super().set_height
        self.side = new_height
        self.width = new_height

    def __str__(self):
        return "Square(side={})".format(self.side)
