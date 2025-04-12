from urllib.parse import urlparse
import redis

def fetch(location, redis_url):
    parsed_url = urlparse(redis_url)

    try:
        r = redis.Redis(host=parsed_url.hostname, port=parsed_url.port)
        if r.exists(location):
            data = r.get(location)
            print("Fetching data from cache...")
            return data
        else:
            print("Making API request...")
            return None
    
    except redis.ConnectionError:
        print("Making API request...")
        return None 
    
    except redis.TimeoutError:
        print("Making API request...")
        return None
    
    except redis.ResponseError as e:
        print(f"Redis command error: {e}")
        print("Making API request..")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        print("Making API request...")
        return None
    
def cache(location, data, redis_url):
    parsed_url = urlparse(redis_url)
    
    try:
        r = redis.Redis(host=parsed_url.hostname, port=parsed_url.port)
        r.set(location, data, ex=300)
        print("Data cached for 5 minutes")
        current_cache = r.keys()
        print(f"Current cached locations: {current_cache}")
    except redis.ConnectionError:
        print("Redis connection error. Is the server running?")

    except redis.TimeoutError:
        print(" Redis request timed out.")

    except redis.ResponseError as e:
        print(f"Redis command error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")