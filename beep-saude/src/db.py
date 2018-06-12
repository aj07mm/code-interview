import redis


def get_db(db_name=0):
    pool = redis.ConnectionPool(host='redis', port=6379, db=int(db_name))
    db = redis.StrictRedis(connection_pool=pool)
    return db
