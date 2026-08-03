from utils.Clear import clear
class Console:
    
    def __init__(self,ProductServise,сreateProductScreen,logger):
        self.productServise = ProductServise
        self.сreateProductScreen = сreateProductScreen
        self.logger = logger
        
    def menu(self):
        print('\nFoodTraker\n')
        print("Welcome bro!!!!\n")
        while True:

            print("Claculeta products: 1")
            print("Add products: 2")
            print("find products: 3")
            print("Exit: 4")
            print("Delite products: 5")
            print("Сhange products: 6")

            choice = int(input('=>'))
            
            match choice:
                
                case 1:
                    clear()
                    while True:
                        
                        try:
                        
                            choiceproduct = str(input("Name or id product =>"))
                            choicegrams = int(input("Grams =>"))
                            break
                        except Exception as ex :
                            clear()
                            if isinstance(ex, ValueError):
                                print("Velue not corect")
                            else:
                              self.logger.error(
                                 f"calculate choice -> {self.menu.__name__}: {ex }"
                                                )
                            
                    
                    
                        choiceProduct = self.productServise.ser_calculate(choiceproduct,choicegrams)
                        if not choiceProduct:
                            print(f"Ви имели в виду {self.productServise.find_similar_product(choiceproduct)}?")
                            choicesimilar = str(input("[Y/N] =>").upper)
                            if choicesimilar == 'N':
                                continue
                            choiceProduct = self.productServise.ser_calculate(choiceproduct,choicegrams)
                            
                        print(choiceProduct)
                        break
                      
                    
                
                case 2:
                    result = self.сreateProductScreen.get_product_data()
                    
                    
                    
                    print(f'\n{self.productServise.add_product(result)}\n')
                
                case 3:
                    while True:
                        try :
                                            
                            choiceproduct = str(input("Write product =>"))
                            break
                        except Exception as ex :
                            if isinstance(ex, ValueError):
                                print("NOT CORECT CHOICE!!!\n ")
                            else:
                                self.logger.error(
                                    f" find_product -> {self.menu.__name__}: {ex}"
                                                )
                                break
                            
                        choiceProduct = self.productServise.find_product(choiceproduct)
                        
                        if choiceProduct == str:
                            print(f"Ви имели в виду {choiceProduct}?")
                            choicesimilar = str(input("[Y/N] =>"))
                            if choicesimilar == 'N':
                                break
                          
                    print(choiceProduct)
                    
                    
                
                case 4:
                    
                    break
                
                case 5:
                    
                    try :
                                                             
                        choiceproduct = int(input("Id product delite =>"))
                        
                        print(self.productServise.)
                        
                    except Exception as ex :
                        
                        if isinstance(ex, ValueError):
                            
                            print("Don't CORECT CHOICE!!!\n ")
                            
                        else:
                            
                            self.logger.error(
                                f" delite_product -> {self.menu.__name__}: {ex}"
                                              )
                            
                            break
                
                case 6:
                    
                    pass
                
                case 7:
                    
                    pass
                
            
         
        


        
    
    
    





































