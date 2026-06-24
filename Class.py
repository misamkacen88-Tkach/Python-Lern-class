import os
import msvcrt

os.makedirs("accounts", exist_ok=True)
os.makedirs("histori", exist_ok=True)
os.makedirs("Workout", exist_ok=True)

def clear():
    os.system('cls')

class HistoryTxt:
    def __init__(self,path):
        self.path = path
        os.makedirs(f"histori/{self.path}", exist_ok=True)
    
    def save(self,user_id,histori):
        
        with open(f"histori/{self.path}/{user_id}.txt",'a') as file:
            file.write(f"{histori}\n")
    
    def read_history(self,user_id):
         with open(f"histori/{self.path}/{user_id}.txt",'r') as file:
             lines = file.readlines()
        
         for line in lines:
             print(line)
         print("tach random buton.... ")
         msvcrt.getch()
         clear()

class BankAccount:
    def __init__(self,name,money,id):
        self.name = name
        self.__money = money
        self.id = id
        self.history = HistoryTxt('account_history')
     
    
    @property
    def money(self):
        return self.__money

    
    
    def deposit(self, amount, save_history = True):
        self.__money += amount
        self.save()
        if save_history :
          self.history.save(self.id, f" +{amount} Operetion depisit ")
        
    def withdraw(self, amount, save_history = True):
        if self.__money >= amount:
            self.__money -= amount
            self.save()
            if save_history :
             self.history.save(self.id, f" -{amount} Operetion withdraw ")
        else:
            print("Money is not enough")
            
    def show_balance(self):
        print(f"Name: {self.name} \nBalance: {self.__money}")
        
    def save(self):
        with open(f"accounts/{self.id}.txt", "w") as file:
           file.write(f"{self.name}\n")
           file.write(f"{self.__money}")  
    
    def transfer(self):
        
        target_id= input("Id plise: ")
        amount = int(input("Amount plise: "))
        
        if target_id == self.id:
            print("Нельзя перевести самому себе")
            return
        
        if self.__money >= amount and os.path.isfile(f"accounts/{target_id}.txt"):
     
            with open(f"accounts/{target_id}.txt", 'r') as file:
                lines = file.readlines()
               
            name = lines[0].strip()
            money = int(lines[1].strip())
           
            other_user = BankAccount(name, money, target_id)
            x = input(f"Перевод для {other_user.name}: подтвердить?")
            
            if x == "Yes":
                other_user.deposit(amount,False)
                self.withdraw(amount,False)
                self.history.save(self.id, f" -{amount} Transfer to {other_user.name} id {other_user.id} ")
                self.history.save(other_user.id, f" +{amount} Transfer from {self.name} id {self.id} ")
            else:
              print("Operetion not faund")
        else:
            print("No correct data!")
                
            
            
            
        
        


class Workout:
    def __init__(self,traen):
        self.traen = traen
        with open(f"Workout/{self.traen}.txt", "a") as file:
            file.write(" ")
    def read_work(self):
        with open(f"Workout/{self.traen}.txt", "r") as file:
            lines = file.readlines()
        
        clear()
        for i, task in enumerate(lines, start=0):
           print(f"{i}. {task.strip()}")
    
    def write_work(self):
        clear()
    
        work = input("We are works: ")
        with open(f"Workout/{self.traen}.txt", "a") as file:
            file.write(f"\n{work}; ")
       
    
    def delite_work(self):
        
        clear()
        
        self.read_work()
         
        work = int(input("\nWath delite work: ").strip())
        
        with open(f"Workout/{self.traen}.txt", "r") as file:
            tasks = file.readlines()
        
        if work == -1:
            
            tasks.clear() 
        elif -1<= work <= len(tasks):
            
            tasks.pop(work - 1)
        else:
            print("Еблан тупой нету такой задачи!!!!!!!!")
        
        
        with open(f"Workout/{self.traen}.txt", "w") as file:
            file.writelines(tasks)
            
        
        
        
        
        

class Terminals:
    
    
    def __init__(self):
        self.bank = None
        self.work = None
    
    
    def menu(self):  
         
        while True:
       
            print("\n1. Bank")
            print("2. WorkoutJournal")
            print("3. Todo list")
            print("4. Exit")
        
            choice = input('> ').strip()
            
        
            if choice == '1':
                
              clear()  
              self.bank_manu()
              
            elif choice == '2':
                
                clear()
                self.work_menu()
                
            elif choice == '4':
                
                clear()
                print("\nApp exit")
                break
            
            else:
                
                print("No commands")
    
    
    def bank_manu(self):
        
        while True:
            
            print("\n1. Balanse")
            print("2. To replenish")
            print("3. Withdraw")
            print("4. Exit")
            print("5. Accaunt")
            print("6. Transfer")
            print("7. History")
            
            
            choice_bank = input('> ').strip()
            
            if choice_bank == '4':
                clear()
                print("\nApp exit")
                break
            elif choice_bank == "5":
                
                self.creat_acc_Bank()
                
            elif self.bank is None:
                 clear()
                 print("Create account first")
                 
            elif choice_bank == '1':
                
                clear()
                
                self.bank.show_balance()
                
            elif choice_bank == '2':
                
              clear()
              print(f"Your money {self.bank.money}")
              self.bank.deposit(int(input("Your deposit: ")))
              
            elif choice_bank == '3':
                
                clear()
                print(f"Your money {self.bank.money}")
                self.bank.withdraw(int(input("Your withdarw: "))) 
            elif choice_bank == '6':
                
                clear()
                self.bank.transfer() 
            elif choice_bank == '7':
                
                clear()
                self.bank.history.read_history(self.bank.id) 
            else:
                
                clear()
                print(f"No commands < {choice_bank} >")
            
                
    def creat_acc_Bank(self):
        
         while True:
            
            print("\n1. Criet new accaunt")
            print("\n2. Вход")
            
            choice_bank = input('> ').strip()
            
            if choice_bank == '1':
                clear()
                name = input("\nNew name: ")
                money = int(input("Your money: "))
                id = input("\nNew id: ")
                
                
                self.bank = BankAccount(name, money,id)
                self.bank.save()
                clear()
                break
            
            elif choice_bank == '2':
                
                clear()
                
                id = input("\nYour id: ")
                
                if os.path.exists(f"accounts/{id}.txt"):
                    
                    print("Account found")
                    
                    with open(f"accounts/{id}.txt", 'r') as file:
                        lines = file.readlines()
                    
                    name = lines[0].strip()
                    money = int(lines[1].strip())
                    
                    self.bank = BankAccount(name, money,id)
                   
                    clear()
                    break
                else: 
                    clear()
                    print("Fake ID!!!!!")
            elif choice_bank == '4':
                clear()
                break
    
    
    def work_menu(self):
        
        while True:
             print("\n1. Read work")
             print("\n2. Write work")
             print("\n3. Open work dey")
             print("\n5. Delite work")
             
             choice_work = input('> ').strip()
             
             
             
             if choice_work == '4':
                 
                clear()
                print("\nApp exit")
                break
            
             elif choice_work == '3':
                 
                 print("Wath is the dey?")
                 self.work = Workout(input('> ').strip())
                 clear()
                 
             elif self.work is None:
                 
                 clear()
                 print("Open work plise")
                 
             elif choice_work == '1':
                 
                 self.work.read_work()
                 
             elif choice_work == '2':
                 
                 self.work.write_work()
             elif choice_work == '5':
                 
                 self.work.delite_work()
                 
             
             
            
    
  
                
                
                
            

terminal0 = Terminals()
terminal0.menu()
