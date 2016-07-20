def play_round(numb):
#player_list = ['player 1',1,'player 2', 2]
    if turn_sticks_chosen = (int(input('How many sticks (1,2,or 3) do you want in this turn. ').lower())
        print numb - turn_sticks_chosen
        x = (x + 1)  % 2 ; x
        return
    #if turn_sticks_chosen = input('How many sticks (1,2,or 3) do you want in this turn. ').lower()

def pick_number_of_sticks(numb):
    numb = int(range(1, 100))
    #number_of_sticks = input('How many sticks do you want in this game. ').lower()
    #number_of_sticks = int(number_of_sticks)
    return numb

def play_the_game_again():
    play_again = input(' Do you want to try again (Y)es or (N): ').lower()
    if play_again == 'y':
        main()
    else:
        print('Thanks for trying the game. ')
        exit()

def main():
    os.system('clear')
    print("                     Game of Sticks  ")
    print('*************************************************')
    pick_number_of_sticks(numb)
    print('')
    class New Class = []

    while numb >= 3:
        print('')

        play_round(numb)


    if (player_2=1):
        print("Player 1 you win!")
    else:
        print("Player 1 you lose")
        print('Thanks for trying.')

    play_the_game_again()

if __name__ == '__main__':
    main()
