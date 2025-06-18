class shape:
    def_init_(self,color):
        self.color=color
        def area(self):
            pass
        class Circle(shape):
            def_init_(self,color,radius):
                super()._init_(color)
                self.radius=radius
                def area(self):
                    return 3.14*self.radius**2
                class Rectangle(shape):
                    def_init_(self,color,width,height):
                        super()._init_(color)
                   self.width=width
                   self.height=height
                   def area(self):
                       return self.width*self.height
                    circle=Circle("red",5)
                    rectangle=Rectangle("blue",4,6)
                    print("Circle area:",circle.area())
                    print("Rectangle area:",rectangle.area())
                    
