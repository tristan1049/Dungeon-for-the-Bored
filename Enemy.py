import Player
import Dice
import time
import Consumables as C
import Interface as I

     
        
class Enemy(Player.Player):
    """Creates an Enemy object, deriving from Player"""
        
    def __init__(self, name="Anon", HP=1):
        """
        Inputs:
            name: String representation of enemy's name, default to Anon
            HP: Integer representing Health Points, default to 20
        Purpose: To instantiate an adjustable class for an anonymous enemy
        """
        self.maxHP = HP
        self.HP = HP
        self.name = name
        self.Dice = [Dice.Dice()]
        self.status = 'alive'
        self.items = []
        
        
    
    
    def give_items(self, player):
        """
        Inputs:
            player: A player object for a player in the game
        Purpose: To give a player all the floor's items if they clear the floor
        """
        player.items += self.items
        
        print()
        time.sleep(1)
        for item in self.items:
            print('You got a {}!!'.format(item.get_name()))
    
    
    
    


class Rabid_Rabbit(Enemy):
    """Creates a Rabid Rabbit object, deriving from Enemy"""
    
    def __init__(self, name="Rabid Rabbit", HP=10):
        """
        Inputs:
            name: String representation of enemy's name, default to Rabid Rabbit
            HP: Integer representing Health Points, default to 10
        Purpose: To instantiate an adjustable class for a Rabid Rabbit enemy
        """
        super(Rabid_Rabbit, self).__init__(name, HP)
        
        poss_items = [C.Minor_HP_Potion(), C.HP_Potion(), C.Major_HP_Potion(), C.Rejuv_Potion(),
                      C.Minor_Damage_Scroll(), C.Damage_Scroll()]
        weights = [0.4, 0.2, 0.1, 0.1, 0.05, 0.03]
        
        self.items = I.choose_all(poss_items, weights)
    
    
    
    
class Wolf(Enemy):
    """Creates a Wolf object, deriving from Enemy"""
    
    def __init__(self, name="Wolf", HP=15):
        """
        Inputs:
            name: String representation of enemy's name, default to Wolf
            HP: Integer representing Health Points, default to 15
        Purpose: To instantiate an adjustable class for a Wolf enemy
        """
        super(Wolf, self).__init__(name, HP)
        
        poss_items = [C.Minor_HP_Potion(), C.HP_Potion(), C.Major_HP_Potion(), C.Full_HP_Potion(), C.Rejuv_Potion(),
                      C.Minor_Damage_Scroll(), C.Damage_Scroll(), C.Major_Damage_Scroll()]
        weights = [0.5, 0.25, 0.15, 0.03, 0.15, 0.1, 0.05, 0.01]
        
        self.items = I.choose_all(poss_items, weights)





class Goblin(Enemy):
    """Creates a Goblin object, deriving from Enemy"""
    
    def __init__(self, name="Goblin", HP=20):            
        """
        Inputs:
            name: String representation of enemy's name, default to Goblin
            HP: Integer representing Health Points, default to 20
        Purpose: To instantiate an adjustable class for a Goblin enemy
        """
        super(Goblin, self).__init__(name, HP)
        
        poss_items = [C.HP_Potion(), C.Major_HP_Potion(), C.Full_HP_Potion(), C.Rejuv_Potion(),
                      C.Minor_Damage_Scroll(), C.Damage_Scroll(), C.Major_Damage_Scroll()]
        weights = [0.4, 0.25, 0.05, 0.3, 0.15, 0.1, 0.05]
        
        self.items = I.choose_all(poss_items, weights)
        
        
    
        
class Venom_Spider(Enemy):
    """Creates a Venomous Spider object, deriving from Enemy"""
    
    def __init__(self, name="Venomous Spider", HP=30):            
        """
        Inputs:
            name: String representation of enemy's name, default to Venomous Spider
            HP: Integer representing Health Points, default to 30
        Purpose: To instantiate an adjustable class for a Venomous Spider enemy
        """
        super(Venom_Spider, self).__init__(name, HP)
        
        poss_items = [C.HP_Potion(), C.Major_HP_Potion(), C.Full_HP_Potion(), C.Rejuv_Potion(),
                      C.Minor_Damage_Scroll(), C.Damage_Scroll(), C.Major_Damage_Scroll()]
        weights = [0.6, 0.35, 0.1, 0.35, 0.2, 0.15, 0.08]
        
        self.items = I.choose_all(poss_items, weights)
        
        
        
class Assassin(Enemy):
    """Creates an Assassin object, deriving from Enemy"""
    
    def __init__(self, name="Assassin", HP=40):            
        """
        Inputs:
            name: String representation of enemy's name, default to Assassin
            HP: Integer representing Health Points, default to 30
        Purpose: To instantiate an adjustable class for a Assassin enemy
        """
        super(Assassin, self).__init__(name, HP)

        poss_items = [C.HP_Potion(), C.Major_HP_Potion(), C.Full_HP_Potion(), C.Rejuv_Potion(),
                      C.Damage_Scroll(), C.Major_Damage_Scroll()]
        weights = [0.7, 0.4, 0.15, 0.4, 0.2, 0.1]
        
        self.items = I.choose_all(poss_items, weights)



class Lost_Spirit(Enemy):
    """Creates a Lost Spirit object, deriving from Enemy"""
    
    def __init__(self, name="Lost Spirit", HP=50):            
        """
        Inputs:
            name: String representation of enemy's name, default to Lost Spirit
            HP: Integer representing Health Points, default to 50
        Purpose: To instantiate an adjustable class for a Lost Spirit enemy
        """
        super(Lost_Spirit, self).__init__(name, HP)
        
        poss_items = [C.Major_HP_Potion(), C.Full_HP_Potion(), C.Rejuv_Potion(),
                      C.Damage_Scroll(), C.Major_Damage_Scroll()]
        weights = [0.45, 0.2, 0.5, 0.25, 0.15]
        
        self.items = I.choose_all(poss_items, weights)















class Boss(Enemy):
    """Creates a Boss object, deriving from Enemy class"""
    
    def __init__(self, name="Anon", HP = 50):
        """
        Inputs:
            name:  The string name of the boss object
        Purpose: To create an instance of a boss enemy, a much more powerful enemy 
        with better items and drop rates
        """
        super(Boss, self).__init__(name, HP)
    
    
    
    
class Wolf_Pack(Boss):
    """Creates a Wolf Pack object, deriving from Boss class"""

    def __init__(self, name='Wolf Pack', HP = 50):
        """
        Inputs:
            name: Name of object, default to Wolf Pack
            HP: Health points of object, default to 50
        Purpose: To create an instance of a Wolf Pack boss object
        """
        super(Wolf_Pack, self).__init__(name, HP)
        self.add_dice(Dice.Dice())                                                          #Has low HP for boss, but 2 dice!
        
        poss_items = [C.HP_Potion(), C.Major_HP_Potion(), C.Full_HP_Potion(), C.Rejuv_Potion(),
                      C.Minor_Damage_Scroll(), C.Damage_Scroll(), C.Major_Damage_Scroll()]
        weights = [0.6, 0.4, 0.3, 0.4, 0.25, 0.2, 0.1]
        
        self.items = I.choose_all(poss_items, weights)


    
class Goblin_Mob(Boss):
    """Creates a Goblin Mob object, deriving from Boss class"""
    
    def __init__(self, name='Goblin Mob', HP=80):
        """
        Inputs:
            name: Name of object, default to Goblin Mob
            HP: Health points of object, default to 80
        Purpose: To create an instance of a Goblin Mob boss object
        """
        super(Goblin_Mob, self).__init__(name, HP)
        
        poss_items = [C.HP_Potion(), C.Major_HP_Potion(), C.Full_HP_Potion(), C.Rejuv_Potion(),
                      C.Minor_Damage_Scroll(), C.Damage_Scroll(), C.Major_Damage_Scroll()]
        weights = [0.6, 0.4, 0.3, 0.4, 0.25, 0.2, 0.1]
        
        self.items = I.choose_all(poss_items, weights)
        
        


class Head_Assassin(Boss):
    """Creates a Head Assassin object, deriving from Boss class"""
    
    def __init__(self, name='Head Assassin', HP = 100):
        """
        Inputs:
            name: Name of object, default to Head Assassin
            HP: Health points of object, default to 80
        Purpose: To create an instance of a Goblin Mob boss object
        """
        super(Head_Assassin, self).__init__(name, HP)
        self.add_dice(Dice.Dice())
        self.add_dice(Dice.Dice())
        
        poss_items = [C.Full_HP_Potion(), C.Rejuv_Potion(),
                      C.Damage_Scroll(), C.Major_Damage_Scroll()]
        weights = [0.5, 0.7, 0.5, 0.3]
        
        self.items = I.choose_all(poss_items, weights)




class Spider_Queen(Boss):
    """Creates a Spider Queen object, deriving from Boss class"""
    
    def __init__(self, name='Spider Queen', HP=150):
        """
        Inputs:
            name: Name of object, default to Spider Queen
            HP: Health points of object, default to 80
        Purpose: To create an instance of a Spider Queen boss object
        """
        super(Spider_Queen, self).__init__(name, HP)
        self.add_dice(Dice.Dice())
        
        poss_items = [C.Full_HP_Potion(), C.Rejuv_Potion(),
                      C.Damage_Scroll(), C.Major_Damage_Scroll()]
        weights = [0.5, 0.7, 0.5, 0.3]
        
        self.items = I.choose_all(poss_items, weights)
