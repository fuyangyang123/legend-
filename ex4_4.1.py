presetnum = 4
active = True
while active:
    player = input("Please enter an integer between 0 and 9： ")
    player = int(player)
    if player > presetnum:
        print("Too heigh,Guess again: ")
    elif  player < presetnum:
        print("Too low,Guess again: ")
    else:
        print("Congratulations,You guessed!")
        break
