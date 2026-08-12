class Animal:
    
    def __init__(self):
        self.x = 'tttgg'
    
    
    
    def info(self):
        print("I Animal")
        raise NotImplementedError
    
    def speak(self):
        print("gaf")

class Dog(Animal):
    
    def info(self):
           
           print('5')
        

        
        
class Cat(Animal):
    
    def info(self):
       
        print('5')
        
    def speak(self):
        print("may")
        
        
class Duck(Animal):
    
    def __init__(self):
        super().__init__()
    
    def info(self):
       
        print('5')
   
        
    def speak(self):
        print("Kra")



animals = [Dog(), Cat(), Duck()]


for animal in animals:
    animal.info()
    animal.speak()
    animal.x

