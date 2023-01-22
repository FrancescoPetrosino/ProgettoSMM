import json
import pandas
import retry
import spotipy as sp

def export_to_json(file_name, data):
	with open(file_name, 'w') as f:
		f.write(json.dumps(data, indent=4))

def export_to_csv(file_name, dataframe):
	dataframe.to_csv(file_name, sep=';', index=True)

def import_from_csv(file_name) -> pandas.DataFrame:
	return pandas.read_csv(file_name, sep=";")

@retry(tries=5, delay=5)
def playlist_items(playlist_id):
    return sp.playlist_items(playlist_id=playlist_id, limit=100)