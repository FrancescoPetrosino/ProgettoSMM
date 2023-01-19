import json

def export_to_json(file_name, data):
	with open(file_name, 'w') as f:
		f.write(json.dumps(data, indent=4))

