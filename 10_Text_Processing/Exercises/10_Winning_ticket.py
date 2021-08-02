tickets = input().split(", ")

winning_symbol_at = '@' * 6
winning_symbol_hash = '#' * 6
winning_symbol_dollar = '$' * 6
winning_symbol_circumfix = '^' * 6


for ticket in tickets:
    ticket = ticket.strip()

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left_side = ticket[:10]
    right_side = ticket[10:]

    match_symbol = ""

    if winning_symbol_at in left_side and winning_symbol_at in right_side:
        match_symbol = "@"
    elif winning_symbol_hash in left_side and winning_symbol_hash in right_side:
        match_symbol = "#"
    elif winning_symbol_dollar in left_side and winning_symbol_dollar in right_side:
        match_symbol = "$"
    elif winning_symbol_circumfix in left_side and winning_symbol_circumfix in right_side:
        match_symbol = "^"
    else:
        print(f'ticket "{ticket}" - no match')
        continue

    left_side_count = left_side.count(match_symbol)
    right_side_count = right_side.count(match_symbol)

    match_lenght_symbol = min(left_side_count, right_side_count)

    if match_lenght_symbol == 10:
        print(f'ticket "{ticket}" - {match_lenght_symbol}{match_symbol} Jackpot!')
    else:
        print(f'ticket "{ticket}" - {match_lenght_symbol}{match_symbol}')

