class TheLift():
    def __init__(self, waiting_people, lift_state):
        self.waiting_people = waiting_people
        self.lift_state = lift_state

    def run(self):
        index = 0
        while len(self.lift_state) > index and self.waiting_people > 0:

            if self.lift_state[index] == 4:
                index += 1
                continue

            self.lift_state[index] += 1
            self.waiting_people -= 1

        if self.waiting_people == 0 and (len(self.lift_state) * 4) == sum(self.lift_state):
            self.no_people_and_full_wagon()
        elif self.waiting_people == 0:
            self.no_more_people()
        elif (len(self.lift_state) * 4) == sum(self.lift_state):
            self.no_wagon_space()

    def no_more_people(self):
        self.lift_state = [str(el) for el in self.lift_state]
        return print(f"The lift has empty spots!\n {' '.join(self.lift_state)}")

    def no_wagon_space(self):
        self.lift_state = [str(el) for el in self.lift_state]
        return print(f"There isn't enough space! {self.waiting_people} people in a queue!\n \
        {' '.join(self.lift_state)}")

    def no_people_and_full_wagon(self):
        self.lift_state = [str(el) for el in self.lift_state]
        return print(f"{' '.join(self.lift_state)}")


waiting_people = int(input())
lift_state = [int(el) for el in input().split()]
lift = TheLift(waiting_people, lift_state)
lift.run()