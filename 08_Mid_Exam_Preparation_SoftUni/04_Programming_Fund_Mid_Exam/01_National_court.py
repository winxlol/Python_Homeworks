class NationalCourt:

    def __init__(self, employee_one: int, employee_two: int, employee_three: int, people_count: int):
        self.employee_one = employee_one
        self.employee_two = employee_two
        self.employee_three = employee_three
        self.people_count = people_count

    def total_employee_count_per_hour(self):
        return self.employee_one + self.employee_two + self.employee_three

    def needed_hours(self):
        working_hours = 0
        while self.people_count > 0:
            working_hours += 1
            self.people_count -= self.total_employee_count_per_hour()
            if working_hours % 4 == 0:
                working_hours += 1

        return working_hours

    def __repr__(self):
        return f"Time needed: {self.needed_hours()}h."


employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
people_count = int(input())

employee_work = NationalCourt(employee_one, employee_two, employee_three, people_count)
print(employee_work)


