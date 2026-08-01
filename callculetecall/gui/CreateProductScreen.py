from utils.decorators import log
from utils.Clear import clear


class CreateProductScreen:

    def __init__(self, productFields, logger):

        self.logger = logger
        self.productFields = productFields

    @log
    def get_product_data(self):
        clear()
        while True:

            print("\t<Create product >\n")
            print("Plise write lines:")

            data = {}
            for key, (prompt, date_tape) in self.productFields.MAIN.items():
                try:

                    data[key] = date_tape(input(prompt))

                except Exception as ex:

                    if isinstance(ex, ValueError):
                        print(f"Dont corect product stat [ {key} ]")
                        break
                    else:
                        self.logger.error(
                            f"GenereteMain error -> {self.get_product_data.__name__}: {ex} | key: {key}"
                        )
                        break
            
            if len(data) == len(self.productFields.MAIN):
            
                break
        
        clear()
        while True:
        
            print("\t<Create product stept 2 >\n")
            print("Plise write lines:")
            
            data["vitamins"] = {}
            for key in self.productFields.VITAMINS:
                
                try:
                    
                    data["vitamins"][key] = float(input(key))
                     
                except Exception as ex:
                    
                    if isinstance(ex, ValueError):
                        print(f"Dont corect product stat [ {key} ]")
                        break
                    else:
                        self.logger.error(
                            f"GenereteVitamins error -> {self.get_product_data.__name__}: {ex} | key: {key}"
                        )
                        break
                    
            if len(data["vitamins"]) == len(self.productFields.VITAMINS):
            
                break
                
                
        clear()
        while True:
        
            print("\t<Create product stept 3 >\n")
            print("Plise write lines:")
            
            data["minerals"] = {}
            for key in self.productFields.MINERALS:
                
                try:
                    
                    data["minerals"][key] = float(input(key)) 
                    
                except Exception as ex:
                    
                    if isinstance(ex, ValueError):
                        print(f"Dont corect product stat [ {key} ]")
                        break
                    else:
                        self.logger.error(
                            f"GenereteMinerals error -> {self.get_product_data.__name__}: {ex} | key: {key}"
                        )
                        break
                    
            if len(data["minerals"]) == len(self.productFields.MINERALS):
            
                break
        
        return data
            
       
