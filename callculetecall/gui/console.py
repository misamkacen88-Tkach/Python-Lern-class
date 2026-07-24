
class Console:
    
    def __init__(self,ProductServise):
        self.productServise = ProductServise

    def menu(self):
        while True:
    
    
            print('\nFoodTraker\n')
            print("Welcome bro!!!!\n")
            print("Claculeta products: 1")
            print("Add products: 2")
            print("find products: 3")

            choice = int(input('=>'))
            
            if choice == 4:
                break
            elif choice == 1:
                
                choiceProduct = self.productServise.ser_calculate('1',100)
                print(choiceProduct)
                
                
            elif choice == 2:
                break
            elif choice == 3:
                choiceProduct = self.productServise.ser_calculate('1',100)
                print(choiceProduct)
                
        


        
    
    
    





































