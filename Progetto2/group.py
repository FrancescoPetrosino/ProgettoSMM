import pandas
import numpy
from user import User


class Group(object):

    def __init__(self):
        self.list = {}
        self.playlist_dataframe = pandas.DataFrame(columns=['user_id', 'user_display_name', 'playlist_id', 'playlist_name', 'playlist_description', 'playlist_uri', 'playlist_public', 'playlist_total_tracks'])
        self.playlist_tracks_dataframe = pandas.DataFrame(columns=['user_id', 'user_display_name', 'playlist_id', 'playlist_name', 'album_id', 'album_name', 'album_release_date', 'album_total_tracks', 'artist_id',
                                                                   'artist_name', 'track_disc_number', 'track_duration_ms', 'track_explicit', 'track_id', 'track_name', 'track_popularity'])
        self.artists_top_tracks = []
        self.albums_top_tracks = []
        self.top_tracks = []
        self.recommended_playlist = []

    # Aggiunge un nuovo user al gruppo
    def append(self, user: User):
        self.list[len(self.list)] = user

    # Ritorna il numero di utenti presenti in lista
    def count(self) -> int:
        return len(self.list.items())

    # Stampa le informazioni degli utenti del gruppo
    def print(self):
        print('Il gruppo è composto da: ')
        for user in self.list.values():
            print(user.display_name)

    # Ritorna l'utente del gruppo tramite indice
    def get_from_list(self, index: int) -> User:
        return self.list[index]

    def __by_display_name(self, user: User, display_name: str):
        return user.display_name == display_name

    # Ritorna un uitente tramite display_name
    def find(self, display_name: str) -> User:
        res = list(filter(lambda user: self.__by_display_name(user, display_name), self.list.values()))
        if len(res) > 0:
            return res[0]
        else:
            return None

    # Concateno con il dataframe di tutte le playlists del gruppo
    def append_to_playlist_dataframe(self, dataframe):
        self.playlist_dataframe = pandas.concat([self.playlist_dataframe, dataframe], ignore_index=True)

    # Ritorna il dataframe delle playlist del gruppo
    def get_playlist_dataframe(self):
        return self.playlist_dataframe

    # Concateno con il dataframe di tutte le tracks delle playlists del gruppo
    def append_to_playlist_tracks_dataframe(self, dataframe):
        self.playlist_tracks_dataframe = pandas.concat([self.playlist_tracks_dataframe, dataframe], ignore_index=True)

    # Ritorna il dataframe di tutte le tracks del gruppo
    def get_playlist_tracks_dataframe(self):
        return self.playlist_tracks_dataframe

    # Aggiunge una colonna al dataframe con la funzione di aggregazione sum
    def __append_sum_column(self, pivot_table: pandas.DataFrame) -> pandas.DataFrame:
        pivot_table = pivot_table.assign(Sum=pivot_table.sum(axis=1))
        return pivot_table.sort_values(by='Sum', ascending=False, inplace=False)

    # Crea una tabella pivot con il numero di volte in cui compare una track nelle playlist di un utente
    def create_tracks_pivot_table(self):
        self.tracks_pivot_table = pandas.pivot_table(self.playlist_tracks_dataframe, index=['track_id'], columns=['user_id'], values=['playlist_id'], aggfunc=pandas.Series.count, fill_value=0.0)
        self.tracks_pivot_table = self.__append_sum_column(self.tracks_pivot_table)

    # Crea una tabella pivot con il numero di volte in cui compare un album nelle tracks di un utente
    def create_albums_pivot_table(self):
        self.albums_pivot_table = pandas.pivot_table(self.playlist_tracks_dataframe, index=['album_id'], columns=['user_id'], values=['track_id'], aggfunc=pandas.Series.count, fill_value=0.0)
        self.albums_pivot_table = self.__append_sum_column(self.albums_pivot_table)

    # Crea una tabella pivot con il numero di volte in cui compare un artista nelle tracks di un utente
    def create_artists_pivot_table(self):
        self.artists_pivot_table = pandas.pivot_table(self.playlist_tracks_dataframe, index=['artist_id'], columns=['user_id'], values=['track_id'], aggfunc=pandas.Series.count, fill_value=0.0)
        self.artists_pivot_table = self.__append_sum_column(self.artists_pivot_table)

    # Ritorna la tabella pivot
    def get_tracks_pivot_table(self) -> pandas.DataFrame:
        return self.tracks_pivot_table

    # Ritorna la tabella pivot
    def get_albums_pivot_table(self) -> pandas.DataFrame:
        return self.albums_pivot_table

    # Ritorna la tabella pivot
    def get_artists_pivot_table(self) -> pandas.DataFrame:
        return self.artists_pivot_table

    # Aggiunge le tracks nella lista delle top tracks di un artista
    def append_to_artists_top_tracks(self, list):
        for item in list:
            self.artists_top_tracks.append(item)

    # Aggiunge le tracks nella lista delle top tracks di un album
    def append_to_albums_top_tracks(self, list):
        for item in list:
            self.albums_top_tracks.append(item)

    # Aggiunge la track nella lista delle top tracks generale
    def append_to_top_tracks(self, item):
        self.top_tracks.append(item)

    # Ritorna la lista delle top tracks di un artista
    def get_artists_top_tracks(self) -> list:
        return self.artists_top_tracks

    # Ritorna la lista delle top tracks di un album
    def get_albums_top_tracks(self) -> list:
        return self.albums_top_tracks

    # Ritorna la lista delle top tracks generale
    def get_top_tracks(self) -> list:
        return self.top_tracks

    # Aggiunge una track nella recommended playlist
    def append_to_recommend_playlist(self, item):
        for obj in self.recommended_playlist:
            if obj['track_id'] == item['track_id']:
                return
        self.recommended_playlist.append(item)

    # Ritorna la recommended playlist
    def get_recommended_playlist(self) -> list:
        return self.recommended_playlist
