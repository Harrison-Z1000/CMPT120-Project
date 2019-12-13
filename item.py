class Item:
    def __init__(self, name, description, uses):
        # Includes all info about an item
        self.name = name
        self.description = description
        self.uses = uses

# Instantiates each item
item_list = [Item("Sword", "A medium-length sword gifted to you by the "
                           "Vindaugan villager.", 1000),
             Item("Shield", "A light yet sturdy shield gifted to you by the "
                            "Vindaugan villager.", 1000),
             Item("Berries", "Tart, red berries that you and Svend picked "
                             "from bushes.", 1),
             Item("Flask", "An empty flask that you and Svend discovered by a "
                           "creek.", 10)]

    
