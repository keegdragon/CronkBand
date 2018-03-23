import random as r


class Dice:
    """Describes a handful of dice."""
    # We will probably want a more efficient way to resolve rolls, but 
    # for now it's nice to have the abstraction of a hand of dice.

    def __init__(self, d=6, n=0, name=''):
        self.name = name if (name != '') else 'Dice'
        if n > 0:
            d_key = str(d)
            self.hand = {d_key: n}
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
    

class Item:
    """An Item can be held in a Character or Pile's inventory"""
    def __init__(self, name='', mass=0, description='', quantity=1):
        self.name = name
        self.mass = mass
        self.description = description
        self.quantity = quantity


class Spell(Item):
    """Spells are used from the inventory to cast magic. idk how yet """
    def use(self, logger):
        logger.do_magic()
        #We'll figure this out soon


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


class Character(Actor):
    """Describes a character.
    EXAMPLE
    name = 'Name McNameFace'
    status = [health, max_health, level, exp]           [int]
    abilities = [str, dex, con, int, wis, cha]          [int]
    skills = [acr, ani han, arc, ..., ste, sur]         [bool]
    equipment = [armor, hat, shoes, gloves,
                 ring1, ring2, ..., necklace,
                 left_hand, right_hand]                 [Item]
    inventory = [potion_heal_a, pen, paper, quest_item] [Item]
    spellbook = [fireball, healing, ... ]               [Spell]
    """

    def __init__(self,
                 name='',
                 status=[0, 0, 0, 0],
                 abilities=[0, 0, 0, 0, 0, 0],
                 skills=[False, False, False, False, False,
                         False, False, False, False, False,
                         False, False, False, False, False,
                         False, False, False],
                 equipment = [],
                 inventory=[],
                 spellbook=[]):
        self.name = name
        self.status = status
        self.abilities = abilities
        self.skills = skills
        self.equipment = equipment
        self.inventory = inventory
        self.spellbook = spellbook
        self.solid = True

    def show_summary(self):
        """Print all info about Character.
        Mostly just for development purposes, but could be used later.
        """
        status_list = ['Health', 'Max Health', 'Level', 'Experience']
        abilities_list = ['Strength', 'Dexterity', 'Constitution',
                          'Intelligence', 'Wisdom', 'Charisma']
        skills_list = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics',
                       'Deception', 'History', 'Insight', 'Intimidation',
                       'Investigation', 'Medicine', 'Nature', 'Perception',
                       'Performance', 'Persuasion', 'Religion',
                       'Sleight of Hand', 'Stealth', 'Survival']
        print(self.name)
        print('\nStatus: ')
        for stt in range(len(self.status)):
            print(status_list[stt] + ': ' + str(self.status[stt]))
        print('\nAbilities: ')
        for abl in range(len(self.abilities)):
            print(abilities_list[abl] + ': ' + str(self.abilities[abl]))
        print('\nSkills: ')
        for skl in range(len(self.skills)):
            if self.skills[skl]:
                print(skills_list[skl])
        print('\nEquipment:')
        for eqp in self.equipment:
            print(eqp.name)
        print('\nInventory:')
        for itm in self.inventory:
            print(itm.name + ' x' + str(itm.quantity))
        print('\nSpellbooks:')
        for spl in self.spellbook:
            print(spl.name)

    def show_inventory(self):
        """Print a detailed inventory list."""
        print('Inventory: \n')
        for itm in self.inventory:
            print(itm.name)
            print('Quantity: ' + str(itm.quantity))
            print('Description: ' + itm.description)
        print()

    def add_item(self, new_item):
        """Add an/many item/s to the inventory."""
        found = False
        for itm in self.inventory:
            if itm.name == new_item.name:
                itm.quantity += new_item.quantity
                found = True
                break
        if not found:
            self.inventory.append(new_item)
    
    def drop_item(self, name, quantity=1):
        """Remove some or all of one item from the inventory."""
        found = False
        for itm in self.inventory:
            if itm.name == name:
                if itm.quantity > quantity:
                    itm.quantity -= quantity
                else:
                    self.inventory.remove(itm)
                found = True
                break
        if not found:
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
