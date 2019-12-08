class Player:
    def __init__(self, name, score, location, moves, inventory):
        # Includes all info about the player
        self.name = name
        self.score = score
        self.location = location
        self.moves = moves
        self.inventory = []

    def change_location(self, location, firstVisit, score):
        # This function handles changing the player's location and score
        # Player only gains points the first time they visit a location in the game
        if location == "VILLAGE" and firstVisit:
            self.location = "MOUNTAINS"
            self.score = score + 5
            return self
        elif location == "MOUNTAINS" and firstVisit:
            self.location = "FOREST"
            self.score = score + 5
            return self
        elif location == "FOREST" and firstVisit:
            self.location = "BUSHES"
            self.score = score + 5
            return self
        elif location == "BUSHES" and firstVisit:
            self.location = "CREEK"
            self.score = score + 5
            return self
        elif location == "CREEK" and firstVisit:
            self.location = "SETTLEMENT"
            self.score = score + 5
            return self
        elif location == "SETTLEMENT" and firstVisit:
            self.location = "BARNHOUSE"
            self.score = score + 5
            return self
        else:
            print("You have already been to this location. \n")
        return
