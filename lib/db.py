import redis
from config import get_config

cfg = get_config()


class HapaasRedis(redis.Redis):

    def __init__(self, **kwargs):
        host = 'localhost'
        port = 6379

        if cfg.has_section('redis'):
            host = cfg.get('redis', 'host')
            port = cfg.get('redis', 'port')

        redis.Redis.__init__(self, host=host, port=port, **kwargs)
