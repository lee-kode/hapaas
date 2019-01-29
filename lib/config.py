
import ConfigParser
import json
import os

# TODO: we need to put some defaults here at some point

CONFIG_FILE = '/etc/hapaas/config.ini'


def get_config():
    cfg_file = os.getenv('HAPAAS_CONFIG', CONFIG_FILE)
    config = ConfigParser.RawConfigParser()
    return config.read(cfg_file)
