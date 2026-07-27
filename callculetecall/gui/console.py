from utils.Clear import clear
class Console:
    
    def __init__(self,ProductServise):
        self.productServise = ProductServise

    def menu(self):
        print('\nFoodTraker\n')
        print("Welcome bro!!!!\n")
        while True:

            print("Claculeta products: 1")
            print("Add products: 2")
            print("find products: 3")

            choice = int(input('=>'))
            
            if choice == 4:
                break
            elif choice == 1:
                clear()
                try:
                    
                    choiceproduct = int(input("Id product =>"))
                    choicegrams = int(input("Grams =>"))
                except :
                    print("NOT CORECT CHOICE!!!\nStep 101")
                    break
                
                choiceProduct = self.productServise.ser_calculate(str(choiceproduct),choicegrams)
                clear()
                print(choiceProduct)
                
                
            elif choice == 2:
                print(self.productServise.add_product())
            elif choice == 3:
                try :
                                    
                    choiceproduct = int(input("Id product =>"))
                    
                except :
                    print("NOT CORECT CHOICE!!!\nStep 101")
                    
                
                choiceProduct = self.productServise.find_product(str(choiceproduct))
                print(choiceProduct)
                
        


        
    
    
    





































