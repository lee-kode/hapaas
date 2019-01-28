import json
import os

# TODO: we need to put some defaults here at some point

CONFIG_FILE = '/etc/hapaas/config.json'


def get_config():
    cfg_file = os.getenv('HAPAAS_CONFIG', CONFIG_FILE)
    with open(cfg_file) as cfh:
        return json.load(cfh)
