class Shoot:
    def __init__(self, targets):
        self.targets = targets
        self.shot_targets = 0

    def run(self):
        while True:
            token = input()

            if token == "End":
                self.targets = [str(el) for el in self.targets]
                return print(f"Shot targets: {self.shot_targets} -> {' '.join(self.targets)}")

            indices = int(token)

            if self.valid_target(indices):
                shooted_target = self.targets[indices]

                if shooted_target == -1:
                    continue

                self.targets[indices] = -1
                self.shot_targets += 1

                self.reduce_or_increase(shooted_target)

    def valid_target(self, indices):
        if 0 <= indices < len(self.targets):
            return True

        return False

    def reduce_or_increase(self, shooted_target):
        for current_target in self.targets:
            if current_target > shooted_target:
                current_target_index = self.targets.index(current_target)
                self.targets[current_target_index] -= shooted_target
            elif current_target <= shooted_target:
                current_target_index = self.targets.index(current_target)
                self.targets[current_target_index] += shooted_target


targets = [int(el) for el in input().split()]
shoot = Shoot(targets)
shoot.run()