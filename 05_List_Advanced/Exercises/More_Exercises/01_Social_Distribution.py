def distribution(min_wealth, max_wealth):
    for min_index in range(len(min_wealth)):
        wealth_need = avar_wealth - min_wealth[min_index]

        for value in reversed(max_wealth):

            if value - wealth_need >= avar_wealth:
                min_wealth[min_index] += wealth_need
                max_index = max_wealth.index(value)
                max_wealth[max_index] -= wealth_need

                break
    return min_wealth


population = input().split(", ")
avar_wealth = int(input())

population = [int(el) for el in population]

min_wealth = [el for el in population if el < avar_wealth]
max_wealth = [el for el in population if el >= avar_wealth]

distribution(min_wealth, max_wealth)

flag = True

for el in min_wealth:
    if el < avar_wealth:
        flag = False        print("No equal distribution possible")
        break

if flag:
    print(min_wealth + max_wealth)




