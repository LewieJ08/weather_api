from urllib.parse import urlparse
import redis 

def cache(data, redis_url):
    parsed_url = urlparse(redis_url)
    r = redis.Redis(host=parsed_url.hostname, port=parsed_url.port)