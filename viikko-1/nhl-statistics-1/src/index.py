from statistics_service import StatisticsService
from player_reader import PlayerReader
from sortby import SortBy

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = StatisticsService(reader)
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    print("Philadelphia Flyers:")
    print()
    for player in philadelphia_flyers_players:
        print(player)

    # järjestetään kaikkien tehopisteiden eli maalit+syötöt perusteella
    print()
    print("Top point getters:")
    for player in stats.top(10, SortBy.POINTS):
        print(player)

    # metodi toimii samalla tavalla kuin yo. kutsu myös ilman toista parametria
    print()
    for player in stats.top(10):
        print(player)

    # järjestetään maalien perusteella
    print()
    print("Top point goal scorers:")
    for player in stats.top(10, SortBy.GOALS):
        print(player)

    # järjestetään syöttöjen perusteella
    print()
    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS):
        print(player)


if __name__ == "__main__":
    main()
