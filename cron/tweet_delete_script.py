import os.path
import sys
import yaml


dir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_path, "../../"))
conf_path = path = os.path.join(dir_path, "../tweets.yaml")

from lib.twitter import Twitter

if __name__ == '__main__':
    with open(conf_path) as f:
        config_map = yaml.safe_load(f)
        for key, value in config_map['auth'].items():
            print("Deleting {} tweets".format(key))
            twitter = Twitter(**value)
            twitter.clean_up()
            print("Delete completed for {} tweets".format(key))
