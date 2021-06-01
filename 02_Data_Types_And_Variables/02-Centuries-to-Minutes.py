YEARS = 100
DAYS = 365.2422
HOURS = 24
MINUTES = 60

centuries = int(input())

years = centuries * YEARS
days = years * DAYS
days = round(days)
hours = days * HOURS
minutes = hours * MINUTES

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")