import pandas
import numpy
from user import User


class Group(object):
    
    def __init__(self):
        self.list = {}
        self.playlist_dataframe = pandas.DataFrame(columns=['user_id', 'user_display_name', 'playlist_id', 'playlist_name', 'playlist_description', 'playlist_uri', 'playlist_public', 'playlist_total_tracks'])
        self.playlist_tracks_dataframe = pandas.DataFrame(columns=['user_id', 'user_display_name', 'playlist_id', 'playlist_name', 'album_id', 'album_name', 'album_release_date', 'album_total_tracks', 'artist_id', 'artist_name', 'track_disc_number', 'track_duration_ms', 'track_explicit', 'track_id', 'track_name', 'track_popularity'])
        self.artists_top_tracks = []
        self.albums_top_tracks = []
        self.top_tracks = []
        self.recommended_playlist = []

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

    def __append_sum_column(self, pivot_table: pandas.DataFrame) -> pandas.DataFrame:
        pivot_table = pivot_table.assign(Sum=pivot_table.sum(axis=1))
        return pivot_table.sort_values(by='Sum', ascending=False, inplace=False)

    def create_tracks_pivot_table(self):
        self.tracks_pivot_table = pandas.pivot_table(self.playlist_tracks_dataframe, index=['track_id'], columns=['user_id'], values=['playlist_id'], aggfunc=pandas.Series.count, fill_value=0.0)
        self.tracks_pivot_table = self.__append_sum_column(self.tracks_pivot_table)

    def create_albums_pivot_table(self):
        self.albums_pivot_table = pandas.pivot_table(self.playlist_tracks_dataframe, index=['album_id'], columns=['user_id'], values=['track_id'], aggfunc=pandas.Series.count, fill_value=0.0)
        self.albums_pivot_table = self.__append_sum_column(self.albums_pivot_table)

    def create_artists_pivot_table(self):
        self.artists_pivot_table = pandas.pivot_table(self.playlist_tracks_dataframe, index=['artist_id'], columns=['user_id'], values=['track_id'], aggfunc=pandas.Series.count, fill_value=0.0)
        self.artists_pivot_table = self.__append_sum_column(self.artists_pivot_table)

    def get_tracks_pivot_table(self) -> pandas.DataFrame:
        return self.tracks_pivot_table

    def get_albums_pivot_table(self) -> pandas.DataFrame:
        return self.albums_pivot_table

    def get_artists_pivot_table(self) -> pandas.DataFrame:
        return self.artists_pivot_table

    def append_to_artists_top_tracks(self, list):
        for item in list:
            self.artists_top_tracks.append(item)

    def append_to_albums_top_tracks(self, list):
        for item in list:
            self.albums_top_tracks.append(item)

    def append_to_top_tracks(self, item):
        # for item in list:
        self.top_tracks.append(item)

    def get_artists_top_tracks(self) -> list:
        return self.artists_top_tracks

    def get_albums_top_tracks(self) -> list:
        return self.albums_top_tracks

    def get_top_tracks(self) -> list:
        return self.top_tracks
    
    def append_to_recommend_playlist(self, item):
        for obj in self.recommended_playlist:
            if obj['track_id'] == item['track_id']:
                return
        self.recommended_playlist.append(item)

    def get_recommended_playlist(self) -> list:
        return self.recommended_playlist
