class DnD35Character:
    """Step 1: Define what data a character has"""

    def __init__(self):
        # Basic Info and Abilities
        self.character_name = ''
        self.player_name = ''
        self.race = ''
        self.character_class = ''

        # Ability Scores
        self.abilities = {
            'Strength': 10
            , 'Dexterity': 10
            , 'Constitution': 10
            , 'Intelligence': 10
            , 'Wisdom': 10
            , 'Charisma': 10
        }

        # Combat stats
        self.ac_armor_bonus = 0
        self.ac_shield_bonus = 0
        self.ac_natural_armor = 0
        self.size = "Medium"
    
    def get_ability_modifier(self, ability_name):
        """Step 2: Add calculation methods"""
        score = self.abilities.get(ability_name, 10)
        # Int division : 16 -> (16-10)//2 = 3)
        return (score - 10) // 2
    
    def get_size_modifier(self):
        """Calculate size modifier for AC and attacks"""
        size_mods = {
            'Fine': 8
            , 'Diminutive' : 4
            , 'Tiny' : 2
            , 'Small' : 1
            , 'Medium' : 0
            , 'Large' : -1
            , 'Huge' : -2
            , 'Gargantuan' : -4
            , 'Colossal' : -8
        }
        return size_mods.get(self.size, 0)
    
    def get_ac_total(self):
        """
        Calculate total Armor Class
        Formula: 10 + Armor + Shield + dex_mod + size_mod + natural + misc...
        """
        dex_mod = self.get_ability_modifier('Dexterity')
        size_mod = self.get_size_modifier()

        total = (10 +
                 self.ac_armor_bonus +
                 self.ac_shield_bonus +
                 dex_mod +
                 size_mod +
                 self.ac_natural_armor)
        
        return total
    
if __name__ == "__main__":
    # Create a character
    char = DnD35Character()
    char.character_name = "Test Hero"
    char.abilities['Strength'] = 16
    char.abilities['Dexterity'] = 14
    char.ac_armor_bonus = 4
    char.ac_shield_bonus = 2
    char.size = "Medium"

    ac = char.get_ac_total()

    # Calculate modifier
    str_mod = char.get_ability_modifier('Strength')
    print(f"Strength 16 has modifier: +{str_mod}")
    print(f"Total AC: {ac}")
