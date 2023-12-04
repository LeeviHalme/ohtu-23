class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def won_point(self):
        self.score += 1

    def get_score(self):
        return self.score

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = {
            "player1": Player(player1_name),
            "player2": Player(player2_name)
        }
        self.score_names = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        self.players[player_name].won_point()

    def get_score(self):
        player_1_score = self.players["player1"].get_score()
        player_2_score = self.players["player2"].get_score()

        # tasatilanteet
        if player_1_score == player_2_score:
            if player_1_score == 0:
                return "Love-All"
            elif player_1_score == 1:
                return "Fifteen-All"
            elif player_1_score == 2:
                return "Thirty-All"
            else:
                return "Deuce"
        # ei tasatilanne, jos jompikumpi on saavuttanut vähintään 4 pistettä
        elif player_1_score >= 4 or player_2_score >= 4:
            score_difference = player_1_score - player_2_score

            if score_difference == 1:
                return "Advantage player1"
            elif score_difference == -1:
                return "Advantage player2"
            elif score_difference >= 2:
                return "Win for player1"
            else:
                return "Win for player2"
        # ei tasatilanne, jos kumpikaan ei ole saavuttanut 4 pistettä
        else:
            return f"{self.score_names[player_1_score]}-{self.score_names[player_2_score]}"
