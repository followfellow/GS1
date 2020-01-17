from time import sleep
from unittest import TestCase
from Caculator import Caculator

class TestCaculator(TestCase):
    def test_add(self):
        self.Caculator = Caculator()
        self.assertEqual(self.Caculator.add(3,4),7)

    def test_mutiply(self):
        sleep(0.1)
        self.fail()
