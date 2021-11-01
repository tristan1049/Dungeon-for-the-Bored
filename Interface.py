import os

import Game
from Util import c, inp, inp_clear
from Util import del_file, save_obj, load_obj, get_saves

def game_intro():
    """
    Purpose: To print and take inputs for the game intro, which introduces the 
    player into the style of game and creates or uses a save file
    Output: The data from the save file chosen, if new is chosen then None
    """
    c()
    print('Welcome to the Dice Dungeon!')
    print()
    
    while True:
        # Gets the string name of the folder with all save files in it
        Save_files = get_saves()        
        # For each file, check that it is a pickle file, and list as option if so                      
        Save_names = [i[:-4] for i in Save_files if i.endswith('.pkl')]       
       
        print('Save files:')
        print()
        print('New')
        for save in Save_names:           
            print(save)

        # Take in input for each file name 
        choice_save = inp_clear('Choose a Save File: ').strip() 
        if choice_save in Save_names:
            print('Save: {}'.format(choice_save)) 
            print()
            print('--'*30)
            print('Options:\nPlay \nDelete') 

            # For chosen file, take action to either play or it delete it
            File_Action = inp_clear('What would you like to do? ').lower().strip()
            if File_Action in ['delete', 'd']:
                del_file(choice_save)
            # If chosen file is not new, then load the file and use for the game
            elif File_Action in ['play', 'p']:      
                player_data = load_obj(choice_save)
                player_name = choice_save
                break

        # If new file, then play game from beginning
        elif choice_save.lower() in ['new', 'n']: 
            print("This dungeon is filled with, like, monsters and shit," + 
                "you have to kill them! I hope you're ready, because that's the only way out.")
            inp_clear('Press enter to continue: ')
            player_name = inp_clear("Anyways, what's your name? ").strip()
            player_data = None
            break
    
    print("Alright {}, we\'re all counting on you! Who knows, you may even find some cool things along the way...".format(player_name))
    return player_name, player_data

if __name__ == "__main__":
    player_name, save_data = game_intro()
    g = Game.Game(player_name, save_dict=save_data)

    # Ask the player to start the game, and play if they say yes
    while True:
        start = inp_clear('Do you wish to proceed? ').lower().strip()
        if start in ['no', 'n', 'exit', 'e']:
            print("You're no fun :(")
            break
        if start not in ['yes', 'y']:
            print("That wasn't an option, dummy!")
        if start in ['yes', 'y']:
            g.play()
            break