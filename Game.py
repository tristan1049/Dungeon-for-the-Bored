import Player
import Floor
import Fight
import time
from Util import save_obj
from Util import add_to_queue, print_queue


class Game(object):
    """Creates a dice battle game for a player"""
    def __init__(self, player_name: str, num_floors: int=10, save_dict: dict=None):
        """
        Inputs:
            player_name: String representation of player's input name
            num_floors: Integer of the number of floors in the Game, defaults to 5
            save_dict: A dictionary of a player's items, statuses, and attributes
            from a save file
        Purpose: To initialize a dice battle game
        """
        if save_dict == None:
            self.player = Player.Player(player_name) 
            self.player.add_dice(2) 
            if player_name == "dev":
                self.player.add_dice(8)

        else:
            self.player = save_dict['player']
        
        self.status = 'ongoing'
        self.floor = None
        self.num_floors = num_floors
        self.level = 0
        self.q = []
        
    def is_ongoing(self):
        """
        Purpose: To check that the game is still ongoing
        Output: Boolean of whether status of game is ongoing
        """
        return self.status == 'ongoing'
    
    def get_status(self):
        """
        Purpose: To get the status of the game
        Output: String representation of the status of the game
        """
        return self.status
    
    def get_player(self):
        """
        Purpose: To get the player
        Output: The player object
        """
        return self.player
    
    def get_floor(self):
        """
        Purpose: To get the floor currently on
        Output: The floor object
        """
        return self.floor
        
    def change_status(self, change):
        """
        Inputs:
            change: Change to the status of the game
        Purpose: To stop, pause, extend, or end the game status
        """
        self.status = change
        
    def next_floor(self):
        """
        Purpose: To make the next floor for the player and start the fight
        """
        self.level += 1
        self.floor = Floor.get_floor(self.level)
        
        # Add a die to the player's dice upon beating first boss
        if self.level == 6 and len(self.player.Dice) == 2:
            self.player.add_dice(1)

        # Create a fight instance for the next floor and start the battle
        f = Fight.Fight(self.floor, self.player, self.floor.get_enemy())
        result = f.battle()
        
        # Get the result from the battle and either end the game or move forward
        if result == 'lost':
            self.status = 'lost'
            self.player.restart()
        elif result == 'ran':
            self.status = 'ran'
            self.player.restart()
        elif self.level >= self.num_floors:
            self.status = 'won'

    def play(self):
        """
        Purpose: To start and maintain the state of the game
        """
        # If game is ongoing, head to next floor
        while self.is_ongoing():
            self.next_floor()
            if self.get_status() == 'won':
                add_to_queue(self.q, "You beat the dungeon!! Great job!")
            elif self.get_status() == 'ran':
                add_to_queue(self.q, "You safely escape the dungeon with your life, and live to fight another day.")
            elif self.get_status() == 'lost':
                add_to_queue(self.q, 'Oh noo! You died!')
            print_queue(self.q)
            save_obj({'player': self.get_player()}, self.get_player().get_name())  
        time.sleep(2)