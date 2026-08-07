from utils.Clear import clear
from utils.commands import parse_and_execute_command
from exceptions.navigation import BackToMenu,ExitApplication
class Console:
    
    def __init__(self,ProductServise,сreateProductScreen,logger):
        self.productServise = ProductServise
        self.сreateProductScreen = сreateProductScreen
        self.logger = logger
        
    def menu(self):
        print('\nFoodTraker\n')
        print("Welcome bro!!!!\n")
        
        while True:
            try:
                print("Claculeta products: 1")
                print("Add products: 2")
                print("find products: 3")
                print("Exit: /exit -app")
                print("Delite products: 5")
                print("Сhange products: 6")

                parse_and_execute_command(choice := input('=>'))
                
                match int(choice):
                    
                    case 1:
                        clear()
                        while True:
                            
                            try:
                                choiceproduct = str(input("Name or id product =>"))
                                parse_and_execute_command(choiceproduct)
                                choicegrams = int(input("Grams =>"))
                                
                            except ValueError :
                                
                                clear()
                                
                                print("Velue not corect")
                                continue
                                
                                
                        
                        
                            choiceProduct = self.productServise.ser_calculate(choiceproduct,choicegrams)
                        
                            if not choiceProduct:
                                
                                choiceProduct = self.productServise.find_similar_product(choiceproduct)
                            
                                if not choiceProduct:
                                    
                                    print("\nПродукта совершенно точно не существует \n")
                                    
                                    break
                                
                                print(f"Ви имели в виду {choiceProduct}?")
                                
                                parse_and_execute_command(choicesimilar := str(input("[Y/N] =>").upper()))
                                
                                if choicesimilar == 'N':
                                    
                                    continue
                                
                                choiceProduct = self.productServise.ser_calculate(choiceProduct,choicegrams) 
                            print(choiceProduct)
                            break
                            
                        
                        
                    
                    case 2:
                        result = self.сreateProductScreen.get_product_data()
                        
                        
                        
                        print(f'\n{self.productServise.add_product(result)}\n')
                    
                    case 3:
                        while True:
                            try :
                                                
                                parse_and_execute_command(choiceproduct := input("Write product =>"))
                                
                            except ValueError :
                               
                                print("\nNOT CORECT CHOICE!!!\n ")
                                continue
                                
                            choiceProduct = self.productServise.find_product(choiceproduct)
                            
                            if not choiceProduct:
                                
                                choiceProduct = self.productServise.find_similar_product(choiceproduct)
                                
                                if not choiceProduct:
                                                                    
                                    print("\nПродукта совершенно точно не существует \n")
                                                                    
                                    break
                                
                                print(f"Ви имели в виду {choiceProduct}?")
                                
                                parse_and_execute_command(choicesimilar := str(input("[Y/N] =>").upper()))
                                
                                if choicesimilar == 'N':
                                    break
                                сhoiceProduct = self.productServise.find_product(choiceproduct)
                            
                            print(choiceProduct)
                            break
                        
                        
                    
                   
                    
                    case 5:
                        
                        try :
                                                                
                            parse_and_execute_command(choiceproduct := input("Name or id product delite => "))
                            
                            print(self.productServise.delite_product(choiceproduct))
                            
                        except ValueError :
                            
                            
                            print("Don't CORECT CHOICE!!!\n ")
                                
                           
                    
                    case 6:
                        
                        pass
                    
                    case 7:
                        
                        pass
                    
            except BackToMenu:
                continue
            
            except ExitApplication:
                print('\nProgram 200\n')
                break
            
            except Exception as ex:
                self.logger.error(
                    f" delite_product -> {self.menu.__name__}: {ex}"
                                )
                
         
        


        
    
    
    





































