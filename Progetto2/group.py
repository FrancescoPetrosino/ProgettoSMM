import pandas
from user import User


class Group(object):
    
    def __init__(self):
        self.list = {}
        self.playlist_dataframe = pandas.DataFrame(columns=['user_id', 'id', 'name', 'description', 'uri', 'public', 'total_tracks'])

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

    # Concateno con il dataframe del gruppo
    def append_to_playlist_dataframe(self, playlist_dataframe):
        self.playlist_dataframe = pandas.concat([self.playlist_dataframe, playlist_dataframe], ignore_index=True)

    # Get
    def get_playlist_dataframe(self):
        return self.playlist_dataframe
