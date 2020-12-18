import unittest
from unittest.mock import MagicMock
from src.ex3_friendships.friendships import FriendShips
from src.ex3_friendships.friendships_database import FriendShipsDatabase
import copy


class TestFriendshipsDatabase(unittest.TestCase):
    def setUp(self):
        initial = {
            "Miotk": ["Kowalski", "Nowak", "Bobkowska"],
            "Kowalski": ["Miotk"],
            "Nowak": ["Miotk"],
            "Bobkowska": ["Miotk"],
            "Test": []
        }
        self.initial = initial
        self.friendships = FriendShips(initial=initial)

    def test_load_database(self):
        db_read = MagicMock()
        db_read.return_value = self.initial
        friendships_database = FriendShipsDatabase(None, db_read, None)
        self.assertTrue(friendships_database.load_database())

    def test_load_database_mock_call(self):
        db_read = MagicMock()
        db_read.return_value = self.initial
        friendships_database = FriendShipsDatabase(None, db_read, None)
        friendships_database.load_database()
        db_read.assert_called()

    def test_load_database_connection_error(self):
        db_read = MagicMock()
        db_read.side_effect = ConnectionError
        friendships_database = FriendShipsDatabase(None, db_read, None)
        with self.assertRaisesRegex(ConnectionError, "^Can't load the database$"):
            friendships_database.load_database()

    def test_create_person(self):
        person = "Bing"
        db_create = MagicMock()
        db_create.side_effect = (lambda x: x)
        friendships_database = FriendShipsDatabase(db_create, None, None)
        self.assertEqual(friendships_database.create_person(person), person)

    def test_create_person_mock_call(self):
        person = "Bing"
        db_create = MagicMock()
        db_create.side_effect = (lambda x: x)
        friendships_database = FriendShipsDatabase(db_create, None, None)
        friendships_database.create_person(person)
        db_create.assert_called_with(person)

    def test_create_person_connection_error(self):
        db_create = MagicMock()
        db_create.side_effect = ConnectionError
        friendships_database = FriendShipsDatabase(db_create, None, None)
        with self.assertRaisesRegex(ConnectionError, "^Can't create a resource in the database$"):
            friendships_database.create_person("XYZ")

    def test_make_friends(self):
        def db_update_function(x, y):
            temp = {}
            temp[x] = copy.deepcopy(self.initial[x])
            temp[x].append(y)
            temp[y] = copy.deepcopy(self.initial[y])
            temp[y].append(x)
            return temp

        db_update = MagicMock()
        db_update.side_effect = db_update_function
        friendships_database = FriendShipsDatabase(None, None, db_update, self.friendships)
        self.assertDictEqual(friendships_database.make_friends("Nowak", "Test"), {
            "Nowak": ["Miotk", "Test"],
            "Test": ["Nowak"]
        })

    def test_make_friends_mock_call(self):
        def db_update_function(x, y):
            temp = {}
            temp[x] = copy.deepcopy(self.initial[x])
            temp[x].append(y)
            temp[y] = copy.deepcopy(self.initial[y])
            temp[y].append(x)
            return temp

        db_update = MagicMock()
        db_update.side_effect = db_update_function
        friendships_database = FriendShipsDatabase(None, None, db_update, self.friendships)
        friendships_database.make_friends("Nowak", "Test")
        db_update.assert_called_with("Nowak", "Test")

    def test_make_friends_connection_error(self):
        db_update = MagicMock()
        db_update.side_effect = ConnectionError
        friendships_database = FriendShipsDatabase(None, None, db_update, self.friendships)
        with self.assertRaisesRegex(ConnectionError, "^Can't update the database$"):
            friendships_database.make_friends("Nowak", "Test")

    def test_get_friends_list(self):
        friendships_database = FriendShipsDatabase(None, None, None, self.friendships)
        self.assertListEqual(friendships_database.get_friends_list("Nowak"), ["Miotk"])

    def test_are_friends(self):
        friendships_database = FriendShipsDatabase(None, None, None, self.friendships)
        self.assertFalse(friendships_database.are_friends("Miotk", "Test"))

    def tearDown(self):
        self.friendships = None


if __name__ == '__main__':
    unittest.main()
