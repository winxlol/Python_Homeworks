from collections import defaultdict
players = {}


while True:
    data = input()

    if data == "Season end":
        break

    if ">" in data:
        player_details = data.split(" -> ")

        player = player_details[0]
        position = player_details[1]
        skill = int(player_details[2])

        if player not in players:
            players[player] = {}

        if position not in players[player]:
            players[player][position] = skill
        else:
            if skill > players[player][position]:
                players[player][position] = skill
    else:
        players_battle = data.split(" vs ")

        first_player = players_battle[0]
        second_player = players_battle[1]

        if first_player in players and second_player in players:
            for current_position in players[first_player].keys():
                if current_position in players[second_player].keys():
                    if players[first_player][current_position] > players[second_player][current_position]:
                        players.pop(second_player)
                        break
                    elif players[first_player][current_position] < players[second_player][current_position]:
                        players.pop(first_player)
                        break


total_points_of_players = defaultdict(int)

for name, player_info in players.items():
    for player_position, position_points in player_info.items():
        total_points_of_players[name] += position_points


for current_name, total_points in sorted(total_points_of_players.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{current_name}: {total_points} skill")
    for pos, pos_points in sorted(players[current_name].items(), key=lambda kvp: (-kvp[1], kvp[0])):
        print(f"- {pos} <::> {pos_points}")






