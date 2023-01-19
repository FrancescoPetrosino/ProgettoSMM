from user import User


class Group(object):
    
    def __init__(self):
        self.list = {}

    # Append a new user to the list
    def append(self, user: User):
        self.list[len(self.list)] = user

    def count(self) -> int:
        return len(self.list.items())

    def get_from_list(self, index: int) -> User:
        return self.list[index]

    def __by_display_name(self, user: User, display_name: str):
        return user.display_name == display_name

    # Gets a user by display_name
    def find(self, display_name: str) -> User:
        res = list(filter(lambda user: self.__by_display_name(user, display_name), self.list.values()))
        if len(res) > 0:
            return res[0]
        else:
            return None
