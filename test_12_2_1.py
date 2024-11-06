import unittest
from unittest import TestCase
from tests_12_2 import Tournament, Runner

class TournamentTest(TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)


    @classmethod
    def tearDownClass(cls):
        for name, result in cls.all_results.items():
            print(f'{name}')
            for key, value in result.items():
                print(f'\t{key}: {value}')

    def test_turn1(self):
        turn_1 = Tournament(90, self.runner1, self.runner3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == self.runner3.name)
        self.all_results['Test1'] = result

    def test_turn2(self):
        turn_2 = Tournament(90, self.runner2, self.runner3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == self.runner3.name)
        self.all_results['Test2'] = result

    def test_turn3(self):
        turn_3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == self.runner3.name)
        self.all_results['Test3'] = result

    if __name__ == '__main__':
        unittest.main()











