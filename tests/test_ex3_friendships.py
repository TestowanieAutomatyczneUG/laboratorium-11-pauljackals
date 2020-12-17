import unittest
from src.ex3_friendships.friendships import FriendShips


class TestFriendships(unittest.TestCase):
    def setUp(self):
        database = {
            "Miotk": ["Kowalski", "Nowak", "Bobkowska"],
            "Kowalski": ["Miotk"],
            "Nowak": ["Miotk"],
            "Bobkowska": ["Miotk"],
            "Test": []
        }
        self.friendships = FriendShips(database=database)

    def test_create_person(self):
        person = "Bing"
        self.assertEqual(self.friendships.create_person(person), person)

    def test_create_person_wrong_type(self):
        with self.assertRaisesRegex(TypeError, "^Person must be a string$"):
            self.friendships.create_person(545)

    def test_add_friend(self):
        friend = "Nowak"
        self.assertEqual(self.friendships.add_friend("Test", friend), friend)

    def test_add_friend_wrong_type(self):
        with self.assertRaisesRegex(TypeError, "^Both person and friend must be strings$"):
            self.friendships.add_friend("Test", 546)

    def test_add_friend_no_person(self):
        with self.assertRaisesRegex(LookupError, "^No such people to add a friend$"):
            self.friendships.add_friend("Tes", "Pong")

    def test_get_friends_list(self):
        self.assertListEqual(self.friendships.get_friends_list("Miotk"), ["Kowalski", "Nowak", "Bobkowska"])

    def test_get_friends_list_empty(self):
        self.assertListEqual(self.friendships.get_friends_list("Test"), [])

    def test_get_friends_list_wrong_type(self):
        with self.assertRaisesRegex(TypeError, "^Person must be a string$"):
            self.friendships.get_friends_list(545)

    def test_get_friends_list_empty_no_person(self):
        with self.assertRaisesRegex(LookupError, "^No such person to get their friends$"):
            self.friendships.get_friends_list("Tes")

    def test_are_friends(self):
        self.assertTrue(self.friendships.are_friends("Nowak", "Miotk"))

    def test_are_friends_no(self):
        self.assertFalse(self.friendships.are_friends("Nowak", "Test"))

    def test_are_friends_wrong_type(self):
        with self.assertRaisesRegex(TypeError, "^Both people must be strings$"):
            self.friendships.are_friends(544, "Miotk")

    def test_are_friends_no_person2(self):
        with self.assertRaisesRegex(LookupError, "^No such people to check$"):
            self.friendships.are_friends("Nowak", "Tes")

    def test_are_friends_no_person1(self):
        with self.assertRaisesRegex(LookupError, "^No such people to check$"):
            self.friendships.are_friends("Nowa", "Test")

    def test_make_friends(self):
        people = "Nowak", "Test"
        self.assertTupleEqual(self.friendships.make_friends(*people), people)

    def tearDown(self):
        self.friendships = None


if __name__ == '__main__':
    unittest.main()
