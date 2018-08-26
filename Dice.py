import random as r


class Dice:
    """Describes a handful of dice."""

    # Look, I like abstractions okay? Fuck you. Fuck this. I quit.
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
