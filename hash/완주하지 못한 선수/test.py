import unittest

from question import solution


class TestAlgorithm(unittest.TestCase):
    def test_solution(self):
        self.assertEqual("leo", solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
        self.assertEqual("vinko", solution(["marina", "josipa", "nikola", "vinko", "filipa"], 
        ["josipa", "filipa", "marina", "nikola"]))
        self.assertEqual("mislav", solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


if __name__ == "__main__":
    unittest.main()