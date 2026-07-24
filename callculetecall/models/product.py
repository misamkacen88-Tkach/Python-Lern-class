class Product:

    def __init__(self, id, name, calories, protein, fat, cards,minerals, vitamins):

        self.id = id
        self.name = name
        
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.cards = cards
        
        self.vitamins = vitamins
        self.minerals = minerals
    
    def __str__(self):
        return (f"Name: {self.name}\n\n"
                f"Calories: {self.calories}\n\n"
                f"Protein: {self.protein}\n\n"
                f"Fat: {self.fat}\n\n"
                f"Cards: {self.cards}\n\n"
                f"Vitamins:\n{self._dict_to_string(self.vitamins)}\n\n"
                f"Minerals:\n{self._dict_to_string(self.minerals)}\n\n"
                )
    
    
    @classmethod
    def from_lines(cls,lines):
        
        lines = [line.strip() for line in lines]
        print('1 fromLines')
        return cls(
            int(lines[0]),
            lines[1],
            float(lines[2]),
            float(lines[3]),
            float(lines[4]),
            float(lines[5]),
            vitamins = {"B3":float(lines[6]),
                        "B6":float(lines[7]),
                        "B9":float(lines[8]),
                        "B5":float(lines[9]),
                        "B2":float(lines[10]),
                        "B7":float(lines[11]),
                        "B12":float(lines[12]),
                        "B9":float(lines[13])},
            
            minerals = {"Калий":float(lines[14]),
                        "Фосфор":float(lines[15]),
                        "Селен":float(lines[16]),
                        "Сера":float(lines[17]),
                        "Хлор":float(lines[18]),
                        "Натрий":float(lines[19]),
                        "Магний":float(lines[20]),
                        "Цинк":float(lines[21])}
                   )
        
    
    
    def _dict_to_string(self,data):
        return "\n".join(
            f"{key}: {value}"
            for key,value in data.items()
        )
    
    
    
    
    
    
    
    
    
    
    
    
    

