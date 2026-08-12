from models.product import Product
from utils.decorators import log

class ProductServise:
    
    def __init__(self, database, calculator,logger):
        
        self.database = database
        self.calculator = calculator
        self.logger = logger
        
    
    @log
    def find_product(self,name):

            
            try:
                return self.database.find_product_by_id(int(name))
            except:
                return self.database.find_product_by_name(name)
                
        
    def find_similar_product(self,name):
        
        return self.database.find_similar_food(name)
        
    
    
    @log
    def find_product_id(self,product_id):
    
        
        result = self.database.find_product_by_id(product_id)
        
        return result

    @log
    def find_product_name(self,product_name):
    
        
        result = self.database.find_product_by_name(product_name)
        
        return result

    @log
    def ser_calculate(self,name, grams):
        result = self.find_product(name)
        
                
            
            
        return self.calculator.calculate_product(result,grams) if isinstance(result,Product) else result
    
    @log
    def add_product(self,result):
        
        
        
        result["id"]= self.database.get_new_product_id()
         
        
        product = Product.from_dict(result)
        
        self.database.save_product(product)
        return "Продукт успешно добавлено "

    @log
    def delite_product(self,name):
            try:
                return self.database.delite_product_by_id(int(name))
            except:
                return self.database.delite_product_by_name(name)

    @log
    def delite_product_by_name(self,name):
        
        result = self.database.delite_product_by_name(name)
        
        return f"Product -> {result}, delite"

    @log
    def delite_product_by_id(self,product_id):
        
        result = self.database.delite_product_by_id(product_id)
        
        return f"Product -> {result}, delite"
        















