import os
from models.product import Product





class Datebase:
    
    def __init__(self):
        if not os.path.exists("callculetecall/datebase"):
            os.makedirs("callculetecall/datebase")
            print('папку бд создано')
        else:
            print('папку бд найдено')
        
        self.bdId = {}
    
    
    
    def find_product(self,id_product):
       
        try:
            with open(f"callculetecall/datebase/{id_product}.txt", 'r') as file:
                lines = file.readlines()
            
                product = Product.from_lines(lines)
                
        except:
            print('2 find Errorr')
            return None
            
        return product
    
    
    
    def save_product(self,product):
        
        
        
        print("save 1")
        
        with open(f"callculetecall/datebase/{product.id}.txt", 'w') as file:
            
            file.write("\n".join(product.to_lines()))
            
        print('save 2')
            
  
        
    def get_new_product_id(self):
        
         

        ids = [
            int(file[:-4])          
            for file in os.listdir("callculetecall/datebase")
            if file.endswith(".txt")
        ]

        if not ids:
            return 1

        return max(ids) + 1
        
        
  
        











