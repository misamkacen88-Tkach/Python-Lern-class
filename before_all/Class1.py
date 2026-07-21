class BankAccaunt:
    
    def __init__(self,name, money):
        self._name = name
        self.__money = money
        
        
    def deposit(self, amount):
        self.__money += amount
        print(f"+ {amount} deposit")
        
    def say_profil(self):
        print(f"Name - {self._name}\nBalans - {self.__money}")

class VipAcc(BankAccaunt):
   
    def __init__(self, name, money):
        super().__init__(name, money)
    
    def withdraw(self, amount):
        super().withdraw(amount)
        comishin = amount * 5 / 100
        self.money -= comishin
        print(f"- 5% \n{self.money}")


bankAcc = BankAccaunt("Misha", 100)
bankAcc.deposit(20)
bankAcc.say_profil()










