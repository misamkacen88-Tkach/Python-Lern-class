class BankAccount:

    def __init__(self, money):
        self.__money = money

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):

        if value >= 0:
            self.__money = value
        else:
            print("Balance can't be negative")


acc = BankAccount(100)

acc.money = 10

print(acc.money)