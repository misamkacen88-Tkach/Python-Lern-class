import os
from difflib import get_close_matches
from models.product import Product
from models.Meal import Meal
from utils.decorators import log




class Database:
    
    def __init__(self,logger):
        
        
        self.paths = ["database/Product","database/Meal"]
        
        self.__for_Create_file(self.paths)
        
        self.logger = logger
        
        self.name_to_id = {}
        
        self._load_index(self.paths)
        
    
    
    
    def find_food_by_id(self,id_food, food_class):
       
        try:
            with open(f"callculetecall/{food_class.database_path}/{id_food}.txt", 'r', encoding="utf-8") as file:
                lines = file.readlines()
                
                food = food_class.from_lines(lines)
                
                
        except Exception as ex:    
            self.logger.warning(
                f"Dont Find -> {self.find_food_by_id.__name__}: {ex}"
                )
            return None
            
        return food
    
    
    def find_food_by_name(self,name,food_class = Product):
        
        name = name.lower()
        
        
        if name in self.name_to_id:
            
            return self.find_food_by_id(self.name_to_id[name], food_class)
        
        return None
    
    
    def find_similar_food(self,name):
        
     
        
        matches = get_close_matches(
            name,
            self.name_to_id.keys(),
            n =1,
            cutoff=0.75
        )
        

        return matches[0] if matches else None
        
           
    
    def save_food(self,food):
    
        
        with open(f"callculetecall/{food.database_path}/{food.id}.txt", 'w',encoding="utf-8") as file:
            
            file.write("\n".join(food.to_lines()))
        
        self._update_index(food)
            
        
    def delite_food_by_id(self, food_id, food_class = Product):
        
        if os.path.exists(f"callculetecall/{food_class.database_path}/{food_id}.txt"):
            os.remove(f"callculetecall/{food_class.database_path}/{food_id}.txt")
            return "Продукт успешно удален"
            
    
    def delite_food_by_name(self, name,food_class = Product):
        
        name = name.lower()
                
        if name in self.name_to_id:
                    
            return self.delite_food_by_id(self.name_to_id[name], food_class)
                
        return None
        
        
    def get_new_food_id(self, food_class = Product):
        
         

        ids = [
            int(file[:-4])          
            for file in os.listdir(f"callculetecall/{food_class.database_path}")
            if file.endswith(".txt")
        ]

        if not ids:
            return 1

        return max(ids) + 1
    
    
    
    
    
    
    
    def _update_index(self, food):
        
        self.name_to_id[food.name.lower()] = food.id
    
    
    @log
    def _load_index(self,paths):
        
        self.name_to_id.clear()
        for file in paths:
            for file_name in os.listdir(f"callculetecall/{file}"):
                
                
                try:
                    with open(f"callculetecall/{file}/{file_name}", 'r',encoding="utf-8" ) as file:
                        
                        
                        id_food = int(file.readline().strip())
                        
                        name_food = file.readline().strip()
                        
                
                except Exception as ex:
                    self.logger.error(
                        f" database -> {self._load_index.__name__}: {ex}"
                                    )
                    
                self.name_to_id[name_food.lower()] = id_food



    def __for_Create_file(self, paths):
        
        for file_name in paths:
            
            if not os.path.exists(f"callculetecall/{file_name}"):
                os.makedirs(f"callculetecall/{file_name}")
        
    
  
        











