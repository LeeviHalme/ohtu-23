import requests
from player import Player

class PlayerReader():
    def __init__(self, url):
        self.url = url
    
    def get_players(self):
        response = requests.get(self.url).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players
    
class PlayerStats():
    def __init__(self, reader: PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players = self.reader.get_players()
        players_by_nationality = filter(lambda player: player.nationality == nationality, players)
        return sorted(players_by_nationality, key=lambda player: player.goals + player.assists, reverse=True)

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print("Players from FIN:")
    print()

    for player in players:
        print(player)

if __name__ == "__main__":
    main()