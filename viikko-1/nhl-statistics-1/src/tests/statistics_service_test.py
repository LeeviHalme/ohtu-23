import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
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
