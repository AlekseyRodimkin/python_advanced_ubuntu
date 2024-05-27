import configparser
import json


config_obj = configparser.ConfigParser()
file = open('config.ini', 'r')
config_obj.read_file(file)
output_dict = dict()
dict_config = {}
sessions = config_obj.sections()
for session in sessions:
    item = config_obj.items(session)
    output_dict[session] = dict(item)
with open('dict_config.py', 'w') as file:
    file.write(f"dict_config = {json.dumps(output_dict, indent=4)}")
file.close()
