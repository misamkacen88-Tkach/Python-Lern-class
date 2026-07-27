from models.product import Product

class ProductServise:
    
    def __init__(self, datebase, calculator,addProduct):
        
        self.datebase = datebase
        self.calculator = calculator
        self.addProduct = addProduct
        
    def find_product(self,name):
    
        
        result = self.datebase.find_product(name)
        
        return result
    
    def ser_calculate(self,name, grams):
        
            
            result = self.datebase.find_product(name)
            
            product = self.calculator.calculate_product(result,grams)
            
            return product
    
    def add_product(self):
        
        result = self.addProduct.get_product_data()
        
        result["id"]= self.datebase.get_new_product_id()
        
        
        
        product = Product.from_dict(result)
        
        self.datebase.save_product(product)
        return "Продукт успешно добавлено нах"
        















