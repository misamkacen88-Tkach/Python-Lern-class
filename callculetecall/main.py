import bd

from servise.ProductServise import ProductServise
from servise.Calculator import Calculator
from gui.CreateProductScreen import CreateProductScreen
from gui.console import Console
from utils.Fields import ProductFields
from utils.Logger import Logger

calculator = Calculator()
productFields = ProductFields()
logger = Logger()
datebase = bd.Datebase(logger)
сreateProductScreen = CreateProductScreen(productFields, logger)
productServise = ProductServise(datebase, calculator, logger)
console = Console(productServise,сreateProductScreen, logger)


console.menu()
