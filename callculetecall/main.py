import bd

from servise.ProductServise import ProductServise
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
datebase = bd.Datebase(logger)
сreateProductScreen = CreateProductScreen(productFields,commands, logger)
productServise = ProductServise(datebase, calculator, logger)
console = Console(productServise,сreateProductScreen,commands, logger)


console.menu()
