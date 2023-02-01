lives = 3
score = 0
score_needed = 1000
bullet_refresh = 1
level = 0

#adds lives every 1000 points
if score == score_needed:
    lives = lives + 1
    score_needed = score_needed + 1000

print(lives)