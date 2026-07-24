import bd
from servise.ProductServise import ProductServise
from gui.console import Console

datebase = bd.Datebase()
productServise = ProductServise(datebase)
console = Console(productServise)



console.menu()













