class FriendShips:
    def __init__(self, database=None):
        if database is None:
            self.friendships = {}
        else:
            self.friendships = database

    def create_person(self, person):
        if type(person) != str:
            raise TypeError('Person must be a string')
        else:
            self.friendships[person] = []
            return person

    def add_friend(self, person, friend):
        if type(person) != str or type(friend) != str:
            raise TypeError('Both person and friend must be strings')
        elif person not in self.friendships or friend not in self.friendships:
            raise LookupError('No such people to add a friend')
        else:
            self.friendships[person].append(friend)
            return friend

    def get_friends_list(self, person):
        if type(person) != str:
            raise TypeError('Person must be a string')
        elif person not in self.friendships:
            raise LookupError('No such person to get their friends')
        else:
            return self.friendships[person]

    def are_friends(self, person1, person2):
        if type(person1) != str or type(person2) != str:
            raise TypeError('Both people must be strings')
        elif person2 not in self.friendships or person1 not in self.friendships:
            raise LookupError('No such people to check')
        else:
            return person1 in self.friendships[person2]

    def make_friends(self, person1, person2):
        self.add_friend(person1, person2)
        self.add_friend(person2, person1)
        return person1, person2
