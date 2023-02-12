import json

class User(object):

    def __init__(self, user):
        self.display_name = user['display_name']
        self.user_id = user['id']
        self.following_playlists = []

    # Stampa il nome dell'utente e il relativo id
    def print(self):
        print("L'username di {:s} è {:s}".format(self.display_name, self.user_id))

    # Imposta delle playlist all'utente
    def set_following_playlists(self, playlists):
        json_p = json.dumps(playlists)
        playlist_json = json.loads(json_p)
        public_playlist_json = filter(lambda p: p.get('public') == True, playlist_json)
        self.following_playlists = list(public_playlist_json)

    # Ritorna le playlist dell'utente
    def get_following_playlists(self):
        return self.following_playlists


