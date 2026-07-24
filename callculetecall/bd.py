import os
from models.product import Product





class Datebase:
    
    def __init__(self):
        if not os.path.exists("callculetecall/datebase"):
            os.makedirs("callculetecall/datebase")
            print('папку бд создано')
        else:
            print('папку бд найдено')
    
    def find_product(self,id_product):
        print(' 1 find')
        try:
            with open(f"callculetecall/datebase/{id_product}.txt", 'r') as file:
                lines = file.readlines()
            
                product = Product.from_lines(lines)
                print('2 find')
        except:
            print('2 find Errorr')
            return None
            
        return product
        
        
        











