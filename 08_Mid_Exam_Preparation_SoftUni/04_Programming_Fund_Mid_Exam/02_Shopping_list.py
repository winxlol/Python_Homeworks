class ShoppingList:
    def __init__(self, groceries):
        self.groceries = groceries

    def run(self):
        while True:
            tokens = input()

            if tokens == "Go Shopping!":
                return self.groceries

            tokens = tokens.split(maxsplit=1)
            command = tokens[0]

            if command == "Urgent":
                item = tokens[1]

                self.urgent(item)
            elif command == "Unnecessary":
                item = tokens[1]

                self.unnecessary(item)
            elif command == "Correct":
                old_item, new_item = tokens[1].split()

                self.correct(old_item, new_item)
            elif command == "Rearrange":
                item = tokens[1]

                self.re_arrange(item)

    def item_exist(self, item):
        if item in self.groceries:
            return False

        return item

    def urgent(self, item):
        if self.item_exist(item):
            self.groceries.insert(0, item)

    def unnecessary(self, item):
        if self.item_exist(item) is False:
            self.groceries.remove(item)

    def correct(self, old_item, new_item):
        if old_item in self.groceries:
            old_item_index = self.groceries.index(old_item)
            self.groceries.remove(old_item)
            self.groceries.insert(old_item_index, new_item)

    def re_arrange(self, item):
        if self.item_exist(item) is False:
            self.groceries.remove(item)
            self.groceries.append(item)

    def __repr__(self):
        return f'{", ".join(self.groceries)}'


groceries = input().split("!")
shop = ShoppingList(groceries)
shop.run()
print(shop)


