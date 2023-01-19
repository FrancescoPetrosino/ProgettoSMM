class User(object):

    # def __init__(self, display_name, user_id):
    #     self.display_name = display_name
    #     self.user_id = user_id

    def __init__(self, user):
        self.display_name = user['display_name']
        self.user_id = user['id']

    def print(self):
        print("L'username di {:s} è {:s}".format(self.display_name, self.user_id))

    def set_following_playlists(self, playlists):
        self.following_playlists = playlists

    def get_following_playlists(self):
        return self.following_playlists