class Player:
    def __init__(self, name, score, location, moves, inventory):
        # Includes all info about the player
        self.name = name
        self.score = score
        self.location = location
        self.moves = moves
        self.inventory = inventory

    def change_location(self, location, firstVisit, score):
        # Handles changing the player's location and score
        if location == location_list[0] and firstVisit:
            self.location = location_list[1]
            self.score = score + 5
            return self
        elif location == location_list[1] and firstVisit:
            self.location = location_list[2]
            self.score = score + 5
            return self
        elif location == location_list[2] and firstVisit:
            self.location = location_list[3]
            self.score = score + 5
            return self
        elif location == location_list[3] and firstVisit:
            self.location = location_list[4]
            self.score = score + 5
            return self
        elif location == location_list[4] and firstVisit:
            self.location = location_list[5]
            self.score = score + 5
            return self
        elif location == location_list[5] and firstVisit:
            self.location = location_list[6]
            self.score = score + 5
            return self
        elif location == location_list[6] and firstVisit:
            self.location = location_list[7]
            self.score = score + 5
            return self
        elif location == location_list[7] and firstVisit:
            self.score = score + 10
            return self
        else:
            # Player only gains points the first time they visit a location
            # and after they display its long description
            print("You have already been to this location. \n")
        return

    def moves_count(self, total_moves):
        # Keeps track of how many moves the player has made
        self.moves = total_moves + 1
        total_moves = self.moves
        return total_moves


location_list = ["MEADOW", "VILLAGE", "MOUNTAINS", "FOREST", "BUSHES", "CREEK",
                 "SETTLEMENT", "BARNHOUSE"]
