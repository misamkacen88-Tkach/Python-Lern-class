class Animal:
    
    def info(self):
        print("I Animal")
        raise NotImplementedError

class Dog(Animal):
    
    def info(self):
        
        print('5')
        
    def speak(self):
        print("gaf")
        
        
class Cat(Animal):
    
    def info(self):
       
        print('5')
        
    def speak(self):
        print("may")
        
        
class Duck(Animal):
    
    def info(self):
       
        print('5')
   
        
    def speak(self):
        print("Kra")



animals = [Dog(), Cat(), Duck()]


for animal in animals:
    animal.info()
    animal.speak()

