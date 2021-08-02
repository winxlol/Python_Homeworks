class ArrayModifier:
    def __init__(self, array):
        self.array = array

    def run(self):
        while True:
            tokens = input().split()

            if tokens[0] == "end":
                break

            command = tokens[0]

            if command == "swap":
                index_one = int(tokens[1])
                index_two = int(tokens[2])

                self.swap(index_one, index_two)
            elif command == "multiply":
                index_one = int(tokens[1])
                index_two = int(tokens[2])

                self.multiply(index_one, index_two)
            elif command == "decrease":
                self.decrease()

    def swap(self, index_one, index_two):
        self.array[index_one], self.array[index_two] = self.array[index_two], self.array[index_one]

    def multiply(self, index_one, index_two):
        number = int(self.array[index_one]) * int(self.array[index_two])
        self.array[index_one] = str(number)

    def decrease(self):
        self.array = [int(el) for el in self.array]
        self.array = map(lambda x: x - 1, self.array)

    def __repr__(self):
        self.array = [str(el) for el in self.array]
        return f"{', '.join(self.array)}"


array = input().split()
array_modifier = ArrayModifier(array)
array_modifier.run()
print(array_modifier)