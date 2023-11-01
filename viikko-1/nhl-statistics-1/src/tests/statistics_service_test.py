import unittest
from statistics_service import StatisticsService
from player import Player
from sortby import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12), # 16
            Player("Lemieux", "PIT", 45, 54), # 99
            Player("Kurri",   "EDM", 37, 53), # 90
            Player("Yzerman", "DET", 42, 56), # 98
            Player("Gretzky", "EDM", 35, 89) # 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        reader_stub = PlayerReaderStub()
        self.service = StatisticsService(reader_stub)

    def test_search_exists(self):
        result = self.service.search("Semenko")

        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Semenko")
        self.assertEqual(result.team, "EDM")
        self.assertEqual(result.goals, 4)
        self.assertEqual(result.assists, 12)

    def test_search_not_exists(self):
        result = self.service.search("DoesNotExist")

        self.assertIsNone(result)

    def test_team(self):
        result = self.service.team("EDM")

        self.assertEqual(len(result), 3)

    def test_top(self):
        result = self.service.top(1)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Gretzky")

    def test_top_multiple(self):
        result = self.service.top(2)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Lemieux")
    
    def test_top_points(self):
        result = self.service.top(1, SortBy.POINTS)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Gretzky")
    
    def test_top_assists(self):
        result = self.service.top(1, SortBy.ASSISTS)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Gretzky")
    
    def test_top_goals(self):
        result = self.service.top(1, SortBy.GOALS)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Lemieux")
