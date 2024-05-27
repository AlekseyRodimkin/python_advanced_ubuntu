import configparser
from d_config import dict_config


file = open('new_conf.ini', 'w')
config_obj = configparser.ConfigParser()
for section, options in dict_config.items():
    config_obj.add_section(section)
    if type(options) is dict:
        for key, value in options.items():
            config_obj.set(section, key, str(value))
    else:
        config_obj.set(section, 'value', str(options))
config_obj.write(file)
file.close()
