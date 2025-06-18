class animal:
    def sound(self):
        pass
    class Cat(animal):
        def sound(self):
            print("meow")
                class Dog(animal):
                    def sound(self):
                        print("wolf")
                        def make_sound(animal):
                            animal.sound()
                            cat=Cat()
                            dog=Dog()
                            make_sound(cat)
                            make_sound(dog)
                            
