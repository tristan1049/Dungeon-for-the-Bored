import Game
import os
import sys
import pickle
from numpy.random import choice


def c():
    """Shortcut for clearing the screen"""
    os.system('clear')
    print()


def inp(s = ''):
    """For use with the game instead of input() function, compatible 
    with game inputs and gets rid of bugs"""
    sys.stdout.flush()
    return input(s)


def choose_one(obj_list, weights):
    """
    Inputs:
        obj_list: A list of objects to choose from
        weights: A list of weights associated to object list
    Purpose: To choose one object out of list with given weights
    Output: Chosen object
    """
    return choice(obj_list, p=weights)

    
def choose_all(obj_list, weights):
    """
    Inputs:
        obj_list: A list of objects to choose from
        weights: A list of weights associated to object list
    Purpose: To choose each object out of list with given weights
    Output: List of chosen objects, if any
    """
    rv = []
    for i in range(len(obj_list)):
        ch = choice([obj_list[i], []], p=[weights[i], 1-weights[i]])
        
        if ch != []:
            rv.append(ch)
            
    return rv

    
    
    
def save_obj(obj, name):
    with open('Saves/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('Saves/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def del_file(file_name):
    os.remove('Saves/' + file_name + '.pkl')






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
        Save_files = os.listdir(os.getcwd() + '/Saves')                                         #Gets the string name of the folder with all save files in it
        Save_names = [i[:-4] for i in Save_files if i.endswith('.pkl')]                              #For each file, check that it is a pickle file, and list as option if so                                             
       
        
        print('Save files:')
        print()
        print('New')
        for save in Save_names:                                                                 #Print each file name as option
            print(save)
            
            
            
        choice_save = inp('Choose a Save File: ').strip()                                       #Take in input for each file name
        c()
        
        
        if choice_save in Save_names:
            print('Save: {}'.format(choice_save))                                                   #For chosen file, take action to either play or it delete it
            print()
            print('--'*30)
            print('Options:\nPlay \nDelete')                  
            File_Action = inp('What do you want to do? ').lower().strip()
            
            c()
            if File_Action == 'delete':
                del_file(choice_save)
                
            elif File_Action == 'play':                                             #If chosen file is not new, then load the file and use for the game
                player_data = load_obj(choice_save)
                player_name = choice_save
                break
    
    
        elif choice_save.lower() == 'new':                                                     #If new file, then play game from beginning
            player_data = None
            
            print("This dungeon is filled with, like, monsters and shit, \
you have to kill them! I hope you're ready, because that's the only way out.")
            inp('Press enter to continue: ')
            c()
    
            print("Anyways, what's your name? ")
            player_name = inp().strip()
            c()
            break
        


        
    save_obj({}, player_name)                                                           #and save new file under player's name
 
    print('Alright {}, we\'re all counting on you! Who knows, you may even find some \
cool things along the way...'.format(player_name))

    
    
    return player_name, player_data
        
        
        
        
        
        
        
        
        
    

if __name__ == "__main__":
    player_name, save_data = game_intro()
    
    g = Game.Game(player_name, save_dict=save_data)


    

    while True:
        start = inp('Do you wish to proceed? ').lower().strip()
        c()
        
        if start != 'no' and start != 'yes':
            
            print('That wasn\'t an option, dummy!')
        elif start == 'no' or start == 'exit':
            print("You're no fun :(")
            break
        else:
            break
    
    
    
    
    
    if start == 'yes':
        while g.is_ongoing():
            g.next_floor()                  #If game is ongoing, head to next floor

        if g.get_status() == 'won':
            print('You beat the dungeon!! Great job!')
        elif g.get_status == 'ran':
            print('You safely escape the dungeon with your life, and live to fight another day.')
    
    
        save_obj({'player': g.get_player()}, player_name)                                               #Save the game to the file 
