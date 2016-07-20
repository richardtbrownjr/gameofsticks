import os

def play_round(numb, player):
#player_list = ['player 1',1,'player 2', 2]
    print(player, end='')
    turn_sticks_chosen = (int(input('how many sticks (1,2,or 3) do you want in this turn. ')))
    #if turn_sticks_chosen not 1,2,3 call again
    print("There are {} sticks left".format , numb = numb - turn_sticks_chosen)
    return numb

def pick_number_of_sticks():
    #numb = int(range(1, 100))
    number_of_sticks = int(input('How many sticks do you want in this game. '))
    return number_of_sticks

def player1(player):
    return("Player 1 ")

def player2(player):
    return("Player 2 ")

def game_over(numb):
    pass
    #if numb = 1 or numb = 0
    return

def play_the_game_again():
    play_again = input(' Do you want to try again (Y)es or (N): ').lower()
    if play_again == 'y':
        main()
    else:
        print('Thanks for trying the game. Any suggestions please email richardtbrownjr@gmail.com')
        exit()


def main():
    os.system('clear')
    print("                     Game of Sticks  ")
    print('*************************************************')
    pick_number_of_sticks()
    print('')
    #class New Class = []

    while True:
        player1
        play_round(numb)
        player2
        play_round(numb)
        if game_over(numb)
            break

    play_the_game_again()

if __name__ == '__main__':
    main()
