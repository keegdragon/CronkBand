class Item:
    """An Item can be held in a Character or Pile's inventory"""

    def __init__(self, name='', mass=0, description='', quantity=1):
        self.name = name
        self.mass = mass
        self.description = description
        self.quantity = quantity


class Actor:
    """Generic actor for building map"""

    def __init___(self):
        self.solid = False

    def bump(self, whos_there):
        return self.solid


class Pile(Actor):
    """A pile of something."""

    def __init__(self, stuff, name='Pile'):
        self.stuff = stuff
        self.solid = False
        self.symbol = '$'
        self.name = name

    def bump(self, whos_there):
        whos_there.add(self.stuff)
        return self.solid


class Character(Actor):
    """Describes a player-character based on D&D character sheet."""

    def __init__(self, name, symbol, status=None, abilities=None, skills=None,
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
        self.symbol = symbol
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
        print(self.name + ", " + self.symbol)
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

    def __init__(self, area):
        self.atlas = {}
        self.people = []
        self.game_board = []
        for i in range(area[0]):
            column = [None] * area[1]
            self.game_board.append(column)

    def add_character(self, character, position):
        """Add a character to the encounter."""
        if character not in self.people:
            self.atlas[character.name] = position
            self.people.append(character)
            if self.game_board[position[0]][position[1]] is None:
                self.game_board[position[0]][position[1]] = character
            else:
                print("Position (" + position[0] + ", " + position[1] + ") "
                      + "is occupied.")
        else:
            print("Character " + character.name + " is already in the "
                  + "encounter.")

    def move_character(self, character, position):
        """Change the position of the character."""
        old_position = self.atlas[character.name]
        self.game_board[old_position[0]][old_position[1]] = None
        self.atlas[character.name] = position
        self.game_board[position[0]][position[1]] = character

    def remove_character(self, character):
        """Remove a charcter from the encounter."""
        position = self.atlas[character.name]
        self.game_board[position[0]][position[1]] = None
        del self.atlas[character.name]
        self.people.remove(character)

    def name_at(self, x, y):
        """Return the name of the character at (x, y)."""
        return (self.game_board[x][y].name if self.game_board[x][y] is not None
                else None)

    def make_drawable(self):
        """Package the encounter to a drawable format for GameView"""
        drawable_env = []
        for column in self.game_board:
            drawable_line = ""
            for point in column:
                symbol = point.symbol if point is not None else '.'
                drawable_line += symbol
            drawable_env.append(drawable_line)
        return drawable_env

    def draw(self):
        """Draw a rough map of the characters in the encounter."""
        for column in self.game_board:
            for point in column:
                symbol = point.symbol if point is not None else '.'
                print(symbol, end='')
            print('')

    def player_to_front(self, player_name):
        """Make the player the 0th item in the list if they aren't already.
        Returns True iff the player was already at people[0]."""
        player = None
        found_player = False
        player_already_at_front = False
        for person in self.people:
            if person.name is player_name:
                player = person
                found_player = True
                break
        if found_player:
            player_already_at_front = True
            if self.people[0] is not player:
                player_already_at_front = False
                self.people.remove(player)
                self.people.insert(0, player)
        else:
            print("Player by that name not found.")
        return player_already_at_front
