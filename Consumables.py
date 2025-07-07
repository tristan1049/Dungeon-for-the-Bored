import Player as Player
import Enemy as Enemy
import time


class Consumable(object):
    """Class for a consumable item for players in the game"""
    def __init__(self):
        """
        Purpose: To create a unique consumable
        """
        self.uses = 1
        self.name = ""
    
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
    
    def does_interact_with_enemies(self):
        """
        Purpose: To determine if item interacts with enemies
        Output: Boolean of whether item interacts with enemies
        """
        return False
    
    def __eq__(self, other):
        """
        Purpose: To provide a better way of equality checking for items
        Output: Boolean of whether other consumable properties match self
        """
        if not other:
            return False
        # If properties are the same, though they may not be
        # the same object instance, they are functionally equal and can
        # be interchanged when being used
        return (self.name == other.name) and (self.uses == other.uses)
    
class HPPotion(Consumable):
    """Creates a HP Potion from Consumable Class"""
    def __init__(self, HP_change: int=10):
        """
        Inputs:
            HP_change: Integer amount to heal the player's HP by
        Purpose: To create a Health Potion object
        """
        super().__init__()
        self.HP_change = HP_change
        self.name = 'HP Potion'
        
    def use(self, player: Player):
        """
        Inputs: 
            player: The player object
            enemy: Enemy object, default to None for potions
        Purpose: For a player to use the item
        q is not cleared
        """
        if self.can_use():
            prev_health = player.get_HP()
            player.healing(self.HP_change)
            self.uses -= 1

            print(f"You successfully used {self.name}")
            time.sleep(1)
            print(f"You healed for {player.get_HP() - prev_health} HP points!")
            time.sleep(2)
        
        if self.uses <= 0:
            player.remove_item(self)

    def __str__(self):
        """
        Purpose: To represent the object in string form
        """
        return(f"{self.name}: \n \nRestores the health of the player by {self.HP_change} HP \
               \nUses: 1 \nUsable in combat and out of combat.")

    
class MinorHPPotion(HPPotion):
    """Creates a minor health potion from the HP_Potion class"""
    def __init__(self, HP_change: int=5):
        """
        Inputs:
            HP_change: The HP that the player is to be healed up to
        Purpose: To create an instance of a minor HP Potion out of the HP_Potion class
        """
        super(MinorHPPotion, self).__init__(HP_change)
        self.name = 'Minor HP Potion'
        
    
class MajorHPPotion(HPPotion):
    """Creates a minor health potion from the HP_Potion class"""
    def __init__(self, HP_change: int=20):
        """
        Inputs:
            HP_change: The HP that the player is to be healed up to
        Purpose: To create an instance of a minor HP Potion out of the HP_Potion class
        """
        super(MajorHPPotion, self).__init__(HP_change)
        self.name = 'Major HP Potion'
        
    
class FullHPPotion(HPPotion):
    """Creates a full health potion from the HP_Potion class"""
    def __init__(self, HP_change: int=None):
        """
        Inputs: 
            HP_change: The HP that the player is healed, set to None since full heal
        Purpose: To create an instance of Full_HP_Potion out of HP_Potion class
        """
        super(FullHPPotion, self).__init__(HP_change)
        self.name = 'Full HP Potion'
          
    def use(self, player: Player):
        """
        Inputs:
            player: The player object
            enemy: Enemy object, default to None for potions
        Purpose: Redefine use function of class to fully heal player
        """
        if self.can_use():
            prev_health = player.get_HP()
            player.healing(player.get_maxHP())
            self.uses -= 1

            print(f"You successfully used {self.name}")
            time.sleep(1)
            print(f"You healed for {player.get_HP() - prev_health} HP points!")
            time.sleep(2)

        if self.uses <= 0:
            player.remove_item(self)

    def __str__(self):
        """
        Purpose: To represent the object in string form
        """
        return(f"{self.name}: \n \nRestores the health of the player fully \
               \nUses: 1 \nUsable in combat and out of combat.")
        
 
class RejuvPotion(HPPotion):
    """Creates an instance of a Rejuvenation Potion, originating from HP Potion class"""
    
    def __init__(self, HP_change: int=5):
        """
        Inputs: HP_change: Integer amount to heal the player per turn
        Purpose: To create an instance of a Rejuvenation potion, which heals
        the player a small amount for a certain amount of turns
        """
        super(RejuvPotion, self).__init__(HP_change)
        self.name = 'Rejuv Potion'
        self.turns = 5
        
    def use(self, player: Player):
        """
        Inputs:
            player: The player object
            enemy: Enemy object, default to None for potions
        Purpose: Redefine use function of class to heal player over turns
        """
        if self.can_use():
            self.uses -= 1
            player.status_effects.append(self)
            print(f"You successfully used {self.name}.")
            time.sleep(2)
        
        if self.uses <= 0:
            player.remove_item(self)

    def status_use(self, player: Player):
        """
        Inputs:
            player: The player object
            enemy: Enemy object, default to None for potions
        Purpose: To heal player over several turns, viewed as status effect
        """
        if self.turns > 0:
            prev_health = player.get_HP()
            player.healing(self.HP_change)
            self.turns -= 1
            print(f"You healed for {player.get_HP() - prev_health} HP points from {self.name}!")
        
        # If no turns left, remove status. Always remove immediately when status is gone
        if self.turns <= 0:
            player.remove_status(self)

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

    def __eq__(self, other):
        """
        Purpose: To provide a better way of equality checking for items
        Output: Boolean of whether other consumable properties match self
        """
        if not other:
            return False
        return (self.name == other.name) and (self.uses == other.uses) and (self.turns == other.turns)
            
    
class DmgScroll(Consumable):
    """Creates a Dmg Scroll object"""
    def __init__(self, damage: int=0):
        """
        Inputs:
            damage: Integer amount to damage the enemy by
        Purpose: To create a Dmg Scroll object
        """
        super().__init__()
        self.uses = 1
        self.name = 'Dmg Scroll'
        self.damage = damage
        
    def use(self, player: Player, enemy: Enemy=None):
        """
        Inputs:
            player: The player object
            enemy: The enemy object
        Purpose: To use the object to deal damage to enemy object
        """
        # Can't use damage scrolls outside of battle
        if not enemy:
            print("Can't use item outside of battle!")
            time.sleep(2)
            return
        if not enemy.is_alive():
            print("Can't use item outside of battle!")
            time.sleep(2)
            return

        # If in battle, use if there are uses left
        if self.can_use():
            prev_en_health = enemy.get_HP()
            enemy.damage(self.damage)
            self.uses -= 1
            
            print(f"You successfully used {self.name}\n")
            time.sleep(1)
            print(f"You hurt {enemy.get_name()} for {prev_en_health - enemy.get_HP()} damage!\n")
            time.sleep(2)
        
        if self.uses <= 0:
            player.remove_item(self)

    def does_interact_with_enemies(self):
        """
        Purpose: To determine if item interacts with enemies
        Output: Boolean of whether item interacts with enemies
        """
        return True

    def __str__(self):
        """
        Purpose: To represent the object in string form
        """
        return('{}: \n \nDeals {} amount of damage to an enemy \
               \nUses: 1 \nUsable in combat only.'.format(self.name, self.damage))
        
        
class MinorDamageScroll(DmgScroll):
    """Creates a Minor Damage Scroll object"""
    def __init__(self, damage: int=10):
        """
        Inputs:
            damage: Integer amount to damage the enemy by
        Purpose: To create a Minor Damage Scroll object
        """
        super(MinorDamageScroll, self).__init__(damage)
        self.name = 'Minor Damage Scroll'
        
        
class DamageScroll(DmgScroll):
    """Creates a Damage Scroll object"""
    def __init__(self, damage: int=15):
        """
        Inputs:
            damage: Integer amount to damage the enemy by
        Purpose: To create a Damage Scroll object
        """
        super(DamageScroll, self).__init__(damage)
        self.name = 'Damage Scroll'
        
        
class MajorDamageScroll(DmgScroll):
    """Creates a Major Damage Scroll object"""
    def __init__(self, damage: int=20):
        """
        Inputs:
            damage: Integer amount to damage the enemy by
        Purpose: To create a Major Damage Scroll object
        """
        super(MajorDamageScroll, self).__init__(damage)
        self.name = 'Major Damage Scroll'


class RabbitFoot(Consumable):
    """Creates a Rabbit Foot object"""
    def __init__(self):
        super().__init__()
        self.uses = 1
        self.battles = 1
        self.dice = 2
        self.name = "Rabbit's Foot"
        self.activated = False
        self.enemy = None

    def use(self, player: Player):
        """
        Inputs:
            player: The player object
            enemy: The enemy object
        Purpose: To use the object to temporarily increase the number 
        of dice for the player for 1 battle
        """
        if self.can_use():
            self.uses -= 1
            
            player.status_effects.append(self)
            player.add_dice(2)
            
            print(f"You successfully used {self.name}\n")
            time.sleep(1)
            print(f"You gained {self.dice} dice for this battle!\n")
            time.sleep(2)
        
        if self.uses <= 0:
            player.remove_item(self)

    def status_use(self, player: Player, enemy: Enemy=None):
        """
        Inputs:
            player: The player object
            enemy: Enemy object, default to None for potions
        Purpose: To maintain activation status and remove dice from player after use
        """
        # Activate if enemy present and not yet activated
        if enemy and not self.activated:
            self.activated = True
            self.enemy = enemy
            self.battles -= 1

        # Remove status effect if activated, given different enemy, and out of battles
        if self.activated and enemy != self.enemy:
            if self.battles <= 0:
                player.remove_dice(2)
                player.remove_status(self)
            else:
                self.battles -= 1

    def __str__(self):
        """
        Purpose: To represent the object in string form
        """
        return('{}: \n \nTemporarily increases the number of dice of the user by {}\
        \nfor the current or next battle. Usable in combat and out of combat'.format(self.name, self.dice))

    def __eq__(self, other):
        """
        Purpose: To provide a better way of equality checking for items
        Output: Boolean of whether other consumable properties match self
        """
        if not other:
            return False
        return (self.name == other.name) and (self.activated == other.activated) \
            and (self.uses == other.uses) and (self.battles == other.battles) and (self.enemy == other.enemy)