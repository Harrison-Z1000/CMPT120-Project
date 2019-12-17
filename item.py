class Item:
    def __init__(self, name, description, uses):
        # Includes all info about an item
        self.name = name
        self.description = description
        self.uses = uses

    def get_item(itemIndex):
        # Returns the requested item as an object
        return item_list[itemIndex]


# Instantiates each item


item_list = [Item("Sword", "A medium-length sword you found in "
                           "Vindauga.", 1000),
             Item("Shield", "A light, yet sturdy shield you found in "
                            "Vindauga.", 1000),
             Item("Berries", "Tart, red berries that you and Svend picked "
                             "from bushes.", 1),
             Item("Flask", "An empty flask that you and Svend discovered by a "
                           "creek.", 20)]
