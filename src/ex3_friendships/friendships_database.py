from .friendships import FriendShips


class FriendShipsDatabase:
    def __init__(self, db_create, db_read, db_update, storage=None):
        if storage is None:
            self.storage = FriendShips()
        else:
            self.storage = storage
        self.db_create = db_create
        self.db_read = db_read
        self.db_update = db_update

    def load_database(self):
        try:
            data = self.db_read()
            for key in data:
                self.storage.create_person(key)
            for key, values in data.items():
                for value in values:
                    if not self.storage.are_friends(key, value):
                        self.storage.make_friends(key, value)
            return True
        except ConnectionError:
            raise ConnectionError("Can't load the database")

    def create_person(self, person):
        try:
            person_created = self.db_create(person)
            self.storage.create_person(person)
            return person_created
        except ConnectionError:
            raise ConnectionError("Can't create a resource in the database")

    def make_friends(self, person1, person2):
        try:
            people_created = self.db_update(person1, person2)
            self.storage.make_friends(person1, person2)
            return people_created
        except ConnectionError:
            raise ConnectionError("Can't update the database")

    def get_friends_list(self, person):
        return self.storage.get_friends_list(person)

    def are_friends(self, person1, person2):
        return self.storage.are_friends(person1, person2)
