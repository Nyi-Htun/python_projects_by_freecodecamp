class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = (2*self.width) + (2*self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2)**0.5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        line_width = '*' * self.width + '\n'
        line = ''
        for _ in range(self.height):
            line += line_width
        return line
    
    def get_amount_inside(self, rec):
        if self.get_area() < rec.get_area():
            return 0
        elif self.get_area() == rec.get_area():
            return 1
        else:
            return int(self.get_area() / rec.get_area())

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, new_width):
        self.set_side(new_width)

    def set_height(self, new_height):
        self.set_side(new_height)
    
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))