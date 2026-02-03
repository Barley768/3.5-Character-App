class DnD35Character:
    """Step 1: Define what data a character has"""

    def __init__(self):
        # Basic Info and Abilities
        self.character_name = ''
        self.player_name = ''
        self.race = ''
        self.size = "Medium"
        self.character_class = ''
        self.level = 1

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
        self.max_hp = 1
        self.current_hp = 1
        self.ac_armor_bonus = 0
        self.ac_shield_bonus = 0
        self.ac_natural_armor = 0
        self.base_attack_bonus = 1
    
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
    
    def get_initiative_mod(self):
        init_mod = self.get_ability_modifier('Dexterity')
        return init_mod
    
    def melee_attack_bonus(self):
        MAB = self.base_attack_bonus + self.get_ability_modifier('Strength') +self.get_size_modifier()

    
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
