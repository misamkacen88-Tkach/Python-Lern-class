from utils.Clear import clear
from exceptions.navigation import BackToMenu,ExitApplication
from models.product import Product
from models.Meal import Meal


class Console:
    
    def __init__(self,foodServise,сreateProductScreen,commands,logger):
        self.foodServise = foodServise
        self.сreateProductScreen = сreateProductScreen
        self.commands = commands
        self.logger = logger
        
    def menu(self):
        print('\nFoodTraker\n')
        print("Welcome bro!!!!\n")
        
        while True:
            try:
                print("Calaculeta products: 1")
                print("Add products: 2")
                print("find products: 3")
                print("Exit: /exit -app")
                print("Delite products: 5")
                print("Сhange products: 6")

                self.commands.parse_and_execute_command(choice := input('=>'))
                
                match int(choice):
                    
                    case 1:
                        clear()
                        while True:
                            
                            try:
                                match self.commands.parse_and_execute_command(
                                                                                    str(input("What calculete?\nProduct 1\nMeal 2=>")),
                                                                                    context="Calaculeta"
                                                                                    ):
                                    case "1":
                                        food_class = Product
                                    case "2":
                                        food_class = Meal
                                    case _:
                                        print("Not corect object")
                                        continue
                                
                                
                                
                                
                                
                                self.commands.parse_and_execute_command(
                                                    choiceproduct := str(input(f"Name or id {food_class.class_name} =>")),
                                                    context="Calaculeta"
                                                    )
                                
                               
                                choicegrams = int(input("Grams =>"))
                                
                            except ValueError :
                                
                                clear()
                                
                                print("Velue not corect")
                                continue
                                
                                
                        
                        
                            choiceProduct = self.foodServise.ser_calculate(choiceproduct,choicegrams,cla)
                        
                            if not choiceProduct:
                                
                                choiceProduct = self.foodServise.find_similar_food(choiceproduct)
                            
                                if not choiceProduct:
                                    
                                    print("\nПродукта совершенно точно не существует \n")
                                    
                                    break
                                
                                print(f"Ви имели в виду {choiceProduct}?")
                                
                                self.commands.parse_and_execute_command(choicesimilar := str(input("[Y/N] =>").upper()))
                                
                                if choicesimilar == 'N':
                                    
                                    continue
                                
                                choiceProduct = self.foodServise.ser_calculate(choiceProduct,choicegrams) 
                            print(choiceProduct)
                            break
                            
                        
                        
                    
                    case 2:
                        result = self.сreateProductScreen.get_product_data()
                        
                        
                        
                        print(f'\n{self.foodServise.add_food(result)}\n')
                    
                    case 3:
                        while True:
                            try :
                                                
                                self.commands.parse_and_execute_command(choiceproduct := input("Write food =>"))
                                
                            except ValueError :
                               
                                print("\nNOT CORECT CHOICE!!!\n ")
                                continue
                                
                            choiceProduct = self.foodServise.find_food(choiceproduct)
                            
                            if not choiceProduct:
                                
                                choiceProduct = self.foodServise.find_similar_food(choiceproduct)
                                
                                if not choiceProduct:
                                                                    
                                    print("\nПродукта совершенно точно не существует \n")
                                                                    
                                    break
                                
                                print(f"Ви имели в виду {choiceProduct}?")
                                
                                self.commands.parse_and_execute_command(choicesimilar := str(input("[Y/N] =>").upper()))
                                
                                if choicesimilar == 'N':
                                    break
                                elif choicesimilar == 'Y' :
                                    сhoiceProduct = self.foodServise.find_food(choiceProduct)
                            
                            print(сhoiceProduct)
                            break
                        
                        
                    
                   
                    
                    case 5:
                        
                        try :
                                                                
                            self.commands.parse_and_execute_command(choiceproduct := input("Name or id food delite => "))
                            
                            
                            print(self.foodServise.delite_food(choiceproduct))
                            
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
            
            
                
         
        


        
    
    
    





































