cards = input().split()

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

is_terminated = False

for current_card in cards:
    current_team_card = current_card.split("-")
    team = current_team_card[0]
    player = int(current_team_card[1])

    if team == "A":
        if player in team_a:
            team_a.remove(player)
            if len(team_a) < 7:
                print(f"Team A - {len(team_a)}; Team B - {len(team_b)}\nGame was terminated")
                is_terminated = True
                break
    elif team == "B":
        if player in team_b:
            team_b.remove(player)
            if len(team_b) < 7:
                print(f"Team A - {len(team_a)}; Team B - {len(team_b)}\nGame was terminated")
                is_terminated = True
                break

if not is_terminated:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")


