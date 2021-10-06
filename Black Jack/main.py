from random import randint


Player_input = str(input("Hit or pass(h) or (no)"))
player_total = 0
score = 21
playing = True
round = True
while playing == True:
    while player_total != score:
        print(Player_input)
        if Player_input == "h":
            rannum = randint(1, 11)
            player_total = rannum + player_total
            print(player_total)
            playing = False

        if playing == False:
            hit = str(input("do you want to hit again"))
            if hit == "yes":
                rannum = randint(1, 11)
                player_total = rannum + player_total
                print(player_total)
                playing = False
            if hit == "no":
                round = False

            if round == False:
                if player_total != score:
                    print("you lose")
                    break
                else:
                    print("you win")





















