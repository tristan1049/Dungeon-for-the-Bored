import os
import time

import Game
from Util import c, inp, inp_clear
from Util import add_to_queue, add_list_to_queue, clear_queue, print_queue, input_with_queue
from Util import del_file, save_obj, load_obj, get_save_names

def game_intro():
    """
    Purpose: To print and take inputs for the game intro, which introduces the 
    player into the style of game and creates or uses a save file
    Output: The data from the save file chosen, if new is chosen then None
    """
    q = []
    player_name = ""
    player_data = None
    add_to_queue(q, 'Welcome to the Dice Dungeon!\n')
    
    while True:
        # Gets the string names of all save files
        save_files = get_save_names()            
       
       # Add save files to print queue
        add_to_queue(q, 'Save files:\nNew')
        add_list_to_queue(q, save_files)

        # Take in input for each file name 
        choice_save = input_with_queue(q, '\nChoose a Save File: ').strip()
        if choice_save in save_files:
            clear_queue(q)
            add_to_queue(q, 'Save: {}\n\n'.format(choice_save) + '--'*30 + '\nOptions:\nPlay\nDelete')

            # For chosen file, take action to either play or it delete it
            file_action = input_with_queue(q, 'What would you like to do? ').lower().strip()
            clear_queue(q)
            if file_action in ['delete', 'd']:
                del_file(choice_save)

            # If chosen file is not new, then load the file and use for the game
            elif file_action in ['play', 'p']:      
                player_data = load_obj(choice_save)
                player_name = choice_save
                break

        # If new file, then play game from beginning
        elif choice_save.lower() in ['new', 'n']:
            clear_queue(q)
            add_to_queue(q, "This dungeon is filled with, like, monsters and shit," + 
                "you have to kill them! I hope you're ready, because that's the only way out.")
            input_with_queue(q, 'Press enter to continue: ')
            clear_queue(q)
            player_name = input_with_queue(q, "Anyways, what's your name? ").strip()
            clear_queue(q)
            break

        else:
            clear_queue(q)
            add_to_queue(q, "Choose an available option\n")

    
    add_to_queue(q, "Alright {}, we\'re all counting on you! Who knows, you may even find some cool things along the way...".format(player_name))
    print_queue(q)
    clear_queue(q)
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