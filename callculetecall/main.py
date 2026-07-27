import bd

from servise.ProductServise import ProductServise
from servise.Calculator import Calculator
from servise.GenereteProduct import GenereteProduct
from gui.console import Console
from utils.Fields import ProductFields



datebase = bd.Datebase()
calculator = Calculator()
productFields = ProductFields()
genereteProduct = GenereteProduct(productFields)
productServise = ProductServise(datebase,calculator,genereteProduct)
console = Console(productServise)



console.menu()













