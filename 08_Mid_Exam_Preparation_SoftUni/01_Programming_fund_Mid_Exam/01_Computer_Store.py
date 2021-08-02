class Receipt:
    def __init__(self):
        self.total_price = 0
        self.taxes = 0
        self.special_cust = 0
        self.regular_cust = 0
        self.data = None

    def run(self):
        while True:
            token = input()
            self.data = token
            if token == "special" or token == "regular":
                break

            price = float(token)
            if price < 0:
                self.is_negaative_price(price)
            else:
                self.total_price_count(price)
                self.total_taxes(price)

    def total_price_count(self, price):
        self.total_price += price

    def total_taxes(self, price):
        self.taxes += (price * 0.20)

    def customer(self):
        if self.data == "special":
            self.special_cust = (self.total_price + self.taxes) * 0.90

            return f"{self.special_cust:.2f}"
        elif self.data == "regular":
            self.regular_cust = self.total_price + self.taxes

            return f"{self.regular_cust:.2f}"

    def is_negaative_price(self, price):
        if price < 0:
            return print("Invalid price!")

    def __repr__(self):
        if self.total_price == 0:
            return "Invalid order!"

        return f"Congratulations you've just bought a new computer!\nPrice without taxes: {self.total_price:.2f}$\n" \
               f"Taxes: {self.taxes:.2f}$\n-----------\nTotal price: {self.customer()}$"


receipt = Receipt()
receipt.run()
print(receipt)







