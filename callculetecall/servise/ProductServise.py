

class ProductServise:
    
    def __init__(self, datebase):
        
        self.datebase = datebase
        
    def ser_calculate(self,name, grams):
    
        print('1 ser_cal')
        result = self.datebase.find_product(name)
        print('2 ser_cal')
        return result















