class Student():
    
    company = "Alabian Solutions"
    address = "No 12, Olu Akerele"
    
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        print('Your name is {} and age is {} with color {}'.format(self.name, self.age, self.color))
    
    def common_stuff(self):
        print('Our company name is {} and address is  {}'.format(self.company, self.address))
    
    def __str__(self):
            
        
student1 = Student('Vokna', 33, 'Dark')        
student1.common_stuff()
        