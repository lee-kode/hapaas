
import ConfigParser
import os

CONFIG_FILE = '/etc/hapaas/config.ini'


def get_config():
    cfg_file = os.getenv('HAPAAS_CONFIG', CONFIG_FILE)
    cfg = ConfigParser.RawConfigParser(allow_no_value=True)
    cfg.read(cfg_file)
    return cfg

