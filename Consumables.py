from Interface import c as c
import time




class Consumable(object):
    """Class for a consumable item for players in the game"""
    
    def __init__(self):
        """
        Purpose: To create a unique consumable
        """
        self.uses = 1
    
    
    def can_use(self):
        """
        Purpose: Determines if the item can be used
        Output: Boolean of whether item can be used
        """
        return self.uses > 0
    
    
    def get_name(self):
        """
        Purpose: To get the name of the object
        Output: String of the name of the object
        """
        return self.name
        
        
    
    
    

    
class HP_Potion(Consumable):
    """Creeates a HP Potion from Consumable Class"""
    
    def __init__(self, HP_change=10):
        """
        Inputs:
            HP_change: Integer amount to heal the player's HP by
        Purpose: To create a Health Potion object
        """
        self.uses = 1
        self.HP_change = HP_change
        self.name = 'HP Potion'
        
        
    def use(self, player, enemy=None):
        """
        Inputs: 
            player: The player object
            enemy: Enemy object, default to None for potions
        Purpose: For a player to use the item
        """
        prev_health = player.get_HP()
        
        player.healing(self.HP_change)
        self.uses -= 1
        c()
        print("You successfully used {}.".format(self.name))
        time.sleep(1)
        print("You healed for {} HP points!".format(player.get_HP() - prev_health))
        time.sleep(2)
        c()
    
        

    def __str__(self):
        """
        Purpose: To represent the object in string form
        """
        return('{}: \n \nRestores the health of the player by {} HP \
               \nUses: 1 \nUsable in combat and out of combat.'.format(self.name, self.HP_change))

    
    
    
        
class Minor_HP_Potion(HP_Potion):
    """Creates a minor health potion from the HP_Potion class"""
    
    def __init__(self, HP_change=5):
        """
        Inputs:
            HP_change: The HP that the player is to be healed up to
        Purpose: To create an instance of a minor HP Potion out of the HP_Potion class
        """
        super(Minor_HP_Potion, self).__init__(HP_change)
        self.name = 'Minor HP Potion'
        
        
    
class Major_HP_Potion(HP_Potion):
    """Creates a minor health potion from the HP_Potion class"""
    
    def __init__(self, HP_change=20):
        """
        Inputs:
            HP_change: The HP that the player is to be healed up to
        Purpose: To create an instance of a minor HP Potion out of the HP_Potion class
        """
        super(Major_HP_Potion, self).__init__(HP_change)
        self.name = 'Major HP Potion'
        
        

class Full_HP_Potion(HP_Potion):
    """Creates a full health potion from the HP_Potion class"""

    def __init__(self, HP_change=None):
        """
        Inputs: 
            HP_change: The HP that the player is healed, set to None since full heal
        Purpose: To create an instance of Full_HP_Potion out of HP_Potion class
        """
        super(Full_HP_Potion, self).__init__(HP_change)
        self.name = 'Full HP Potion'
        
        
    def use(self, player, enemy=None):
        """
        Inputs:
            player: The player object
            enemy: Enemy object, default to None for potions
        Purpose: Redefine use function of class to fully heal player
        """
        prev_health = player.get_HP()
        
        player.healing(player.get_maxHP())
        self.uses -= 1

        print("You successfully used {}.".format(self.name))
        time.sleep(1)
        print("You healed for {} HP points!".format(player.get_HP() - prev_health))
        time.sleep(2)
        c()


        
    def __str__(self):
        """
        Purpose: To represent the object in string form
        """
        return('{}: \n \nRestores the health of the player fully \
               \nUses: 1 \nUsable in combat and out of combat.'.format(self.name))
        
 
    


class Rejuv_Potion(HP_Potion):
    """Creates an instance of a Rejuvenation Potion, originating from HP Potion class"""
    
    def __init__(self, HP_change=5, turns=5):
        """
        Inputs: HP_change: Integer amount to heal the player per turn
        Purpose: To create an instance of a Rejuvenation potion, which heals
        the player a small amount for a certain amount of turns
        """
        super(Rejuv_Potion, self).__init__(HP_change)
        self.name = 'Rejuv Potion'
        
        self.turns = 5
        
        
        
    def use(self, player, enemy=None):
        """
        Inputs:
            player: The player object
            enemy: Enemy object, default to None for potions
        Purpose: Redefine use function of class to heal player over turns
        """
        prev_health = player.get_HP()
        player.healing(self.HP_change)
        self.turns -= 1
        self.uses -= 1
        
        player.status_effects.append(self)
        
        print("You successfully used {}.".format(self.name))
        time.sleep(1)
        print("You healed for {} HP points!".format(player.get_HP() - prev_health))
        time.sleep(2)
        c()



    def status_use(self, player, enemy=None):
        """
        Inputs:
            player: The player object
            enemy: Enemy object, default to None for potions
        Purpose: To heal player over several turns, viewed as status effect
        """
        prev_health = player.get_HP()
        player.healing(self.HP_change)
        self.turns -= 1
        

        print("You healed for {} HP points from {}!".format(player.get_HP() - prev_health, self.name))
        time.sleep(2)
        c()
        
        
    def get_turns(self):
        """
        Purpose: To get the number of turns on the status effect that are left
        Output: Integer of number of turns left on object
        """
        return self.turns
    
    
    def __str__(self):
        """
        Purpose: To represent the object in string form
        """
        return('{}: \n \nRestores the health of the player by {} for 5 turns \
               \nUses: 1 \nUsable in combat and out of combat.'.format(self.name, self.HP_change))
            
    
    
    
    






class Dmg_Scroll(Consumable):
    """Creates a Dmg Scroll object"""
    
    def __init__(self, damage=0):
        """
        Inputs:
            damage: Integer amount to damage the enemy by
        Purpose: To create a Dmg Scroll object
        """
        self.uses = 1
        self.name = 'Dmg Scroll'
        self.damage = damage
        
        
    def use(self, player, enemy):
        """
        Inputs:
            player: The player object
            enemy: The enemy object
        Purpose: To use the object to deal damage to enemy object
        """
        prev_en_health = enemy.get_HP()

        enemy.damage(self.damage)
        self.uses -= 1
        
        print("You successfully used {}.".format(self.name))
        time.sleep(1)
        print("You hurt {} for {} damage!".format(enemy.get_name(), enemy.get_HP() - prev_en_health))
        time.sleep(2)
        c()
        
        
    def __str__(self):
        """
        Purpose: To represent the object in string form
        """
        return('{}: \n \nDeals {} amount of damage to an enemy \
               \nUses: 1 \nUsable in combat only.'.format(self.name, self.damage))
        
        
        
        
        
class Minor_Damage_Scroll(Dmg_Scroll):
    """Creates a Minor Damage Scroll object"""
    
    def __init__(self, damage=10):
        """
        Inputs:
            damage: Integer amount to damage the enemy by
        Purpose: To create a Minor Damage Scroll object
        """
        super(Minor_Damage_Scroll, self).__init__(damage)
        self.name = 'Minor Damage Scroll'
        
        
        
class Damage_Scroll(Dmg_Scroll):
    """Creates a Damage Scroll object"""
    
    def __init__(self, damage=15):
        """
        Inputs:
            damage: Integer amount to damage the enemy by
        Purpose: To create a Damage Scroll object
        """
        super(Damage_Scroll, self).__init__(damage)
        self.name = 'Damage Scroll'
        
        
        
class Major_Damage_Scroll(Dmg_Scroll):
    """Creates a Major Damage Scroll object"""
    
    def __init__(self, damage=20):
        """
        Inputs:
            damage: Integer amount to damage the enemy by
        Purpose: To create a Major Damage Scroll object
        """
        super(Major_Damage_Scroll, self).__init__(damage)
        self.name = 'Major Damage Scroll'
    
