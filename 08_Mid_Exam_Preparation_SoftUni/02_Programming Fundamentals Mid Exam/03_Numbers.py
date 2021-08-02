import sys


class topBiggestNumber:
    def __init__(self, numbers):
        self.numbers = numbers
        self.searched_numbers = []
        self.max_number = -sys.maxsize

    def avarage_number(self):
        return sum(numbers) / len(numbers)

    def run(self):
        while True:

            for current_number in self.numbers:
                if current_number > self.max_number and current_number > self.avarage_number():
                    self.max_number = current_number

            if len(self.searched_numbers) < 5:
                if self.max_number in self.numbers:
                    self.searched_numbers.append(self.max_number)
                    self.numbers.remove(self.max_number)
                    self.max_number = -sys.maxsize
            else:
                break

            if self.avarage_number() >= max(self.numbers):
                break

    def __repr__(self):
        searched_numbers_parse_to_str = [str(el) for el in self.searched_numbers]

        if len(searched_numbers_parse_to_str) > 0:
            return f"{' '.join(searched_numbers_parse_to_str)}"
        else:
            return "No"


numbers = [int(el) for el in input().split()]

find_numbers = topBiggestNumber(numbers)
find_numbers.run()
print(find_numbers)

