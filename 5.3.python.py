class circle:
    def_init_(self,radius):
        self.radius=radius
        def area(self):
            return 3.14*self.radius*self.radius
        def get_circle(r):
            return circle(r)
        c=get_circle(5)
        print("area of circle:",c.area())
        
