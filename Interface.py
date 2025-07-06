import Game
from Util import add_to_queue, add_list_to_queue, print_queue, input_with_queue
from Util import del_file, load_obj, get_save_names

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
        save_files_map = {str(ind+2) : save_files[ind] for ind in range(len(save_files))}
        save_files_list = ["(" + i + ") " + save_files_map[i] for i in save_files_map]

       # Add save files to print queue
        add_to_queue(q, 'Save files:\n(1) New Game\n')
        add_list_to_queue(q, save_files_list)

        # Take in input for each file name 
        choice_save = input_with_queue(q, '\nChoose a Save File: ')
        save_name = None
        if choice_save in save_files_map:
            save_name = save_files_map[choice_save]
        elif choice_save in save_files_map.values():
            save_name = choice_save

        if save_name != None:
            add_to_queue(q, 'Save: {}\n\n'.format(save_name) + '--'*30 + '\nOptions:\nPlay\nDelete')

            # For chosen file, take action to either play or it delete it
            file_action = input_with_queue(q, 'What would you like to do? ').lower()
            if file_action in ['delete', 'd']:
                del_file(save_name)
            # If chosen file is not new, then load the file and use for the game
            elif file_action in ['play', 'p']:      
                player_data = load_obj(save_name)
                player_name = save_name
                break

        # If new file, then play game from beginning
        elif choice_save.lower() in ['new', 'n', '1']:
            add_to_queue(q, "This dungeon is filled with, like, monsters and shit, " + 
                "you have to kill them! I hope you're ready, because that's the only way out.")
            input_with_queue(q, 'Press enter to continue: ')
            player_name = input_with_queue(q, "Anyways, what's your name? ")
            break
        else:
            add_to_queue(q, "Choose an available option\n")

    
    input_with_queue(q, "Alright {}, we\'re all counting on you! Who knows, you may even find some cool things along the way...".format(player_name))
    return player_name, player_data

if __name__ == "__main__":
    player_name, save_data = game_intro()
    g = Game.Game(player_name, save_dict=save_data)
    q = []

    # Ask the player to start the game, and play if they say yes
    while True:
        start = input_with_queue(q, "Do you wish to proceed? (y/n) ").lower()
        if start in ['no', 'n', 'exit', 'e']:
            add_to_queue(q, "You're no fun :(")
            print_queue(q)
            break
        if start not in ['yes', 'y']:
            add_to_queue(q, "That wasn't an option, dummy!")
            print_queue(q)
        if start in ['yes', 'y']:
            g.play()
            break