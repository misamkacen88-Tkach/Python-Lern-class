import os
from difflib import get_close_matches
from models.product import Product
from utils.decorators import log




class Datebase:
    
    def __init__(self,logger):
        if not os.path.exists("callculetecall/datebase"):
            os.makedirs("callculetecall/datebase")
            
        self.logger = logger
        
        self.name_to_id = {}
        
        self._load_index()
        
    
    
    
    def find_product_by_id(self,id_product):
       
        try:
            with open(f"callculetecall/datebase/{id_product}.txt", 'r') as file:
                lines = file.readlines()
            
                product = Product.from_lines(lines)
                
        except Exception as ex:    
            self.logger.warning(
                f"Dont Find -> {self.find_product_by_id.__name__}: {ex}"
                )
            return None
            
        return product
    
    
    def find_product_by_name(self,name):
        
        name = name.lower()
        
        if name in self.name_to_id:
            
            return self.find_product_by_id(self.name_to_id[name])
        
        return None
    
    
    def find_similar_product(self,name):
        
     
        
        matches = get_close_matches(
            name,
            self.name_to_id.keys(),
            n =1,
            cutoff=0.75
        )
        

        return matches[0] if matches else None
        
        
        
    
    def save_product(self,product):
    
        
        with open(f"callculetecall/datebase/{product.id}.txt", 'w') as file:
            
            file.write("\n".join(product.to_lines()))
        
        self._update_index(product)
            
    
        
    def get_new_product_id(self):
        
         

        ids = [
            int(file[:-4])          
            for file in os.listdir("callculetecall/datebase")
            if file.endswith(".txt")
        ]

        if not ids:
            return 1

        return max(ids) + 1
    
    
    def _update_index(self, product):
        
        self.name_to_id[product.name.lower()] = product.id
    
    
    @log
    def _load_index(self):
        
        self.name_to_id.clear()
        
        for file_name in os.listdir("callculetecall/datebase"):
            
            
            try:
                with open(f"callculetecall/datebase/{file_name}", 'r' ) as file:
                    
                    
                    id_product = int(file.readline().strip())
                    
                    name_product = file.readline().strip()
            
            except Exception as ex:
                self.logger.error(
                    f" datebase -> {self._load_index.__name__}: {ex}"
                                  )
                
            self.name_to_id[name_product.lower()] = id_product
                
        
    
  
        











