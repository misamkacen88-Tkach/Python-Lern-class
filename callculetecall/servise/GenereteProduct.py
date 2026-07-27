
class GenereteProduct:
    
    def __init__(self,productFields):
        
        self.productFields = productFields 



    def get_product_data(self):
        
        while True:
            
            try:
                print("\t<Create product >\n")
                print("Plise write lines:")
        
                data = {
                    key: date_tape(input(prompt))
                    for key, (prompt,date_tape) in self.productFields.MAIN.items()
                }
                data["vitamins"] = {
                    key: float(input(key))
                    for key in self.productFields.VITAMINS
                }
        
                data["minerals"] = {
                    key: float(input(key))
                    for key in self.productFields.MINERALS
                }
            except:
                return None
                
            
        return data
        
        
        
        
        
        
                
         




















