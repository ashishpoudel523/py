def game():
    return 78

score = game()
with open('E:/python/08/highscore.txt') as f:
    highscore = (f.read())
    
if highscore == '':
    with open('E:/python/08/highscore.txt', 'w') as f:
        f.write(str(score))

elif int(highscore)<score:
    with open("E:/python/08/highscore.txt", "w") as f:
        f.write(str(score))
