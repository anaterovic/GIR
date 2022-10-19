import unittest

from ir_exercise.test.utils import send_request


class HungerGamesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "12 districts fighting in a deathly game"
        self.gold = "The Hunger Games (film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class NoMoreBabiesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "no mas bebes"
        self.gold = "No más bebés"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class ItTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "It"
        self.gold = "It (2017 film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class FaultInOurStarsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "2014 american coming-of-age romance based on a novel"
        self.gold = "The Fault in Our Stars (film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class HiddenFiguresTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "documentary about women in STEM"
        self.gold = "Picture a Scientist"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


if __name__ == "__main__":
    unittest.main()
