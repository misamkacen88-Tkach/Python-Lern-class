import os
import msvcrt

os.makedirs("accounts", exist_ok=True)
os.makedirs("histori", exist_ok=True)
os.makedirs("ideaout", exist_ok=True)

def clear():
    os.system('cls')

class Transaction:
    def __init__(self, data, operetion, amount):
        self.data = data
        self.operetion = operetion
        self.amount = int(amount) 
    
    def __str__(self):
        return f"{self.data};{self.operetion};{self.amount}"
    
    def __repr__(self):
        return self.__str__()
        
class HistoryTxt:
    def __init__(self,path):
        self.path = path
        os.makedirs(f"histori/{self.path}", exist_ok=True)
    
    def save(self,user_id,histori, x = 'a'):
        
        with open(f"histori/{self.path}/{user_id}.txt", x ) as file:
            file.write(f"{histori}\n")
    
    def read_history(self,user_id,x = False):
         with open(f"histori/{self.path}/{user_id}.txt",'r') as file:
             lines = file.readlines()
        
         for line in lines:
             print(line)
         if x:
          print("tach random buton.... ")
          msvcrt.getch()
          clear()    
    
    def save_all(self,user_id,history):
        
        with open(f"histori/{self.path}/{user_id}.txt", 'w') as file:
            for transaction in history:
                file.write(f"{transaction}\n")     
    
    def sort(self,user_id,key,reverses = False):
         with open(f"histori/{self.path}/{user_id}.txt",'r') as file:
             lines = file.readlines()
        
         history = []

         for line in lines:
           date, operation, amount = line.strip().split(";")
           history.append(Transaction(date, operation, amount))
         history.sort(key=key, reverse=reverses)
       
         self.save_all(user_id, history)
         self.read_history(user_id,x=True)
        





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
          self.history.save(self.id, f"2007.08.17;deposit;{amount}")
        
    def withdraw(self, amount, save_history = True):
        if self.__money >= amount:
            self.__money -= amount
            self.save()
            if save_history :
             self.history.save(self.id, f"2007.08.17;withdraw;-{amount}")
        else:
            print("Money is not enough")
            
    def show_balance(self, admin = False):
        print(f"Name: {self.name} \nBalance: {self.__money}")
        
        if admin:
            print(f"\nID: {self.id} \nHistory: ")
            self.history.read_history(self.id)
            
        
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
                self.history.save(self.id, f"2007.08.17;Transfer to {other_user.name}, {other_user.id};-{amount}")
                self.history.save(other_user.id, f"2007.08.17;Transfer from {self.name}, {self.id};{amount}")
            else:
              print("Operetion not faund")
        else:
            print("No correct data!")
                
            
            
            
        
        


class Workout:
    def __init__(self,traen):
        self.traen = traen
        with open(f"ideaout/{self.traen}.txt", "a") as file:
            file.write(" ")
    def read_idea(self):
        with open(f"ideaout/{self.traen}.txt", "r") as file:
            lines = file.readlines()
        
        clear()
        for i, task in enumerate(lines, start=0):
           print(f"{i}. {task.strip()}")
    
    def write_idea(self):
        clear()
    
        idea = input("We are ideas: ")
        with open(f"ideaout/{self.traen}.txt", "a") as file:
            file.write(f"\n{idea}; ")
       
    
    def delite_idea(self):
        
        clear()
        
        self.read_idea()
         
        idea = int(input("\nWath delite idea: ").strip())
        
        with open(f"ideaout/{self.traen}.txt", "r") as file:
            tasks = file.readlines()
        
        if idea == -1:
            
            tasks.clear() 
        elif -1<= idea <= len(tasks):
            
            tasks.pop(idea - 1)
        else:
            print("Еблан тупой нету такой задачи!!!!!!!!")
        
        
        with open(f"ideaout/{self.traen}.txt", "w") as file:
            file.writelines(tasks)
            
        
        
        
        
        

class Terminals:
    
    
    def __init__(self):
        self.bank = None
        self.idea = None
    
    
    def menu(self):  
         
        while True:
       
            print("\n1. Bank")
            print("2. WorkoutJournal")
            print("3. IdeaList")
            print("4. Exit")
        
            choice = input('> ').strip()
            
        
            if choice == '1':
                
              clear()  
              self.bank_manu()
              
            elif choice == '2':
                
                clear()
                self.idea_menu()
            elif choice == '3':
                
                clear()
                self.idea_menu()
                
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
                
                self.histori_Bank()
                
            elif choice_bank == '0':
                
                clear()
                self.bank.show_balance(True)
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
    
    def histori_Bank(self):
        
        while True:
         self.bank.history.read_history(self.bank.id)
         print("\n1. Wotch histori")
         print("\n2. Sort histori")
            
         choice_bank = input('> ').strip()
         if choice_bank == '4':
                  clear()
                  print("\nApp exit")
                  break
         elif choice_bank =='1':
              clear()
              self.bank.history.read_history(self.bank.id,x = True) 
         elif choice_bank == '2':
             reverse = False
             sort_by = '0'
             while True:
              clear()
              print(f"\n> tipe: {sort_by}: {reverse}")
              print(f"\n0. Reverse: {reverse}")
              print("\n1. Data")
              print("\n2. Operetion")
              print("\n3. Amount")
             
              choice_bank2 = input('> ').strip()
             
              if choice_bank2 == '4':
                   clear()
                   print("\nApp exit")
                   break
              elif choice_bank2 == '1':
                  sort_by = 'data'
              elif choice_bank2 == '2':
                  sort_by = 'operetion'
              elif choice_bank2 == '3':
                 sort_by = 'amount'
              elif choice_bank2 == '0' and reverse == False:
                 reverse = True
              elif choice_bank2 == '0' and reverse == True:
                 reverse = False
              elif choice_bank2 == '5' :
                  print(sort_by)
                  self.bank.history.sort(
                  self.bank.id,
                  key=lambda x: getattr(x, sort_by),
                  reverses=reverse)
               
              else:   
                  clear()
                  print(f"No commands < {choice_bank} >")
                 
                 
    # def idea_menu(self):
        
    #     while True:
    #         print("1. Add idea")
   
   
   
   
    
    def idea_menu(self):
        
        while True:
             print("\n1. Read idea")
             print("\n2. Write idea")
             print("\n3. Open idea dey")
             print("\n5. Delite idea")
             
             choice_idea = input('> ').strip()
             
             
             
             if choice_idea == '4':
                 
                clear()
                print("\nApp exit")
                break
            
             elif choice_idea == '3':
                 
                 print("Wath is the dey?")
                 self.idea = Workout(input('> ').strip())
                 clear()
                 
             elif self.idea is None:
                 
                 clear()
                 print("Open idea plise")
                 
             elif choice_idea == '1':
                 
                 self.idea.read_idea()
                 
             elif choice_idea == '2':
                 
                 self.idea.write_idea()
             elif choice_idea == '5':
                 
                 self.idea.delite_idea()
                 
             
             
            
    
  
                
                
                
            

terminal0 = Terminals()
terminal0.menu()
