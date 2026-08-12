from models.product import Product
from utils.decorators import log

class FoodServise:
    
    def __init__(self, database, calculator, logger):
        
        self.database = database
        self.calculator = calculator
        self.logger = logger
        
    
    @log
    def find_food(self,name, food_class = Product):

            
            try:
                return self.database.find_food_by_id(int(name), food_class)
            except:
                return self.database.find_food_by_name(name, food_class)
                
        
    def find_similar_food(self,name):
        
        return self.database.find_similar_food(name)
        
    
    
    @log
    def find_food_id(self,food_id):
    
        
        result = self.database.find_food_by_id(food_id)
        
        return result

    @log
    def find_food_name(self,food_name):
    
        
        result = self.database.find_food_by_name(food_name)
        
        return result

    @log
    def ser_calculate(self,name, grams):
        result = self.find_food(name)
        
                
            
            
        return self.calculator.calculate_food(result,grams) if isinstance(result,Product) else result
    
    @log
    def add_food(self,result, food_class = Product):
        
        
        
        result["id"]= self.database.get_new_food_id()
         
        
        food = food_class.from_dict(result)
        
        self.database.save_food(food)
        return "Продукт успешно добавлено "

    @log
    def delite_food(self,name, food_class = Product):
            try:
                return self.database.delite_food_by_id(int(name))
            except:
                return self.database.delite_food_by_name(name)

    @log
    def delite_food_by_name(self,name):
        
        result = self.database.delite_food_by_name(name)
        
        return f"Food -> {result}, delite"

    @log
    def delite_food_by_id(self,food_id):
        
        result = self.database.delite_food_by_id(food_id)
        
        return f"Product -> {result}, delite"