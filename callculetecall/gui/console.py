from utils.Clear import clear
class Console:
    
    def __init__(self,ProductServise,logger):
        self.productServise = ProductServise
        self.logger = logger
        
    def menu(self):
        print('\nFoodTraker\n')
        print("Welcome bro!!!!\n")
        while True:

            print("Claculeta products: 1")
            print("Add products: 2")
            print("find products: 3")
            print("Exit: 4")
            print("Remuve products: 5")
            print("Сhange products: 6")

            choice = int(input('=>'))
            
            match choice:
                
                case 1:
                    clear()
                    while True:
                        
                        try:
                        
                            choiceproduct = int(input("Id product =>"))
                            choicegrams = int(input("Grams =>"))
                            break
                        except ValueError as ex :
                            clear()
                            print("Velue not corect")
                            self.logger.warning(
                                f"Dont correct choice -> {self.menu.__name__}: {ex }"
                                                )
                            
                    
                    choiceProduct = self.productServise.ser_calculate(str(choiceproduct),choicegrams)
                    
                    print(choiceProduct)
                    
                
                case 2:
                    result = self.addProduct.get_product_data()
                    
                    print(self.productServise.add_product(result ))
                
                case 3:
                    
                    pass
                
                case 4:
                    
                    break
                
                case 5:
                    
                    pass
                
                case 6:
                    
                    pass
                
                case 7:
                    
                    pass
                
            
            if choice == 4:
                break  
            elif choice == 2:
                print(self.productServise.add_product())
            elif choice == 3:
                try :
                                    
                    choiceproduct = int(input("Id product =>"))
                    
                except :
                    print("NOT CORECT CHOICE!!!\nStep 101")
                    
                
                choiceProduct = self.productServise.find_product(str(choiceproduct))
                print(choiceProduct)
                
        


        
    
    
    





































