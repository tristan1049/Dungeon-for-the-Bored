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
    with game inputs though system output flushing"""
    sys.stdout.flush()
    return input(s)

def inp_clear(s = ''):
    """For use with the game instead of input() function, compatible 
    with game inputs though system output flushing. Clears output after
    input is received"""
    sys.stdout.flush()
    rec = input(s)
    c()
    return rec

def get_saves():
    """Gets the save files of the game"""
    path = os.getcwd() + '/Saves' 
    if not os.path.isdir(path):
        os.makedirs(path)
    return os.listdir(path)
    
 
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
        ch = choice([obj_list[i], None], p=[weights[i], 1-weights[i]])
        if ch:
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