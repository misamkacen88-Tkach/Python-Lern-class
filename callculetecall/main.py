import bd

from servise.FoodServise import FoodServise
from servise.Calculator import Calculator
from servise.HelpService import HelpService
from gui.CreateProductScreen import CreateProductScreen
from gui.console import Console
from utils.Fields import ProductFields
from utils.Logger import Logger
from utils.commands import Commands

calculator = Calculator()
productFields = ProductFields()
logger = Logger()
helpService = HelpService("callculetecall/data")
commands = Commands(helpService,logger)
database = bd.Database(logger)
сreateProductScreen = CreateProductScreen(productFields,commands, logger)
foodServise = FoodServise(database, calculator, logger)
console = Console(foodServise,сreateProductScreen,commands, logger)


console.menu()
