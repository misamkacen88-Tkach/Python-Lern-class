import os
from models.product import Product





class Datebase:
    
    def __init__(self,logger):
        if not os.path.exists("callculetecall/datebase"):
            os.makedirs("callculetecall/datebase")
        
        self.logger = logger
        self.bdId = {}
    
    
    
    def find_product_by_id(self,id_product):
       
        try:
            with open(f"callculetecall/datebase/{id_product}.txt", 'r') as file:
                lines = file.readlines()
            
                product = Product.from_lines(lines)
                
        except Exception as ex:
            self.logger.warning(
                f"Dont Find -> {self.find_product_by_id.__name__}: {ex}"
                )
            return "Dont Find"
            
        return product
    
    
    
    def save_product(self,product):
        
        
        
      
        
        with open(f"callculetecall/datebase/{product.id}.txt", 'w') as file:
            
            file.write("\n".join(product.to_lines()))
            
        
            
  
        
    def get_new_product_id(self):
        
         

        ids = [
            int(file[:-4])          
            for file in os.listdir("callculetecall/datebase")
            if file.endswith(".txt")
        ]

        if not ids:
            return 1

        return max(ids) + 1
        
        
  
        











