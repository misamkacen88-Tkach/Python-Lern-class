from utils.decorators import log
from utils.Clear import clear


class CreateProductScreen:

    def __init__(self, productFields, logger):

        self.logger = logger
        self.productFields = productFields

    @log
    def get_product_data(self):
        clear()
        while True:

            print("\t<Create product >\n")
            print("Plise write lines:")

            data = {}
            for key, (prompt, date_tape) in self.productFields.MAIN.items():
                try:

                    data[key] = date_tape(input(prompt))

                except Exception as ex:

                    if isinstance(ex, ValueError):
                        print(f"Dont corect product stat [ {key} ]")
                    else:
                        self.logger.error(
                            f"GenereteMain error -> {self.get_product_data.__name__}: {ex} | key: {key}"
                        )
            break

        data["vitamins"] = {
            key: float(input(key)) for key in self.productFields.VITAMINS
        }

        data["minerals"] = {
            key: float(input(key)) for key in self.productFields.MINERALS
        }
        return data
