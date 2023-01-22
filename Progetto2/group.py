import pandas
from user import User


class Group(object):
    
    def __init__(self):
        self.list = {}
        self.playlist_dataframe = pandas.DataFrame(columns=['user_id', 'user_display_name', 'playlist_id', 'playlist_name', 'playlist_description', 'playlist_uri', 'playlist_public', 'playlist_total_tracks'])
        self.playlist_tracks_dataframe = pandas.DataFrame(columns=['user_id', 'user_display_name', 'playlist_id', 'playlist_name', 'album_id', 'album_name', 'album_release_date', 'album_total_tracks', 'artist_id', 'artist_name', 'track_disc_number', 'track_duration_ms', 'track_explicit', 'track_id', 'track_name', 'track_popularity'])

    # Append a new user to the list
    def append(self, user: User):
        self.list[len(self.list)] = user

    def count(self) -> int:
        return len(self.list.items())

    def print(self):
        print('Il gruppo è composto da: ')
        for user in self.list.values():
            print(user.display_name)

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
    def append_to_playlist_dataframe(self, dataframe):
        self.playlist_dataframe = pandas.concat([self.playlist_dataframe, dataframe], ignore_index=True)

    # Gets the playlists dataframe
    def get_playlist_dataframe(self):
        return self.playlist_dataframe

    # Concateno con il dataframe del gruppo
    def append_to_playlist_tracks_dataframe(self, dataframe):
        self.playlist_tracks_dataframe = pandas.concat([self.playlist_tracks_dataframe, dataframe], ignore_index=True)

    # Gets the playlists tracks dataframe
    def get_playlist_tracks_dataframe(self):
        return self.playlist_tracks_dataframe
