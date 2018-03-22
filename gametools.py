import random as r

class Dice:
    """Describes a handful of dice."""
    # We will probably want a more efficient way to resolve rolls, but 
    # for now it's nice to have the abstraction of a hand of dice.

    def __init__(self, d=6, n=0, name=''):
        self.name = name if (name != '') else 'Dice'
        if n > 0:
            d_key = str(d)
            self.hand = {d_key:n}
        elif n == 0:
            self.hand = {}
        else:
            print("You cannot have negative dice! No dice added to hand.")
            self.hand = {}
    
    def check(self):
        """Return whichever dice are currently in hand."""
        return self.hand
        
    def roll(self, d=0):
        """Roll dice currently in hand and return results."""
        rolls = {}
        if d != 0:
            d_key = str(d)
            v_list = []
            for i in range(self.hand(d_key)):
                roll = r.randint(1,d)
                v_list.append(roll)
            rolls[d_key] = v_list
        else:
            for d, n in self.hand.items():
                v_list = []
                for j in range(n):
                    roll = r.randint(0, int(d))
                    v_list.append(roll)
                rolls[d] = v_list
        return rolls

    def drop(self):
        """Drop all dice from hand."""
        self.hand = {}
    
    def grab(self, d, n):
        """Add n dice of type d to hand."""
        dn = str(d)
        self.hand[dn] = n if dn not in self.hand else self.hand[dn] + n
   
    def rename(self, name):
        """Change the name of this hand of dice."""
        self.name = name

class FloorPlan:
    """Describes a room's dimensions"""
    # Seems to be that this only supports rectangles at the moment.
    def __init__(self, plan):
        self.plan = plan
        self.x = plan[0].length()
        self.y = plan.length()
    
class Actor:
    """Generic actor for building map"""
    def __init___(self):
        self.solid = False

    def bump(self, whos_there):
        return self.solid

class Pile(Actor):
    """A pile of something."""
    def __init__(self, stuff):
        self.stuff = stuff
        self.solid = False

    def bump(self, whos_there):
        whos_there.add_item(stuff)

class Item:
    """An Item can be held in a Character or Pile's inventory"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
    # We'll need to have a good long chat about how we want Items to 
    # work:
    # Should Item be a barebones class that is extended by e.g. Weapon?
    # Should Item be used for ALL items with flags for item type?
    # Should Item have a generic Use method that is made more specific
    # for each derived class e.g. Weapon, Potion?

class Character(Actor):
    """Describes a character."""

    def __init__(self, name, status=[], abilities=[], skills=[],
                 equipment = [], inventory={}, spellbook=[]):
        self.name = name
        self.status = status
        self.abilities = abilities
        self.skills = skills
        self.inventory = inventory
        self.spellbook = spellbook
        self.solid = True
    
    # EXAMPLE
    # name = 'Name McNameFace'
    # status = [health, max_health, level, exp]           [int]
    # abilities = [str, dex, con, int, wis, cha]          [int]
    # skills = [acr, ani han, arc, ..., ste, sur]         [bool]
    # equipment = [armor, hat, shoes, gloves, 
    #              ring1, ring2, ..., necklace, 
    #              left_hand, right_hand]                 [Item] 
    # inventory = [potion_heal_a, pen, paper, quest_item] [Item]
    # spellbook = [fireball, healing, ... ]               [Spell]

    def show_summary(self):
        """Print all info about Character."""
        print(self.name)
        print('\nStatus: ')
        for stat, val in self.status.items():
            print(stat + ': ' + str(val))
        print('\nAbilities: ')
        for ab, val in self.abilities.items():
            print(ab + ': ' + str(val))
        print('\nInventory: ')
        for name, stuff in self.inventory.items():
            print(name + ': ' + str(self.inventory[name]['quantity']) 
                       + ', worth: ' 
                       + str(self.inventory[name]['total_value']))
        print('\nSpellbook: ')
        for spell in self.spellbook.keys():
            print(spell)

    def item_details(self, item_name):
        """Print the details of an item in character's inventory."""
        if item_name in self.inventory:
            print(item_name + ': ' + self.inventory[item_name])
        else:
            print('No item by that name in inventory!')
    
    def show_inventory(self):
        """Print a detailed inventory list."""
        print('Inventory: \n')
        for name, stuff in self.inventory.items():
            print(name)
            print('Quantity: ' + str(self.inventory[name]['quantity']))
            print('Description: ' + self.inventory[name]['description'])
            if self.inventory[name]['quantity'] > 1:
                print('Value: ' + str(self.inventory[name]['value']))
            print('Total Value: ' 
                  + str(self.inventory[name]['total_value']) + '\n' )
        print()

    def add_item(self, name, quantity, description='', value_per=0):
        """Add a type of item to the inventory."""
        if name in self.inventory.keys():
            self.inventory[name]['quantity'] +=  quantity
            new_value = quantity * self.inventory[name]['value']
            self.inventory[name]['total_value'] += new_value
        else:
            self.inventory[name] = {'quantity' : quantity, 
                                    'description' : description, 
                                    'value' : value_per, 
                                    'total_value': value_per * quantity}
    
    def drop_item(self, name, quantity):
        """Remove some or all of one item from the inventory."""
        if name in self.inventory.keys():
            quant_in = self.inventory[name]['quantity']
            if quant_in > quantity:
                new_quant = quant_in - quantity
                new_val = new_quant * self.inventory[name]['value']
                self.inventory[name]['quantity'] = new_quant
                self.inventory[name]['total_value'] = new_val
            else:
                del self.inventory[name]
        else:
            print('No item by that name in inventory!')


class Encounter:
    """Describes the geography of an encounter."""
    
    def __init__(self, area, atlas={}, people={}, symbols={}):
        self.atlas = atlas
        self.people = people 
        self.symbols = symbols 
        self.X = area[0]
        self.Y = area[1]

    def add_character(self, name, character, symbol, position):
        """Add a character to the encounter."""
        self.atlas[name] = position
        self.people[name] = character
        self.symbols[name] = symbol

    def move_character(self, name, position):
        """Change the position of the character."""
        self.atlas[name] = position

    def remove_character(self, name):
        """Remove a charcter from the encounter."""
        del self.atlas[name]
        del self.people[name]
        del self.symbols[name]

    def draw(self):
        """Draw a rough map of the characters in the encounter."""
        for i in range(self.Y):
            for j in range(self.X):
                someone_here = False
                who = '.'
                for a, b in self.atlas.items():
                    if [j, i] == b:
                        someone_here = True
                        who = self.symbols[a]
                print(who, end='')
            print('')
