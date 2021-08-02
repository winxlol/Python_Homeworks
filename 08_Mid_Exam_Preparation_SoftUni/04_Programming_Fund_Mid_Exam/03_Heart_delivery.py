class HeartDelivery:
    def __init__(self, neighborhood):
        self.neighborhood = neighborhood

    def run(self):
        index = 0
        last_index = 0
        while True:
            commands = input()

            if commands == "Love!":
                break

            commands = commands.split()

            jump = commands[0]
            lenght_jump = int(commands[1])

            if jump == "Jump":
                if self.neighborhood[index + lenght_jump] == 0:
                    index += lenght_jump
                    self.already_get_hearts(index, lenght_jump)
                else:
                    self.jump(lenght_jump, index, last_index)
                    self.hearts_need(index, last_index)

    def jump(self, lenght_jump, index, last_index):
        last_index = index
        index += lenght_jump
        if last_index + index > len(self.neighborhood):
            index = 0
            return self.neighborhood[index] - 2

        return self.neighborhood[index] - 2

    def hearts_need(self, index, last_index):
        if self.jump == 0:
            return print(f"Place {index} has Valentine's day.")

    def already_get_hearts(self, index, lenght_jump):
        index += lenght_jump
        if self.neighborhood[index] == 0:
            return print(f"Place {index} already had Valentine's day.")

    def all_get_hearts(self):
        undelivered_houses = 0
        for heart in self.neighborhood:
            if not heart == 0:
                undelivered_houses += 1
            else:
                return "Mission was successful."

        return f"Cupid has failed {undelivered_houses} places."

    def __repr__(self):
        return f"Cupid's last position was 2.\n{self.all_get_hearts()}"


neighborhood = input().split("@")
neighborhood = [int(el) for el in neighborhood]
delivery = HeartDelivery(neighborhood)
delivery.run()
print(delivery)