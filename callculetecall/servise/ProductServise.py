from models.product import Product
from utils.decorators import log

class ProductServise:
    
    def __init__(self, datebase, calculator,logger):
        
        self.datebase = datebase
        self.calculator = calculator
        self.logger = logger
        
    @log
    def find_product(self,product_id):
    
        
        result = self.datebase.find_product_by_id(product_id)
        
        return result


    @log
    def ser_calculate(self,name, grams):
        
            
            result = self.datebase.find_product_by_id(name)
            
            product = self.calculator.calculate_product(result,grams)
            
            return product
    
    @log
    def add_product(self,result):
        
        
        
        result["id"]= self.datebase.get_new_product_id()
         
        
        product = Product.from_dict(result)
        
        self.datebase.save_product(product)
        return "Продукт успешно добавлено "
        















