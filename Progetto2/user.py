import json

class User(object):

    def __init__(self, user):
        self.display_name = user['display_name']
        self.user_id = user['id']

    def print(self):
        print("L'username di {:s} è {:s}".format(self.display_name, self.user_id))

    def set_following_playlists(self, playlists):
        json_p = json.dumps(playlists)
        playlist_json = json.loads(json_p)
        self.following_playlists = playlist_json

    def get_following_playlists(self):
        return self.following_playlists