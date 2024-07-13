class Circle:
    
    def __init__(self, radius):
        
        self.radius=radius

    def circumference(self):

        print("circumference of the circle is", (2*3.14*self.radius))

    def area(self):

        print("Area of the circle is", (3.14* self.radius**2))

radius=int(input("Enter the radius:"))

circle=Circle(radius)

circle.area()

circle.circumference()