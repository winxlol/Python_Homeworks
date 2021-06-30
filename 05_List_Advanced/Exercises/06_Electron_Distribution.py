electrons = int(input())

shell_position = 0

electron_factory = []

while electrons > 0:
    shell_position += 1

    shell_max_electrons = 2 * (shell_position ** 2)

    if shell_max_electrons <= electrons:
        electron_factory.append(shell_max_electrons)
    else:
        electron_factory.append(electrons)

    electrons -= shell_max_electrons

print(electron_factory)
