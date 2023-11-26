class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length
    
square_of_num = Square(5)
square_area = square_of_num.area()
shape_instance = Shape()
shape_area = shape_instance.area()

print(f"Area of square is: {square_area}")
print(f"Area of shape is: {shape_area}")