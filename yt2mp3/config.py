import sys
import os
import appdirs
import codecs
import configparser
import collections

class Config(collections.UserDict):
    """
    Class for setting settings.
    """
    def __init__(self, arg):
        super(Config, self).__init__()
        self.arg = arg

        # Set default values.
        self.data = {
            'general': {
                'user_data_path': 'default'            
            }
        }

        # TODO: Generalize the config file location somehow?
        script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        config_path = os.path.join(script_dir, 'config', 'app.ini')
        print('config_path: %s' % config_path)

        if os.path.exists(config_path):
            # Add the settings from the config file to the config object.
            self.data.update(
                configparser.ConfigParser.read(config_path))
        else:
            with codecs.open(config_path, 'w', encoding='utf-8') as config_file:
               configparser.ConfigParser.write(self.data)