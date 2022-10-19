import unittest

from ir_exercise.test.utils import send_request


class GladiatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "Russell Crowe in roman age"
        self.gold = "Gladiator (2000 film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class DunkirkTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "Oscar winning Christopher Nolan movie about 2nd world war"
        self.gold = "Dunkirk (2017 film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class FirstManTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "moon landing movie with Ryan Gostling"
        self.gold = "First Man (film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class TheMartianTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "an astronaut is left on the Mars, it was shot in Budapest"
        self.gold = "The Martian (film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class BeautifulMindTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "beautiful mi"
        self.gold = "A Beautiful Mind (film)"

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
