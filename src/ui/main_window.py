import tkinter as tk
from tkinter import ttk
from src.models.character_model import DnD35Character

class SimpleCharacterApp:
    """Step 1: Create a basic window"""

    def __init__(self, root):
        self.root = root
        self.root.title("Character Manager")
        self.root.geometry("400x300")

        # Create our character
        self.character = DnD35Character()

        # Build the interface
        self.create_widgets()

    def create_widgets(self):
        """Step 2: Add widgets to the window"""

        # Character Name
        ttk.Label(self.root, text="Character Name:").grid(
            row=0, column=0, padx=5, pady=5, sticky='e'
        )
        self.name_entry = ttk.Entry(self.root, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Strength
        ttk.Label(self.root, text="Strength:").grid(
            row=1, column=0, padx=5, pady=5, sticky='e'
        )
        self.str_entry = ttk.Entry(self.root, width=10)
        self.str_entry.grid(row=1, column=1, padx=5, pady=5)

        # STR Modifier label (will update automaticially)
        ttk.Label(self.root, text="Modifier:").grid(
            row=1, column=2, padx=5, pady=5, sticky='e'
        )
        self.str_mod_label = ttk.Label(self.root, text=0, relief='sunken')
        self.str_mod_label.grid(row=1, column=3, padx=5, pady=5)

        # Bind event: When user types, update STR modifier
        self.str_entry.bind('<KeyRelease>', self.update_str_modifier)

        # Dexterity
        ttk.Label(self.root, text="Dexterity:").grid(
            row=2, column=0, padx=5, pady=5, sticky='e'
        )
        self.dex_entry = ttk.Entry(self.root, width=10)
        self.dex_entry.grid(row=2, column=1, padx=5, pady=5)

        # DEX Modifier label (will update automaticially)
        ttk.Label(self.root, text="Modifier:").grid(
            row=2, column=2, padx=5, pady=5, sticky='e'
        )
        self.dex_mod_label = ttk.Label(self.root, text=0, relief='sunken')
        self.dex_mod_label.grid(row=2, column=3, padx=5, pady=5)

        # Bind event: When user types, update STR modifier
        self.dex_entry.bind('<KeyRelease>', self.update_dex_modifier)

        # Save button
        ttk.Button(
            self.root
            , text="Save Character"
            , command=self.save_character
        ).grid(row=8, column=0, columnspan=4, pady=20)

    def update_str_modifier(self, event=None):
        """Step 3: Update modifier when strength changes"""
        try:
            # Get value from entry field
            strength = int(self.str_entry.get())
            # Update Character
            self.character.abilities['Strength'] = strength
            # Calulate Modifier
            modifier = self.character.get_ability_modifier('Strength')
            # Update Label
            self.str_mod_label.config(text=str(modifier))
        except ValueError:
            # User typed Non-Number, ignore
            pass

    def update_dex_modifier(self, event=None):
        """Step 3: Update modifier when dex changes"""
        try:
            # Get value from entry field
            dex = int(self.dex_entry.get())
            # Update Character
            self.character.abilities['Dexterity'] = dex
            # Calulate Modifier
            modifier = self.character.get_ability_modifier('Dexterity')
            # Update Label
            self.dex_mod_label.config(text=str(modifier))
        except ValueError:
            # User typed Non-Number, ignore
            pass
    
    def save_character(self):
        """Step 4: Save character data"""
        # Get name from entry
        self.character.character_name = self.name_entry.get()

        print(f"Saved: {self.character.character_name}")
        print(f"Strength: {self.character.abilities['Strength']}")
        print(f"Dexterity: {self.character.abilities['Dexterity']}")

if __name__ == "__main__":
    root= tk.Tk()
    app = SimpleCharacterApp(root)
    root.mainloop()