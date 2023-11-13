class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.team = dict["team"]
        self.assists = dict["assists"]
        self.goals = dict["goals"]
        self.penalties = dict["penalties"]
        self.games = dict["games"]
        self.nationality = dict["nationality"]
    
    def __str__(self):
        return f"{self.name + " " + self.nationality:25}{self.team:5}{self.goals:3}{" + ":3}{self.assists:3}{" = ":3}{self.goals + self.assists:3}"
