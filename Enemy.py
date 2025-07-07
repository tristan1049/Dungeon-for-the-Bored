import Player
import Dice
import time
import Consumables as C
from Util import choose_all

        
class Enemy(Player.Player):
    """Creates an Enemy object, deriving from Player"""
    def __init__(self, name: str="Anon", HP: int=1, floor: int=1):
        """
        Inputs:
            name: String representation of enemy's name, default to Anon
            HP: Integer representing Health Points, default to 20
        Purpose: To instantiate an adjustable class for an anonymous enemy
        """
        super().__init__(name)
        self.Dice = [Dice.Dice()]
        self.floor = floor
        self.HP = HP
        self.maxHP = HP
        
    def give_items(self, player: Player):
        """
        Inputs:
            player: A player object for a player in the game
        Purpose: To give a player all the floor's items if they clear the floor
        """
        print()
        time.sleep(1)
        for item in self.items:
            player.add_item(item)
            print('You got a {}!!'.format(item.get_name()))
            time.sleep(.4)
        if (self.items):
            print()
        self.items = []
    
    def __eq__(self, other):
        """
        Purpose: To provide a better way of equality checking for items
        Output: Boolean of whether other enemy properties match self
        """
        if not other:
            return False
        return (self.name == other.name) and (self.HP == other.HP) and (self.maxHP == other.maxHP) \
            and (self.Dice == other.Dice) and (self.status == other.status) and (self.items == other.items) \
            and (self.exp == other.exp) and (self.floor == other.floor)

    def __ne__(self, other):
        """Provide false checking"""
        return not self.__eq__(other)
    
class RabidRabbit(Enemy):
    """Creates a Rabid Rabbit object, deriving from Enemy"""
    def __init__(self, name: str="Rabid Rabbit", HP: int=10, floor: int=1):
        """
        Inputs:
            name: String representation of enemy's name, default to Rabid Rabbit
            HP: Integer representing Health Points, default to 10
        Purpose: To instantiate an adjustable class for a Rabid Rabbit enemy
        """
        super(RabidRabbit, self).__init__(name, HP, floor)
        
        poss_items = [C.MinorHPPotion(), C.HPPotion(), C.MajorHPPotion(), C.RejuvPotion(),
                      C.MinorDamageScroll(), C.DamageScroll(), C.RabbitFoot()]
        weights = [0.4, 0.2, 0.1, 0.1, 0.05, 0.03, 0.03]
        
        self.items += choose_all(poss_items, weights)
        self.exp += 5
    
    
class Wolf(Enemy):
    """Creates a Wolf object, deriving from Enemy"""
    def __init__(self, name: str="Wolf", HP: int=15, floor: int=1):
        """
        Inputs:
            name: String representation of enemy's name, default to Wolf
            HP: Integer representing Health Points, default to 15
        Purpose: To instantiate an adjustable class for a Wolf enemy
        """
        super(Wolf, self).__init__(name, HP, floor)
        
        poss_items = [C.MinorHPPotion(), C.HPPotion(), C.MajorHPPotion(), C.FullHPPotion(), C.RejuvPotion(),
                      C.MinorDamageScroll(), C.DamageScroll(), C.MajorDamageScroll()]
        weights = [0.5, 0.25, 0.15, 0.03, 0.15, 0.1, 0.05, 0.01]
        
        self.items += choose_all(poss_items, weights)
        self.exp += 10


class Goblin(Enemy):
    """Creates a Goblin object, deriving from Enemy"""
    def __init__(self, name: str="Goblin", HP: int=20, floor: int=1):            
        """
        Inputs:
            name: String representation of enemy's name, default to Goblin
            HP: Integer representing Health Points, default to 20
        Purpose: To instantiate an adjustable class for a Goblin enemy
        """
        super(Goblin, self).__init__(name, HP, floor)
        
        poss_items = [C.HPPotion(), C.MajorHPPotion(), C.FullHPPotion(), C.RejuvPotion(),
                      C.MinorDamageScroll(), C.DamageScroll(), C.MajorDamageScroll()]
        weights = [0.4, 0.25, 0.05, 0.3, 0.15, 0.1, 0.05]
        
        self.items += choose_all(poss_items, weights)
        self.exp += 15
        
        
class VenomSpider(Enemy):
    """Creates a Venomous Spider object, deriving from Enemy"""
    def __init__(self, name: str="Venomous Spider", HP: int=30, floor: int=1):            
        """
        Inputs:
            name: String representation of enemy's name, default to Venomous Spider
            HP: Integer representing Health Points, default to 30
        Purpose: To instantiate an adjustable class for a Venomous Spider enemy
        """
        super(VenomSpider, self).__init__(name, HP, floor)
        
        poss_items = [C.HPPotion(), C.MajorHPPotion(), C.FullHPPotion(), C.RejuvPotion(),
                      C.MinorDamageScroll(), C.DamageScroll(), C.MajorDamageScroll()]
        weights = [0.6, 0.35, 0.1, 0.35, 0.2, 0.15, 0.08]
        
        self.items += choose_all(poss_items, weights)
        self.exp += 25
        
        
class Assassin(Enemy):
    """Creates an Assassin object, deriving from Enemy"""
    def __init__(self, name: str="Assassin", HP: int=40, floor: int=1):            
        """
        Inputs:
            name: String representation of enemy's name, default to Assassin
            HP: Integer representing Health Points, default to 30
        Purpose: To instantiate an adjustable class for a Assassin enemy
        """
        super(Assassin, self).__init__(name, HP, floor)
        self.add_dice(1)

        poss_items = [C.HPPotion(), C.MajorHPPotion(), C.FullHPPotion(), C.RejuvPotion(),
                      C.DamageScroll(), C.MajorDamageScroll()]
        weights = [0.7, 0.4, 0.15, 0.4, 0.2, 0.1]
        
        self.items += choose_all(poss_items, weights)
        self.exp += 35


class LostSpirit(Enemy):
    """Creates a Lost Spirit object, deriving from Enemy"""
    def __init__(self, name: str="Lost Spirit", HP: int=50, floor: int=1):            
        """
        Inputs:
            name: String representation of enemy's name, default to Lost Spirit
            HP: Integer representing Health Points, default to 50
        Purpose: To instantiate an adjustable class for a Lost Spirit enemy
        """
        super(LostSpirit, self).__init__(name, HP, floor)
        
        poss_items = [C.MajorHPPotion(), C.FullHPPotion(), C.RejuvPotion(),
                      C.DamageScroll(), C.MajorDamageScroll()]
        weights = [0.45, 0.2, 0.5, 0.25, 0.15]
        
        self.items += choose_all(poss_items, weights)
        self.exp += 45


# Base class for bosses
class Boss(Enemy):
    """Creates a Boss object, deriving from Enemy class"""
    def __init__(self, name: str="Anon", HP: int=50, floor: int=1):
        """
        Inputs:
            name:  The string name of the boss object
        Purpose: To create an instance of a boss enemy, a much more powerful enemy 
        with better items and drop rates
        """
        super(Boss, self).__init__(name, HP, floor)

    
class WolfPack(Boss):
    """Creates a Wolf Pack object, deriving from Boss class"""
    def __init__(self, name: str='Wolf Pack', HP: int=50, floor: int=1):
        """
        Inputs:
            name: Name of object, default to Wolf Pack
            HP: Health points of object, default to 50
        Purpose: To create an instance of a Wolf Pack boss object
        """
        super(WolfPack, self).__init__(name, HP, floor)
        self.add_dice(1)                                                          #Has low HP for boss, but 2 dice!
        
        poss_items = [C.HPPotion(), C.MajorHPPotion(), C.FullHPPotion(), C.RejuvPotion(),
                      C.MinorDamageScroll(), C.DamageScroll(), C.MajorDamageScroll()]
        weights = [0.6, 0.4, 0.3, 0.4, 0.25, 0.2, 0.1]
        
        self.items += choose_all(poss_items, weights)
        self.exp += 100


class GoblinMob(Boss):
    """Creates a Goblin Mob object, deriving from Boss class"""
    def __init__(self, name: str='Goblin Mob', HP: int=80, floor: int=1):
        """
        Inputs:
            name: Name of object, default to Goblin Mob
            HP: Health points of object, default to 80
        Purpose: To create an instance of a Goblin Mob boss object
        """
        super(GoblinMob, self).__init__(name, HP, floor)
        
        poss_items = [C.HPPotion(), C.MajorHPPotion(), C.FullHPPotion(), C.RejuvPotion(),
                      C.MinorDamageScroll(), C.DamageScroll(), C.MajorDamageScroll()]
        weights = [0.6, 0.4, 0.3, 0.4, 0.25, 0.2, 0.1]
        
        self.items += choose_all(poss_items, weights)
        self.exp += 100
        

class HeadAssassin(Boss):
    """Creates a Head Assassin object, deriving from Boss class"""
    def __init__(self, name: str='Head Assassin', HP: int=100, floor: int=1):
        """
        Inputs:
            name: Name of object, default to Head Assassin
            HP: Health points of object, default to 80
        Purpose: To create an instance of a Goblin Mob boss object
        """
        super(HeadAssassin, self).__init__(name, HP, floor)
        self.add_dice(2)
        
        poss_items = [C.FullHPPotion(), C.RejuvPotion(),
                      C.DamageScroll(), C.MajorDamageScroll()]
        weights = [0.5, 0.7, 0.5, 0.3]
        
        self.items += choose_all(poss_items, weights)
        self.exp += 250


class SpiderQueen(Boss):
    """Creates a Spider Queen object, deriving from Boss class"""
    def __init__(self, name: str='Spider Queen', HP: int=150, floor: int=1):
        """
        Inputs:
            name: Name of object, default to Spider Queen
            HP: Health points of object, default to 80
        Purpose: To create an instance of a Spider Queen boss object
        """
        super(SpiderQueen, self).__init__(name, HP, floor)
        self.add_dice(1)
        
        poss_items = [C.FullHPPotion(), C.RejuvPotion(),
                      C.DamageScroll(), C.MajorDamageScroll()]
        weights = [0.5, 0.7, 0.5, 0.3]
        
        self.items += choose_all(poss_items, weights)
        self.exp += 250