class CounterStrike:
    def __init__(self, energy: int):
        self.initial_energy = energy
        self.win_counts = 0
        self.is_enough_energy = None

    def run(self):
        while True:
            distance = input()

            if distance == "End of battle":
                return print(f"Won battles: {self.win_counts}. Energy left: {self.initial_energy}")

            distance = int(distance)

            self.reach_an_enemy(distance)
            if self.is_enough_energy:
                break

            self.increase_energy()

    def reach_an_enemy(self, distance):
        if self.initial_energy >= distance:
            self.initial_energy -= distance
            self.win_counts += 1
        else:
            self.is_enough_energy = True
            return print(f"Not enough energy! Game ends with {self.win_counts} won battles and {self.initial_energy} energy")

    def increase_energy(self):
        if self.win_counts % 3 == 0:
            self.initial_energy += self.win_counts


energy = int(input())

cs = CounterStrike(energy)
cs.run()
