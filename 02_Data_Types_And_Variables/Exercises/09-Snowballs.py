import sys
attempts = int(input())

highest_ball_score = -sys.maxsize
snowball_snow = 0
snowball_time = 0
snowball_quality = 0

for attempt in range(attempts):
    temp_snowball_snow = int(input())
    temp_snowball_time = int(input())
    temp_snowball_quality = int(input())

    snowball_value = (temp_snowball_snow / temp_snowball_time) ** temp_snowball_quality

    if snowball_value > highest_ball_score:
        highest_ball_score = snowball_value
        snowball_snow = temp_snowball_snow
        snowball_time = temp_snowball_time
        snowball_quality = temp_snowball_quality

print(f"{snowball_snow} : {snowball_time} = {round(highest_ball_score)} ({snowball_quality})")
