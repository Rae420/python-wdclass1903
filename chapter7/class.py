class Car():
    name = 'bmw_x6'
    color = 'red'
    wheels = 4

    def car_detail(self):
        result = 'The name of the car is '+self.name+' and the color is '+self.color+' with '+self.wheels
        return result

bmw = Car()
print(bmw.name)
print(bmw.color)
print(bmw.wheels)
