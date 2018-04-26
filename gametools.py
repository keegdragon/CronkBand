import random as r


class Dice:
    """Describes a handful of dice."""

    # We will probably want a more efficient way to resolve rolls, but
    # for now it's nice to have the abstraction of a hand of dice.
    # Ha GAYYYY
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
                roll = r.randint(1, d)
                v_list.append(roll)
            rolls[d_key] = v_list
        else:
            for d, n in self.hand.items():
                v_list = []
                for j in range(n):
                    roll = r.randint(1, int(d))
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
        # We'll figure this out soon


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
        whos_there.add(self.stuff)


class Character(Actor):
    """Describes a player-character based on D&D character sheet."""

    def __init__(self, name, status=None, abilities=None, skills=None, 
                 equipment=None, inventory=None, spellbook=None):
        self.status_list = ['Health', 'Max Health', 'Level', 'Experience']
        self.abilities_list = ['Strength', 'Dexterity', 'Constitution',
                               'Intelligence', 'Wisdom', 'Charisma']
        self.skills_list = ['Acrobatics', 'Animal Handling', 'Arcana',
                            'Athletics', 'Deception', 'History', 'Insight',
                            'Intimidation', 'Investigation', 'Medicine',
                            'Nature', 'Perception', 'Performance',
                            'Persuasion', 'Religion', 'Sleight of Hand',
                            'Stealth', 'Survival']
        self.name = name
        self.status = (status if status is not None else [10, 10, 1, 0])
        self.abilities = (abilities if abilities is not None
                          else [8, 8, 8, 8, 8, 8])
        self.skills = (skills if skills is not None else [False, False, False,
                                                          False, False, False,
                                                          False, False, False,
                                                          False, False, False,
                                                          False, False, False,
                                                          False, False, False])
        self.equipment = (equipment if equipment is not None else [])
        self.inventory = (inventory if inventory is not None else [])
        self.spellbook = (spellbook if spellbook is not None else [])
        self.solid = True

    def show_summary(self):
        """Print all info about Character.
        Mostly just for development purposes, but could be used later.
        """
        print(self.name)
        print('\nStatus: ')
        for stt in range(len(self.status)):
            print(self.status_list[stt] + ': ' + str(self.status[stt]))
        print('\nAbilities: ')
        for abl in range(len(self.abilities)):
            print(self.abilities_list[abl] + ': ' + str(self.abilities[abl]))
        print('\nSkills: ')
        for skl in range(len(self.skills)):
            if self.skills[skl]:
                print(self.skills_list[skl])
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

    def add(self, new_item):
        """Add an/many item/s to the inventory."""
        found = False
        for itm in self.inventory:
            if itm.name == new_item.name:
                itm.quantity += new_item.quantity
                found = True
                break
        if not found:
            self.inventory.append(new_item)

    def drop(self, name, quantity=1):
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

    def equip(self, name):
        """Move an item from the inventory to the equipment."""
        found = False
        for itm in self.inventory:
            if itm.name.lower() == name.lower():
                self.equipment.append(itm)
                self.drop(itm.name)
                found = True
        print(('Item equipped' if found else 'No item by that name found.'))

    def unequip(self, name):
        """Move an item from the equipment to the inventory."""
        found = False
        for itm in self.equipment:
            if itm.name.lower() == name.lower():
                self.add(itm)
                self.equipment.remove(itm)
                found = True
        print(('Item unequipped' if found else 'No item by that name found.'))

    def toggle_skill(self, skill_name):
        """Toggle on or off a skill by name (case-insensitive)"""
        found = False
        real_skill_name = ''
        new_skill_state = False
        for skl in self.skills_list:
            if skl.lower() == skill_name.lower():
                found = True
                real_skill_name = skl
                skl_idx = self.skills_list.index(skl)
                self.skills[skl_idx] = not self.skills[skl_idx]
                new_skill_state = self.skills[skl_idx]
                break
        if not found:
            print('No skill of that name was found.')
        else:
            print(real_skill_name + ' was changed to ' + str(new_skill_state))


class Encounter:
    """Describes the geography of an encounter."""

    def __init__(self, area, atlas=None, people=None, symbols=None):
        self.atlas = (atlas if atlas is not None else {})
        self.people = (people if people is not None else {})
        self.symbols = (symbols if symbols is not None else {})
        self.X = area[0]
        self.Y = area[1]

    def add_character(self, character, position, name='', symbol='', ):
        """Add a character to the encounter."""
        if name == '':
            name = character.name
        if symbol == '':
            symbol = character.name.strip()[0].lower()
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

    def make_drawable(self):
        """Package the encounter to a drawable format for GameView"""
        drawable_env = []
        drawable_line = ""
        for i in range(self.Y):
            for j in range(self.X):
                someone_here = False
                who = '.'
                for a, b in self.atlas.items():
                    if [j, i] == b:
                        someone_here = True
                        who = self.symbols[a]
                drawable_line += who
            drawable_env.append(drawable_line)
        return drawable_env

    def draw(self):
        """Draw a rough map of the characters in the encounter."""
        for i in range(self.Y):
            for j in range(self.X):
                who = '.'
                for a, b in self.atlas.items():
                    if [j, i] == b:
                        who = self.symbols[a]
                print(who, end='')
            print('')
