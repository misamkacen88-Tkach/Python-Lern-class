class Product:

    def __init__(self, id, name,grams, calories, protein, fat, cards,fiber,minerals, vitamins):

        self.id = id
        self.name = name
        
        self.grams = grams
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.cards = cards
        
        self.fiber = fiber
        
        
        self.vitamins = vitamins
        self.minerals = minerals
    
    def __str__(self):
        return (f"Name: {self.name}\n\n"
                f"Grams: {self.grams}\n\n"
                f"Calories: {self.calories}\n\n"
                f"Protein: {self.protein}\n\n"
                f"Fat: {self.fat}\n\n"
                f"Cards: {self.cards}\n\n"
                f"Fider: {self.fiber}\n\n"
                f"Vitamins:\n{self._dict_to_string(self.vitamins)}\n\n"
                f"Minerals:\n{self._dict_to_string(self.minerals)}\n\n"
                )
    
    
    @classmethod
    def from_lines(cls,lines):
        
        lines = [line.strip() for line in lines]
        
        
        data = {
            "id" : int(lines[0]),
            'name':lines[1],
            "grams" : int(lines[2]),
            "calories" : float(lines[3]),
            "protein" : float(lines[4]),
            "fat":float(lines[5]),
            "cards":float(lines[6]),
            "fiber":float(lines[7]),
            "vitamins" : {"A":float(lines[8]),
                        "C":float(lines[9]),
                        "D":float(lines[10]),
                        "E":float(lines[11]),
                        "K":float(lines[12]),
                        "B1":float(lines[13]),
                        "B9":float(lines[14]),
                        "B12":float(lines[15])},
            "minerals" : {"Калций":float(lines[16]),
                        "Магний":float(lines[17]),
                        "Калий":float(lines[18]),
                        "Натрий":float(lines[19]),
                        "Фосфор":float(lines[20]),
                        "Железо":float(lines[21]),
                        "Цинк":float(lines[22]),
                        "Селен":float(lines[23])}}
            
         
        
        
        
        
        return cls.from_dict(data)
        

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
    
    
    
    
    
    
    def __mul__(self, coefficient):
        
        grams = self.grams * coefficient
        calories = self.calories * coefficient
        protein = self.protein * coefficient
        fat = self.fat * coefficient
        cards = self.cards * coefficient
        fiber = self.fiber *coefficient
        
        new_vitamins = {
            key: value * coefficient
            for key, value in self.vitamins.items()
        }
        
        new_minerals = {
            key: value * coefficient
            for key,value in self.minerals.items()
        }
        
        return self._copy(self.id,
                          self.name,
                          grams,
                          calories,
                          protein,
                          fat,
                          cards,
                          fiber,
                          vitamins = new_vitamins,
                          minerals = new_minerals
                          )
            

    def __rmul__(self, coefficient):
        return self.__mul__(coefficient)



    def _copy(self,
              id,
              name,
              grams, 
              calories, 
              protein, 
              fat, cards,
              fiber,
              vitamins,
              minerals
              ):
        return Product(id,
                      name,
                      grams, 
                      calories, 
                      protein, 
                      fat, 
                      cards,
                      fiber,
                      vitamins,
                      minerals)
    
    
    def _dict_to_string(self,data):
        return "\n".join(
            f"{key}: {value}"
            for key,value in data.items()
        )
    

    def to_lines(self):
        
        return [
        str(self.id),
        self.name,
        
        str(self.grams),
        str(self.calories),
        str(self.protein),
        str(self.fat),
        str(self.cards),
        str(self.fiber),
        *map(str, self.vitamins.values()),
        *map(str, self.minerals.values()),
        ]
    
    
    
    
    
    
    
    
    
    
    

