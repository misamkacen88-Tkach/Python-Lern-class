class ProductFields:

    def __init__(self):
        
        self.MAIN = {
        "name": ("Название: ", str),
        "grams":("Грами: ", int),
        "calories": ("Калории: ", float),
        "protein": ("Белки: ", float),
        "fat": ("Жиры: ", float),
        "cards": ("Углеводы: ", float)
        }

        self.VITAMINS = [
        "B3: " , "B9: ",
        "B6: " , "B7: ",
        "B11: ", "B13: ",
        "B12: ", "B10: "
        ]
     

        self.MINERALS = [
         "Калий1: ", "Калий2: ",
         "Магний11: ", "Магний2: ",
         "Цинк1: ", "Цинк2: ",
         "Цинк3: ", "Цинк4: "
        ]