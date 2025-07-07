import os
import platform
import sys
import pickle
from numpy.random import choice


def inp(s = ''):
    """For use with the game instead of input() function, compatible 
    with game inputs though system output flushing"""
    sys.stdout.flush()
    return input(s)

def get_save_names():
    """Gets the save files of the game"""
    path = os.getcwd() + '/Saves' 
    if not os.path.isdir(path):
        os.makedirs(path)
    save_files = os.listdir(path)
    return [i[:-4] for i in save_files if i.endswith('.pkl')]
    
def add_to_queue(queue, print_string):
    """Add string to print queue to show to user, returning queue"""
    queue.append(print_string)
    return queue

def add_list_to_queue(queue, print_list):
    """Add list of strings to print queue to show to user, returning queue"""
    queue += print_list
    return queue

def clear_queue(queue):
    """Clear the print queue, returning new queue"""
    queue.clear()
    return queue

def print_queue(queue, queue_clear=True, console_clear=True):
    """Print and clear the print queue, returning queue"""
    sys.stdout.flush()
    if (console_clear):
        if (platform.system() == "Windows"):
            os.system("cls")
        else:
            os.system("clear")
    if (len(queue) > 0):
        print("\n".join(queue))
    if queue_clear:
        queue.clear()
    return queue

def input_with_queue(queue, input_string, queue_clear=True, console_clear=True):
    """Print the print queue to the user with input message,
    and return the user input string"""
    print_queue(queue, queue_clear, console_clear)
    sys.stdout.flush()
    return input(input_string).strip()

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