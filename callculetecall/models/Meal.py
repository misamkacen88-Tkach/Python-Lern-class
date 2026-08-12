from models import product

class Meal(product):
    
    database_path = "database/Meal"
    name_class = "Meal"
    
    def __init__(self, 
                id, 
                name,
                grams, 
                calories, 
                protein, 
                fat, 
                cards,
                fiber,
                minerals, 
                vitamins,
                ingredients,
                recipe = None
        ):
        super().__init__(
                    id, 
                    name,
                    grams, 
                    calories, 
                    protein, 
                    fat, 
                    cards,
                    fiber,
                    minerals, 
                    vitamins,  
        )
        
        self.ingredients = ingredients
        self.recipe = recipe
    
    
    
    @classmethod
    def from_lines(cls, lines):
        
        data = super()._data_from_lines(lines)
         
        data["ingredients"] = list(lines[24])
        data["recipe"] = str(lines[25])
        
        return cls.from_dict(data)
    

