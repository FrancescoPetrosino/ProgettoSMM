import json

def export_to_json(file_name, data):
	with open(file_name, 'w') as f:
		f.write(json.dumps(data, indent=4))

def export_to_csv(file_name, dataframe):
	dataframe.to_csv(file_name, sep=';', index=True)

