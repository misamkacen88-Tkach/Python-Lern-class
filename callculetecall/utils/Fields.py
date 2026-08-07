class ProductFields:

    def __init__(self):
        
        self.MAIN = {
        "name": ("Название: ", str),
        "grams":("Грами: ", int),
        "calories": ("Калории: ", float),
        "protein": ("Белки: ", float),
        "fat": ("Жиры: ", float),
        "cards": ("Углеводы: ", float),
        "fiber": ("Клечатка: ", float)
        }

        self.VITAMINS = [
        "A: " , "C: ",
        "D: " , "E: ",
        "K: ", "B1: ",
        "B9: ", "B12: "
        ]
     

        self.MINERALS = [
         "Калций: ", "Магний: ",
         "Калий: ", "Натрий: ",
         "Фосфор: ", "Железо: ",
         "Цинк: ", "Селен: "
        ]